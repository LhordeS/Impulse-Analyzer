import pandas as pd
import yfinance as yf

df_nq = yf.download("NQ-F", interval="1m", period="7d")

df_nq.index = df_nq.index.tz_convert("america/New_York")
df_nq["date"] = df_nq.index.date
df_nq.columns = df_nq.columns.get_level_values(0)

rth = df_nq.between_time("09:30", "15:59").copy()
rth["date"] = rth.index.date
one_day = rth[rth["date"] == rth["date"].iloc[0]]
opening_window = one_day.between_time("09:30", "09:59")

