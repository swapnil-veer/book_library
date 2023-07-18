from django.shortcuts import render,HttpResponse
from app.models import Book
from django.contrib.auth.decorators import login_required

@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active = True)
    return render(request, "show_books.html", {"allbooks" : books})

@login_required
def show_single_book(request,bid):
    try:
        book_obj = Book.objects.get(id = bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    return render(request, 'bookdetail.html', {"book": book_obj})