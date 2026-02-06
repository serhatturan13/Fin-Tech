import pandas as pd
import matplotlib.pyplot as plt

try:
    # 1. Veriyi hiçbir şeyi atlamadan ham halde oku
    df = pd.read_csv("altin_verileri.csv")

    # 2. İlk 3 satır gereksiz (Price, Ticker, Date satırları). Onları atalım.
    # 3. satırdan itibaren gerçek veriler başlıyor.
    df = df.iloc[3:].copy()

    # 3. Sütun isimlerini senin CSV'ne göre manuel set edelim
    # Senin dosyanda: Tarih, Close, High, Low, Open, Volume
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    # 4. Tarihleri ve Sayıları uygun formata sokalım
    df['Date'] = pd.to_datetime(df['Date'])
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce') # Sayı olmayanları temizler
    
    df.set_index('Date', inplace=True)
    df.dropna(subset=['Close'], inplace=True) # Boş satır varsa siler

    # 5. Grafik Çizimi
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], color='gold', linewidth=2, label='Altın Kapanış ($)')
    
    plt.title('Altın Fiyat Arşivi (2023-2026)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    
    plt.savefig("altin_fiyat_grafigi.png")
    print("Grafik başarıyla oluşturuldu! 'altin_fiyat_grafigi.png' dosyasına bakabilirsin.")
    plt.show()

except Exception as e:
    print(f"Hata: {e}")