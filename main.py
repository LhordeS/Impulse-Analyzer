import pandas as pd
import yfinance as yf

df_nq = yf.download("NQ=F", interval="1m", period="7d")
df_es = yf.download("ES=F", interval="1m", period="7d")

df_nq.to_csv("nq_1m_data.csv")

# def detect_opening_inpulse(day_df, atr_value, threshold_fraction):

print(df_nq)
