from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render

from app.forms import AddressForm, Book_form, LoginPage
from app.models import Book

# Create your views here.

@login_required
def welcome_page(request):
    return render(request, "welcome.html")



def common_var(request):
    final_dict = request.POST
    book_name = final_dict.get('nm')
    book_price = final_dict.get('prc')
    book_qty = final_dict.get('qty')
    book_is_pub = final_dict.get('ispub')
    return book_name, book_price, book_qty, book_is_pub

@login_required
def add_single_book(request):
    if request.method == "POST":
        user = request.user
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == 'Yes':
            book_is_published = True
        else:
            book_is_published = False

        Book.objects.create(name=book_name,price = book_price, qty= book_qty,is_published = book_is_published, is_active = True, created_by = user)
        messages.success(request,"Book added successfully...!")
        return redirect("show_books")
    
    elif request.method == "GET":
        return render(request,'addbook.html' )
    
@login_required
def edit_book(request, bid):
    book_obj = Book.objects.get(id = bid)
    if request.method == "GET":
        return render(request, 'edit_book.html', {'book' : book_obj })
    elif request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)

        if book_is_pub == 'Yes':
            book_is_published = True
        else:
            book_is_published = False

        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_published = book_is_published
        book_obj.save()
        messages.success(request,f"Book : {book_obj.name} has been updated successfully...!")
        return redirect("show_books")

@login_required
def delete_single_book(request,bid):
    book_obj = Book.objects.get(id = bid)
    book_obj.delete()
    return redirect('show_inactive_books')

@login_required
def soft_delete_book(request,bid):
    book_obj = Book.objects.get(id = bid)
    book_obj.is_active = False
    book_obj.save()
    return redirect('show_books')

@login_required
def show_inactive_books(request):
    book_obj = Book.objects.filter(is_active = False)
    return render(request, 'show_inactive_books.html', {'allbooks': book_obj})
    

@login_required
def restore_book(request,bid):
    book_obj = Book.objects.get(id = bid)
    book_obj.is_active = True
    book_obj.save()
    return redirect('show_inactive_books')


@login_required
def view_page(request):
    if request.method == "POST":
        print( " in post request")
        data = request.POST
        print(data)
        form = Book_form(data)
        if form.is_valid():
            form.save()
        return redirect("show_books")
    elif request.method == "GET":
        return render(request, 'form_test.html', {'form' : Book_form()})
    

    