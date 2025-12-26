# Order Processing Pipeline (OOP - Python)

Repository ini berisi simulasi pipeline data sederhana untuk memproses dan mentransformasi data pesanan pada sistem e-commerce menggunakan paradigma Object-Oriented Programming (OOP) dengan bahasa Python.

---

## Deskripsi Program

Program ini memodelkan:

- Pesanan pelanggan sebagai objek (`Order`)
- Pengelolaan banyak pesanan menggunakan kelas (`OrderProcessor`)
- Perhitungan total pendapatan dan pajak
- Penampilan detail setiap pesanan

---

## Prinsip OOP yang Digunakan

### 1. Encapsulation

Setiap pesanan direpresentasikan sebagai objek `Order` yang menyimpan data dan perilaku terkait pesanan, seperti perhitungan pajak dan tampilan detail pesanan.

### 2. Abstraction

Detail implementasi perhitungan pajak dan tampilan pesanan disembunyikan di dalam metode kelas (`calculate_tax`, `display_order`) dan hanya diakses melalui antarmuka publik.

### 3. Separation of Responsibility

- Kelas `Order` bertanggung jawab pada satu pesanan.
- Kelas `OrderProcessor` bertanggung jawab mengelola dan memproses banyak pesanan.

### 4. Reusability

Metode `display_order()` digunakan kembali oleh `display_orders()` tanpa menduplikasi kode.

---

## Command Line Interface

Untuk penggunaan aplikasi yang praktis, aplikasi sederhana ini dapat dijalankan melalui CLI dengan pilihan menu sebagai berikut:

- 1. Ubah Pajak _(mengubah rate pajak dari 11%)_
- 2. Tambahkan Order
- 3. Hitung Pendapatan Total dan Pajak
- 4. Tampilan Orders
- 5. Keluar _(menutup aplikasi)_

---

## Environment & Dependency Management (UV)

Project ini menggunakan **UV** sebagai alat manajemen environment dan dependensi Python.  
UV digunakan untuk memastikan konsistensi versi Python dan dependensi selama pengembangan dan pengujian. Alat ini digunakan karena beberapa alasan berikut :

- Lebih cepat dibandingkan `pip` dan `virtualenv`
- Menjamin reproducibility environment
- Memudahkan pengelolaan versi Python pada project

Untuk men-_set-up_ _environment_ proyek ini, silahkan jalankan perintah berikut melalui terminal:

```bash
uv venv
source .venv/bin/activate
```

Untuk menjalankannya, silahkan jalankan perintah berikut melalui terminal:

```bash
uv run main.py
```
