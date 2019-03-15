from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)
    phone=models.CharField(max_length=20)
    addtime=models.DateTimeField()


def __str__(self):
    return "%d:%s:%d:%s:%s" % (self.id,self.name, self.age, self.phone, self.addtime)


class Meta:
    #db_table = "stu"
    verbose_name = '浏览用户信息'
    verbose_name_plural = '用户信息管理'