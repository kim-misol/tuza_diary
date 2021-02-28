from datetime import datetime

import FinanceDataReader as fdr
import numpy as np

def bollinger_band(price_df, n=20, k=2):
    bb = price_df.copy()
    bb['mbb'] = price_df['close'].rolling(n).mean()  # 중앙 이동 평균선
    bb['ubb'] = bb['mbb'] + k * price_df['close'].rolling(n).std()  # 상단 밴드
    bb['lbb'] = bb['mbb'] - k * price_df['close'].rolling(n).std()  # 하단 밴드

    return bb

def data_settings(code, start=datetime(2020, 1, 1), end=datetime.today()):
    # 비트코인 원화 가격 (빗썸) 2016년~현재
    price_df = fdr.DataReader(code, start=start, end=end)
    # 결측치 존재 유무 확인
    invalid_data_cnt = len(price_df[price_df.isin([np.nan, np.inf, -np.inf]).any(1)])

    if invalid_data_cnt == 0:
        price_df['date'] = price_df.index

        price_df['open'] = price_df.iloc[:]['Open'].astype(np.float64)
        price_df['high'] = price_df.iloc[:]['High'].astype(np.float64)
        price_df['low'] = price_df.iloc[:]['Low'].astype(np.float64)
        price_df['close'] = price_df.iloc[:]['Close'].astype(np.float64)
        price_df['volume'] = price_df.iloc[:]['Volume']
        price_df = bollinger_band(price_df)
        df = price_df.loc[:, ['date','open', 'high', 'low', 'close', 'volume', 'ubb', 'mbb', 'lbb']].copy()
        return df
    return False
