from django.db.models import Model, CharField, TextField, JSONField, DateField, FloatField


# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(Model):
    postname = CharField(max_length=50)
    market = CharField(max_length=10)
    code_name = CharField(max_length=20)
    code = CharField(max_length=10)
    summary = TextField(null=True)

    chart_data_json = JSONField(null=True)

    buy_price = FloatField(null=True)
    buy_date = DateField(null=True)
    buy_memo = TextField(null=True)

    sell_price = FloatField(null=True)
    sell_date = DateField(null=True)
    sell_memo = TextField(null=True)

    to_sell_price = FloatField(null=True)
    to_sell_date = DateField(null=True)
    to_buy_price = FloatField(null=True)
    to_buy_date = DateField(null=True)

    def __str__(self):
        return self.postname
