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
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('book/admin/', admin.site.urls),

    # book urls
    path('',include('app.urls')),

    # user app url's
    path('user/',include('user_app.urls')),

    # class based views
    path('cbv/',include('cbv_app.urls')),

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

# class based views
# http://127.0.0.1:8000/cbv/view/
# http://127.0.0.1:8000/cbv/emp-create
# http://127.0.0.1:8000/cbv/emp-list
# http://127.0.0.1:8000/cbv/emp-detail/1
# http://127.0.0.1:8000/cbv/emp-update/1


