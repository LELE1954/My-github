from django.db import models

# Create your models here.

# 图书管理系统, 书  作者 出版社


# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)  # 自增的ID主键
    # 创建一个varchar(64)的唯一的不为空的字段
    name = models.CharField(max_length=64, null=False, unique=True)
    addr = models.CharField(max_length=128, default="番禺大道27号")

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher")

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author Object:{}>".format(self.name)