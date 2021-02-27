# tuza_diary

# installation
```angular2html
pip install -r requirements.txt
```

# run application
```
python manage.py runserver
```

# trouble shooting
1. pipfile 필요한가?


# Django
## 장고 프로젝트 시작

web_study라는 프로젝트를 하나 만들어 보자.

```bash
django-admin startproject tuza_diary
```
장고 프로젝트를 만들면 `tuza_diary`라는 폴더가 생성된다
```bash
cd tuza_diary
```

## 첫 페이지 만들기

프로젝트를 만들었지만 우리가 페이지를 추가하려면 앱(App)이라는 것을 만들어야 한다.
위에서 말했듯이, 장고의 모든 프로젝트는 여러개의 HTML과 .py파일로 이루어진 앱들이 여러개 모여서 만들어진다.
`posts`이라는 이름의 첫 번째 앱을 만들어보자.

```bash
python manage.py startapp posts
```
여기까지 했다면 기초공사가 완료된 것이다!
이제 `tuza_diary/posts/templates/main`폴더를 하나 만들어,
그 안에 `index.html`파일을 만들어주자.
`index.html`에는 그냥 알아볼 수 있도록 표시만 해주자.

이제 우리가 만들 html파일을 인코딩해서 웹에 띄우는 작업을 해야한다.
`posts/views.py`파일을 열어 다음 코드를 추가해준다.

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')
```

이제 마지막으로 우리의 **view**와 **url**을 연결만 해주면 된다.
`posts/urls.py`파일을 하나 새로 만들어 아래의 코드를 추가해준다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

이 앱의 **url**과 프로젝트의 **url**을 연결해주자 `tuza_diary/urls.py`에 들어가서 아래와 같이 바꿔준다.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

# psql

1. Open 'SQL Shell (psql)'
   
1. Command list 
    | command | description |
    |---|---|
    | \l | Database list |
    | \dt | Table list |
    | \c [database_name] | connect to DB |
    | \q | get out of psql |
    | \h | help | 
   
1. Create Database  
    `CREATE DATABASE schedulbot`
   
1. Check database created  
    `\l`
   
1. Access to schedulebot DB  
    `\c schedulebot`
   
1. Check Table created  
    `\dt`  
   

### 참고자료
[Django로 게시판 만들기](https://wikidocs.net/91422)