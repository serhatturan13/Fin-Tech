import yfinance as yf
import pandas as pd

#hangi veriyi istiyoruz?/(Ex:Altın- GC=F veya Türk Hava Yolları- THYAO.IS)
symbol = "GC=F"
# 2. veriyi çekelim
print(f"{symbol} veriler indiriliyor")
data = yf.download(symbol, start="2023-01-01", end="2026-01-01")
# 3. ilk 5 satıra bir bakalım (matematiksel kontrol)
print(data.head())
#4. veriyi bir CSV dosyasına kaydedelim ki elimizde somut bir şey olsun
data.to_csv("altin_verileri.csv")
print("veri başarıyla 'altin_verileri.csv' olarak kaydedildi")
