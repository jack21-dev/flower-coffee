# ☕ Flower Coffee Web App

Selamat datang di **Flower Coffee**, sebuah website toko kopi sederhana yang dibangun menggunakan **Flask (Python)** dan **HTML/CSS**, dilengkapi dengan database **SQLite** untuk menyimpan pesan dari pelanggan.

---

## 🚀 Fitur Utama

- ✅ Halaman Beranda, Menu, Tentang, dan Kontak
- ✅ Formulir Kontak yang menyimpan pesan ke database
- ✅ Validasi backend untuk keamanan input
- ✅ Halaman Admin (dengan login/logout)
- ✅ Hapus pesan pelanggan satu per satu
- ✅ Export data pesan ke file CSV (bisa dibuka di Excel)

---

## 🔧 Teknologi yang Digunakan

- Python 3 + Flask
- HTML/CSS
- SQLite (database lokal)
- Jinja2 (template engine Flask)

---

## 🔑 Login Admin

| Username | Password |
|----------|----------|
| admin    | 1234     |

---

## 📦 Struktur Folder

flower-coffee/
├── app.py
├── templates/
│ ├── index.html
│ ├── menu.html
│ ├── tentang.html
│ ├── kontak.html
│ ├── login.html
│ └── admin.html
├── .gitignore
└── README.md


---

## ▶️ Cara Menjalankan Proyek

```bash
git clone https://github.com/jack21-dev/flower-coffee.git
cd flower-coffee
pip install flask
python app.py

Lalu buka di browser: http://localhost:5000

📤 Export Pesan ke CSV
Setelah login ke /admin, klik tombol "Download CSV" untuk ekspor data ke Excel.

🛡️ Validasi & Keamanan
Input nama dan pesan divalidasi tidak boleh kosong

Data disanitasi dengan html.escape() untuk mencegah XSS

Halaman admin dilindungi session login

💡 Catatan
Database pesan.db akan otomatis dibuat saat aplikasi dijalankan

Jangan lupa ubah secret_key untuk proyek produksi

📃 Lisensi
Proyek ini dibuat untuk latihan dan edukasi. Bebas digunakan, dimodifikasi, dan dikembangkan.

Dibuat dengan semangat belajar oleh jack21-dev ✨


---

### ✅ Selanjutnya

1. Simpan isi di atas sebagai file `README.md`
2. Tambahkan ke Git:
   ```bash
   git add README.md
   git commit -m "Menambahkan README.md"
   git push
3. Buka repo GitHub ➜ tampilan akan jadi rapi otomatis 💻✨
