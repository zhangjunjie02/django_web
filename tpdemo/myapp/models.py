from django.db import models

# Create your models here.
# 自定义的城市区县信息model类
class District(models.Model):
    name=models.CharField(max_length=255)
    upid=models.IntegerField()

class Meta:
    #指定真实表名
    db_table="district"

