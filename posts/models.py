from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    market = models.CharField(max_length=10)
    code_name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    summary = models.TextField()

    chart_data_json = models.CharField(max_length=50)

    buy_price = models.FloatField()
    buy_date = models.DateField()
    buy_memo = models.TextField()

    sell_price = models.FloatField()
    sell_date = models.DateField()
    sell_memo = models.TextField()

    to_sell_price = models.FloatField()
    to_sell_datee = models.DateField()
    to_buy_price = models.FloatField()
    to_buy_datee = models.DateField()

