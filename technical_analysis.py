import pandas as pd
import numpy as np

def calculate_sma(data, window):
    """Basit Hareketli Ortalama"""
    return data['Close'].rolling(window=window).mean()

def calculate_ema(data, span):
    """Üstel Hareketli Ortalama"""
    return data['Close'].ewm(span=span, adjust=False).mean()

def calculate_rsi(data, period=14):
    """Relative Strength Index (0-100 arası)"""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data, fast=12, slow=26, signal=9):
    """MACD Göstergesi"""
    ema_fast = data['Close'].ewm(span=fast, adjust=False).mean()
    ema_slow = data['Close'].ewm(span=slow, adjust=False).mean()
    
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    
    return macd, signal_line, histogram

def calculate_bollinger_bands(data, window=20, num_std=2):
    """Bollinger Bantları"""
    sma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    
    upper_band = sma + (std * num_std)
    lower_band = sma - (std * num_std)
    
    return upper_band, sma, lower_band

def calculate_volatility(data, window=30):
    """Volatilite (Standart Sapma)"""
    returns = data['Close'].pct_change()
    return returns.rolling(window=window).std() * np.sqrt(252) * 100  # Yıllık volatilite