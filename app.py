from flask import Flask, render_template, request, redirect, session, url_for, make_response 
from html import escape  # ✅ Ini yang benar
import sqlite3
import csv
import io



app = Flask(__name__)
app.secret_key = 'flowercoffee123'  # Bebas, tapi rahasiakan kalau produksi


# ✅ Buat tabel jika belum ada
def init_db():
    conn = sqlite3.connect('pesan.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS pesan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            pesan TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Data menu kopi
menu_kopi = [
    {"nama": "Kopi Tubruk", "harga": 10000},
    {"nama": "Es Kopi Susu", "harga": 15000},
    {"nama": "Americano", "harga": 20000},
    {"nama": "Cappuccino", "harga": 25000},
    {"nama": "Latte", "harga": 25000},
]

@app.route('/')
def beranda():
    return render_template("index.html")

@app.route('/menu')
def menu():
    return render_template("menu.html", menu=menu_kopi)

@app.route('/tentang')
def tentang():
    return render_template("tentang.html")

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form['nama'].strip()
        pesan = request.form['pesan'].strip()

        # Validasi backend: tidak boleh kosong
        if not nama or not pesan:
            error = "Nama dan pesan tidak boleh kosong."
            return render_template("kontak.html", sukses=False, error=error)

        # Escape karakter berbahaya
        nama = escape(nama)
        pesan = escape(pesan)

        conn = sqlite3.connect('pesan.db')
        c = conn.cursor()
        c.execute('INSERT INTO pesan (nama, pesan) VALUES (?, ?)', (nama, pesan))
        conn.commit()
        conn.close()

        return render_template("kontak.html", sukses=True, nama=nama)

    return render_template("kontak.html", sukses=False)

@app.route('/admin')
def admin():
    if not session.get('admin'):
        return redirect(url_for('login'))

    conn = sqlite3.connect('pesan.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nama, pesan FROM pesan ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return render_template("admin.html", pesan=data)

@app.route('/hapus/<int:id>')
def hapus(id):
    if not session.get('admin'):
        return redirect(url_for('login'))

    conn = sqlite3.connect('pesan.db')
    c = conn.cursor()
    c.execute('DELETE FROM pesan WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('admin'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Ganti dengan pengecekan sesuai kebutuhanmu
        if username == 'admin' and password == 'kopi':
            session['admin'] = True
            return redirect(url_for('admin'))

        return render_template("login.html", error=True)

    return render_template("login.html", error=False)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

@app.route('/export')
def export_csv():
    if not session.get('admin'):
        return redirect(url_for('login'))

    conn = sqlite3.connect('pesan.db')
    c = conn.cursor()
    c.execute("SELECT id, nama, pesan FROM pesan ORDER BY id DESC")
    data = c.fetchall()
    conn.close()

    # Tulis ke StringIO
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Nama', 'Pesan'])
    writer.writerows(data)

    # Buat response
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=pesan.csv"
    response.headers["Content-Type"] = "text/csv"
    return response



conn = sqlite3.connect("pesan.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM pesan")
data = cursor.fetchall()

for row in data:
    print(row)

conn.close()

if __name__ == '__main__':
    app.run(debug=True)