import streamlit as st
import requests
import pandas as pd

# FastAPIエンドポイント
fast_api_endpoint = "http://127.0.0.1:8000/"

# FastAPIからデータを取得
response = requests.get(fast_api_endpoint)
data = response.json()

# データをPandasのDataFrameに変換
df = pd.DataFrame(data)

# Streamlitでタイトルとデータテーブルを表示
st.title('ゲームデータ')
st.dataframe(df)
