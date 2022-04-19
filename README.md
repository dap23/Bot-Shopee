# Instalasi

* Download Webdriver untuk firefox "https://github.com/mozilla/geckodriver". Pilih versi yang sesuai dengan versi firefox
   Cara melihat versi firefox:
   - Buka firefox > klik titik 3 di pojok kanan atas > Help > About Firefox
* Setelah di download, unzip folder driver dan pindahkan folder ke localdisk C
* Kemudian buka System Properties > Advanced > Environment Variable
* Setelah Environment Variable terbuka pada system variable cari Path lalu klik 2x atau klik lalu pilih edit
* Pilih New dan paste kan path folder geckodriver
* Apabila webdriver telah terinstall sekarang install pip
* Ketik pada cmd 
```
pip3 -r requirements.txt
```
# Cara Menggunakan Bot

```
python3 shopee.py
```
2. Masukan link product shopee yang ingin di beli
3. Masukan waktu pembelian
4. Firefox akan terbuka sendiri, lalu pilih metode login (Disarankan scan barcode untuk login)
5. Enjoy
