from django.shortcuts import render,HttpResponse
from app.models import Book
from django.contrib.auth.decorators import login_required
import csv
from django.contrib.auth.models import User

@login_required
def create_csv(request):
    book = Book.objects.filter(is_active = True)
    response = HttpResponse(content_type="text/csv",headers={"Content-Disposition": 'attachment; filename="test.csv"'})
    lst = [("name","price", "qty", "is_published", "created_by", "is_active"),]
    writer = csv.writer(response)
    # writer.writerow(["name","price", "qty", "is_published", "created_by", "is_active"])
    for single_book in book:
        lst.append((single_book.name, single_book.price, single_book.qty, single_book.is_published, single_book.created_by, single_book.is_active))
    writer.writerows(lst)

    return response


@login_required
def upload_csv(request):
    file = request.FILES["CSV_FILE"]
    decoded_file  = file.read().decode('utf-8').splitlines()
    # print(decoded_file)

    reader = csv.DictReader(decoded_file)
    lst = []
    for element in reader:
        try:
            u = User.objects.get(username = element.get("created_by"))
        except:
            u = None
        lst.append(Book(name = element.get("name"), price = element.get("price"), qty = element.get("qty"), is_published = element.get("is_published"), created_by= u, is_active=element.get("is_active") ))
        # print(element)
    Book.objects.bulk_create(lst)
    return HttpResponse("success")

