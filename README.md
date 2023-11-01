## Header Checker
![image](https://github.com/0xkucing/HeaderCheck/assets/105418279/69d35969-2dfe-44a0-9b3d-f8930168b131)


Header Checker adalah sebuah alat (tool) berbasis Python yang dirancang untuk memeriksa keberadaan header keamanan pada subdomain yang diberikan. Alat ini memungkinkan pengguna untuk memeriksa tiga header keamanan web yang penting: `X-Frame-Options`, `X-XSS-Protection`, dan `Content-Security-Policy`. Dengan menggunakan daftar subdomain yang disediakan dalam file teks (seperti `subdomain.txt`), tools ini mengirimkan permintaan HTTP ke setiap subdomain, mengambil halaman web, dan memeriksa keberadaan header keamanan tersebut. Setelah itu, hasilnya ditampilkan dalam konsol dengan menyertakan informasi status code, judul halaman web, serta keberadaan atau ketidakhadiran dari ketiga header tersebut.

**Cara Penggunaan:**

1. Pengguna menyediakan file teks yang berisi daftar subdomain yang akan diperiksa (misalnya, `subdomain.txt`).
2. Alat ini dijalankan melalui baris perintah dengan menyertakan nama file teks subdomain sebagai argumen (misalnya, `python3 headercek.py -l subdomain.txt`).
3. Alat akan melakukan pemeriksaan pada setiap subdomain dan menampilkan hasilnya dalam konsol.

**Catatan Penting:**

- Pastikan penggunaan alat ini sesuai dengan etika pengujian keamanan dan hukum yang berlaku. Jangan melakukan pemindaian tanpa izin pada situs web atau subdomain yang tidak dimiliki oleh Anda.
