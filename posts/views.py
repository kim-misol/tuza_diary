from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# post.html 페이지 부르는 함수
def post(request):
    return render(request, 'main/post.html')