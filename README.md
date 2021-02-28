# TUZA Diary
주식 또는 가상암호화폐 투자 다이어리

# Requirements
You need to install three packages on your machine:
- Node.js: The JavaScript runtime that you will use to run your frontend project.
- Python 3.8+: A recent Python 3 interpreter to run the Flask backend on.
- PostgreSQL 12.5+

# Clone the sources
```bash
git clone https://github.com/kim-misol/tuza_diary.git
```
# Installation
```angular2html
pip install -r requirements.txt
```

# Run Application
```
python manage.py runserver
```

# trouble shooting
1. pipfile 필요한가?

---

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

[post.html 추가](https://wikidocs.net/91420)

## `Model` 만들기
장고에서는 `Model`을 지원해준다.
이 모델을 이용해 게시판에서 각각의 게시글이 데이터베이스에 어떻게 저장될지를 정해준다.

장고가 이 모델을 데이터베이스에 넣어 저장할 수 있도록 해준다.
즉, `django`의 db에 `migrate`해준다.
일반적인 경우 `model.py`를 수정했다면 바로바로 `migrate`해주어서 우리가 만든 `model`을 데이터베이스에 저장한다.

### `Ctrl + C`를 눌러 웹서버를 종료 후 migration
```bash
python manage.py makemigrations 
python manage.py migrate
```

### Admin에 권한
관리자(admin)가 게시글(Post)에 접근할 권한을 준다.
게시글 게시, 삭제, 수정, 저장 등 여러 작업을 할 수 있게 해준다.

`tuza_diary/posts/admin.py`
```python
from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)
```

하지만 admin계정이 없어서 확인할 수가 없다. 관리자 계정을 만들어보자!

### Superuser 만들기
`Superuser`는 `django` 프로젝트의 모든 `app` 및 `object`를 관리하는 계정이다.
`manage.py`를 통해 `Superuser`계정이 생성되며
`username`, `email address`, 그리고 강한 `password`가 필요하다.

for mac:
```bash
python3 manage.py createsuperuser
```
for windows:
```bash
python manage.py createsuperuser
```
아래와 같이 Superuser 계정을 생성
```
Username (leave blank to use '...'): 
Email address: 
Password:
Password (again):
```
서버를 키고 생성한 `Superuser` 계정을 확인한다.

for mac:
```bash
python3 manage.py runserver
```
for windows:
```bash
python manage.py runserver
```

`http://자신의URL:8000/admin`으로 접속한다.
`Superuser`의 아이디와 비밀번호를 입력해 관리자 페이지로 들어간다.

### Post 작성 시 post name 으로 post 제목 사용 
현재 코드에서 게시글을 작성하면
게시글 제목이 나오지 않고 Post `object(1), (2)`로 나온다.
이를 `postname`이 `Post object` 대신 들어가도록 개선해보자.
이땐 게시글(`Post`)의` model`을 개선하자.

`tuza_diary/posts/models.py`

```python
from django.db import models

class Post(models.Model):
    ...

    def __str__(self):
        return self.postname
```

안의 내용을 알 수 없는 `Post Object` 대신
게시글(`Post`)의 제목(`postname`)으로 바꾸었다.

### 포스트 리스트를 보여줄 페이지 생성
`tuza_diary/posts/views.py`  
`View`(`post` 함수)가 `Model`(`Post` 게시글)을 가져온다.
```python
# index.html 페이지를 부르는 index 함수 (post list를 보여준다)
def index(request):
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'main/index.html', {'postlist': postlist})
```

### 포스트 세부 페이지
포스트마다 `post` 세부 페이지를 만들어보자.  
`tuza_diary/posts/views.py`  
`post.html`에서 포스트-세부페이지에 특정 post 1개만 가져오자.
```python
# post.html 페이지를 부르는 post 함수
def post(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # post.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/post.html', {'post': post})
```

`tuza_diary/posts/urls.py`

첫번째 포스트 세부페이지 들어가기

```python
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(post)
    path('post/<int:pk>', post, name='post'),
]
```
개별 게시글 상세 페이지를 보여준다.




### post.html에서 posting.html 링크
post 게시판에서 게시글의 제목만 남기고,
제목을 클릭하면 post의 세부페이지로 가도록 만들자.  
`tuza_diary/posts/templates/main/index.html`  
`<li>`태그에 `<a>`태그를 넣어 이동할 수 있도록 하자.

```html
<html>
    <head>
       <title>투자 다이어리</title>
    </head>
    <body>
        <h1>게시판 페이지</h1>
        <table>
        {% for list in postlist %}
            <ul>
                <li><a href="{{list.pk}}/">{{list.postname}} ({{list.market}}: {{list.code_name}})</a></li>
            </ul>
        {% endfor %}
        </table>
    </body>
</html>
```

---

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
    `CREATE DATABASE postgres`
   
1. Check database created  
    `\l`
   
1. Access to postgres DB  
    `\c postgres`
   
1. Check Table created  
    `\dt`  
   

### 참고자료
[Django로 게시판 만들기](https://wikidocs.net/91422)