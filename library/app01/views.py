from django.shortcuts import HttpResponse, render, redirect
from app01 import models


# Create your views here.


# 展示出版社列表
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list.html", {"publisher_list": ret})


# # 添加新的出版社
# def add_publisher(request):
#
#     if request.method == "POST":
#         new_name = request.POST.get("publisher_name", None)
#         new_addr = request.POST.get("address", None)
#
#         models.Publisher.objects.create(name=new_name, addr=new_addr)
#
#         # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
#         return redirect("/publisher_list/")
#     return render(request, "add_publisher.html")

from django.views import View

class AddPublisher(View):
    def get(self, request):
        return render(request, "add_publisher.html")

    def post(self, request):
        new_name = request.POST.get("publisher_name", None)
        new_addr = request.POST.get("address", None)

        models.Publisher.objects.create(name=new_name, addr=new_addr)
        return redirect("/publisher_list/")

# 删除出版社的函数
def delete_publisher(request):
    print(request.GET)
    print("=" * 120)
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get("id", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在!")


# 编辑出版社
def edit_publisher(request):
    # 用户修改完出版社的名字,点击提交按钮,给我发来新的出版社名字
    if request.method == "POST":
        print(request.POST)
        # 取新出版社名字
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        new_addr = request.POST.get("address")
        # 更新出版社
        # 根据id取到编辑的是哪个出版社
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.addr = new_addr
        edit_publisher.save()  # 把修改提交到数据库
        # 跳转出版社列表页,查看是否修改成功
        return redirect("/publisher_list/")
    # 从GET请求的URL中取到id参数
    edit_id = request.GET.get("id")
    print(edit_id)
    if edit_id:
        # 获取到当前编辑的出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher": publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在!")


def book_list(request):
    all_book = models.Book.objects.all()

    return render(request, "book_list.html", {"all_book": all_book})


def book_add(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect("/book_list/")

    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "book_add.html", {"publisher_list": ret})


def book_delete(request):
    delete_id = request.GET.get("id")
    models.Book.objects.get(id=delete_id).delete()
    return redirect("/book_list/")


def book_edit(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id = new_publisher_id
        edit_book_obj.save()
        return redirect("/book_list/")

    edit_book_id = request.GET.get("id")
    edit_book_obj = models.Book.objects.get(id=edit_book_id)

    ret = models.Publisher.objects.all()
    return render(request, "book_edit.html", {"publisher_list": ret, "book_obj": edit_book_obj})


def author_list(request):
    all_author = models.Author.objects.all()
    return render(request, "author_list.html", {"all_author": all_author})


def author_add(request):
    if request.method == "POST":
        new_author_name = request.POST.get("author_name")
        new_author_book = request.POST.getlist("books")
        print(new_author_name, new_author_book)
        new_author = models.Author.objects.create(name=new_author_name)
        new_author.book.set(new_author_book)
        return redirect("/author_list/")
    ret = models.Book.objects.all()
    return render(request, "author_add.html", {"book_list": ret})


def author_del(request):
    author_del_id = request.GET.get("id")
    print(author_del_id)
    models.Author.objects.get(id=author_del_id).delete()
    return redirect("/author_list/")


def author_edit(request):
    if request.method == "POST":
        edit_author_id = request.POST.get("author_id")
        print(edit_author_id)
        new_author_edit_name = request.POST.get("author_name")
        new_author_edit_books = request.POST.getlist("books")
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_edit_name
        edit_author_obj.book.set(new_author_edit_books)
        edit_author_obj.save()
        return redirect("/author_list/")

    author_edit_id = request.GET.get("id")
    author_edit_obj = models.Author.objects.get(id=author_edit_id)
    ret = models.Book.objects.all()
    return render(request, "author_edit.html", {"book_list": ret, "author": author_edit_obj})


def test(request):
    ...
