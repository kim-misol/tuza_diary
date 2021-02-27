from django.shortcuts import render

import websockets
import asyncio


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


# post.html 페이지 부르는 함수
def post(request):
    return render(request, 'main/post.html')


# bithumb websocket api
async def get_crytocurrency_ticker(type="ticker", code="BTC_KRW", tick_type="30M"):
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        greeting = await websocket.recv()
        print(greeting)

        # 구독 요청
        data = {"type": type, "symbols": [code], "tickTypes": [tick_type]}
        # data = '{"type":"ticker", "symbols": ["BTC_KRW"], "tickTypes": ["30M"]}'

        # data = f"\{'type': {type}, 'symbols': [{code}], 'tickTypes': [{tick_type}]\}"
        await websocket.send(str(data))

        print("after send data")

        while True:
            recv_data = await websocket.recv()
            print(recv_data)


def data_processing():
    d = {"type": "ticker", "content": {"tickType": "30M", "date": "20210227", "time": "163703", "openPrice": "54234000",
                                   "closePrice": "54263000", "lowPrice": "54102000", "highPrice": "54519000",
                                   "value": "5861540624.04524", "volume": "107.85047173", "sellVolume": "59.07722415",
                                   "buyVolume": "48.77324758", "prevClosePrice": "53672000", "chgRate": "0.05",
                                   "chgAmt": "29000", "volumePower": "82.56", "symbol": "BTC_KRW"}}


if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(get_crytocurrency_ticker())
    data_processing()
