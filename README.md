# Instalasi

1. Download Webdriver untuk chrome "https://chromedriver.chromium.org/downloads". Pilih versi yang sesuai dengan versi chrome
   Cara melihat versi chrome:
   - Buka chrome > klik titik 3 di pojok kanan atas > Help > About chrome
2. Setelah di download, unzip folder driver dan pindahkan folder ke localdisk C
3. Kemudian buka System Properties > Advanced > Environment Variable
4. Setelah Environment Variable terbuka pada system variable cari Path lalu klik 2x atau klik lalu pilih edit
5. Pilih New dan paste kan path folder chromedriver
6. Apabila webdriver telah terinstall sekarang install pip
7. Ketik pada cmd pip3 -r requirements.txt

# Cara Menggunakan Bot

1. python3 shopee.py
2. Masukan link product shopee yang ingin di beli
3. Masukan waktu pembelian
4. Chrome akan terbuka sendiri, lalu pilih metode login (Disarankan scan barcode untuk login)
5. Enjoy
