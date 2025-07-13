// ========== TAMPILKAN MENU KOPI DINAMIS ==========
const menuKopi = [
  { nama: "Kopi Tubruk", harga: 10000 },
  { nama: "Es Kopi Susu", harga: 15000 },
  { nama: "Americano", harga: 20000 },
  { nama: "Cappuccino", harga: 25000 },
  { nama: "Latte", harga: 25000 },
];

// Jalankan hanya jika elemen .menu-list ada
document.addEventListener("DOMContentLoaded", () => {
  const menuContainer = document.querySelector(".menu-list");
  if (menuContainer) {
    menuKopi.forEach((item) => {
      const div = document.createElement("div");
      div.className = "menu-item";
      div.innerHTML = `<h3>${
        item.nama
      }</h3><p>Rp${item.harga.toLocaleString()}</p>`;
      menuContainer.appendChild(div);
    });
  }
});

function bukaPopup() {
  document.getElementById("popup").style.display = "flex";
}

function tutupPopup() {
  document.getElementById("popup").style.display = "none";
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("formKontak");
  const sukses = document.getElementById("sukses");

  form.addEventListener("submit", (e) => {
    e.preventDefault(); // Hindari reload

    // Ambil nilai
    const nama = document.getElementById("nama").value;
    const pesan = document.getElementById("pesan").value;

    if (nama && pesan) {
      console.log("Pesan dari", nama + ":", pesan);
      sukses.style.display = "block";
      form.reset();
    }
  });
});

function bukaPopup() {
  document.getElementById("popup").style.display = "flex";
}

function tutupPopup() {
  document.getElementById("popup").style.display = "none";
}
