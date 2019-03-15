from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    title=models.CharField(max_length=40)
    photo=models.ImageField()
    createtime=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title+":"+self.photo+":"+self.createtime

    class Meta:
        #指定表名
        db_table="user"









