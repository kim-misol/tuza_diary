from django.shortcuts import render

import websockets
import asyncio
from .models import Post


# index.html 페이지를 부르는 index 함수 (post list를 보여준다)
def index(request):
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'main/index.html', {'postlist': postlist})


# post.html 페이지를 부르는 post 함수
def _post(request):
    return render(request, 'main/post.html')


# post.html 페이지를 부르는 post 함수
def post(request, post_id):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=post_id)
    # post.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/post.html', {'post': post})


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
                                       "value": "5861540624.04524", "volume": "107.85047173",
                                       "sellVolume": "59.07722415",
                                       "buyVolume": "48.77324758", "prevClosePrice": "53672000", "chgRate": "0.05",
                                       "chgAmt": "29000", "volumePower": "82.56", "symbol": "BTC_KRW"}}


if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(get_crytocurrency_ticker())
    data_processing()
