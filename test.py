import os
from datetime import datetime

import FinanceDataReader as fdr
import numpy as np

from library.graphs import draw_candle_with_indicator
from library.trading_indicators import bollinger_band


def data_settings(code, start=datetime(2020, 1, 1), end=datetime.today()):
    # 비트코인 원화 가격 (빗썸) 2016년~현재
    price_df = fdr.DataReader(code, start=start, end=end)
    # 결측치 존재 유무 확인
    invalid_data_cnt = len(price_df[price_df.isin([np.nan, np.inf, -np.inf]).any(1)])

    if invalid_data_cnt == 0:
        price_df['open'] = price_df.iloc[:]['Open'].astype(np.float64)
        price_df['high'] = price_df.iloc[:]['High'].astype(np.float64)
        price_df['low'] = price_df.iloc[:]['Low'].astype(np.float64)
        price_df['close'] = price_df.iloc[:]['Close'].astype(np.float64)
        price_df['volume'] = price_df.iloc[:]['Volume']
        price_df = bollinger_band(price_df)
        df = price_df.loc[:, ['open', 'high', 'low', 'close', 'volume', 'ubb', 'mbb', 'lbb']].copy()
        return df
    return False


def save_graph(coin_df, code):
    # $ 그래프 그리기
    # draw_candle(coin_df, code)
    fig = draw_candle_with_indicator(coin_df, code)
    today = str(datetime.today())[:10].replace('-', '')
    fcode = code.replace('/', '-')

    if not os.path.exists("img"):
        os.mkdir("img")
    if not os.path.exists(f"img/{today}"):
        os.mkdir(f"img/{today}")

    # fig.write_image(f"img/{today}/{fcode}.png")
    fig.write_html(f"img/{today}/{fcode}.html")


if __name__ == "__main__":
    # 주식 또는 가상암호화폐 종목 코드 리스트 가져오기
    # $ 코드 리스트
    code_list = ['ETH/KRW']
    # code_list = ['155660', '001250', '294870', '001390', '011070']
    # use_graph = True if input(f"그래프 저장 여부 : (y or n) ") == 'y' else False
    use_graph = True
    # if use_graph not in ('y', 'n') or use_ai_filter not in ('y', 'n'):
    #     print('y 또는 n을 입력해주세요.')
    #     exit(1)

    for code in code_list:
        print(f"종목 코드: {code}")
        get_data_start = datetime.now()
        # 종목별 데이터
        # 데이터 언제부터 가져올지 설정
        coin_df = data_settings(code=code, start=datetime(2018, 1, 1))
        save_graph(coin_df, code)
