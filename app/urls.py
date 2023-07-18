"""
URL configuration for Book_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import welcome_page, show_all_books, show_single_book, add_single_book,edit_book,delete_single_book,soft_delete_book,show_inactive_books, restore_book, view_page, create_csv, upload_csv


urlpatterns = [
    path("book/home/", welcome_page, name= "home_page" ),
    path("book/show-books/", show_all_books, name="show_books"),
    path("book/show-single-books/<int:bid>", show_single_book, name="show_single_books"),
    path("book/add-book/", add_single_book, name="add_single_book"),
    path("book/edit-book/<int:bid>", edit_book, name="edit_book"),
    path("book/delete-single-book/<int:bid>",delete_single_book, name="delete_single_book"),
    path("book/soft-delete-book/<int:bid>",soft_delete_book, name="soft_delete_book"),
    path("book/show-inactive-books/",show_inactive_books, name="show_inactive_books"),
    path("book/restore-book/<int:bid>",restore_book, name="restore_book"),
    path("book/form-view/",view_page, name="form_view"),
    path("book/csv-file",create_csv, name="create_csv"),
    path("book/upload-csv",upload_csv, name="upload_csv"),



]


# patterns/url patterns/urls/endpoints---
# http://127.0.0.1:8000/book/admin/s
# http://127.0.0.1:8000/book/home/
# http://127.0.0.1:8000/book/show-books/
# http://127.0.0.1:8000/book/show-single-books/1
# http://127.0.0.1:8000/book/add-book/
# http://127.0.0.1:8000/book/edit-book/1
# http://127.0.0.1:8000/book/delete-single-book/1
# http://127.0.0.1:8000/book/soft-delete-book/1
# http://127.0.0.1:8000/book/show-inactive-books
# http://127.0.0.1:8000/book/restore-book/


#  user_app urls
# http://127.0.0.1:8000/user/signup/