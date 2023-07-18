from django.contrib.auth.models import User
from app.models import Book
from relationship.models import Aadhar, Person, Car, CarModel, CModel, Fueltype
# exec(open(r"E:\New folder_python\New folder_python\Djangoprojects\Book_library\relationship\db_shell.py").read())
import random

# u = User.objects.get(id = random.randint(1,4))
# p = Person.objects.get(id = random.randint(1,4))


# p1 = Person.objects.create( name = "swapnil", age = 27, email = '123@gmail.com', mobile = 9871236589, created_by = u)
# p2 = Person.objects.create( name = "veer", age = 23, email = 'veer@gmail.com', mobile = 9871214529, created_by = u)
# p2 = Person.objects.create( name = "abc", age = 27, email = 'abc@gmail.com', mobile = 9871215852, created_by = u)
# p5 = Person.objects.create( name = "xyz", age = 27, email = 'xyz@gmail.com', mobile = 9871245895, created_by = u)
# from django.utils import timezone
#  address
# a1=  Aadhar.objects.create(aadhar_number = 1332453466, address ="hj kjk kjljl", DOB =timezone.datetime(1995,1,21) , person = p , created_by = u )# instannce method  
# a2 = Aadhar.objects.create(aadhar_number = 98753466, address ="qwqw l", DOB =timezone.datetime(1997,7,21) , person_id = 1, created_by_id = 1 )# id method

# a = Aadhar.objects.get(id =1)
# print(a.__dict__)
# a1  = Aadhar.objects.select_related("person").get(aadhar_number = 1332453466 )
# print(a1.person)

# c1 = Car.objects.create(name = 'TATA')
# c1 = Car.objects.create(name = 'BMW')

# f1 = CarModel.objects.create(name = "C127", car = c1)
# f = CarModel.objects.get(name = "C127")
# print(f.car)
# print(f.car.__dict__)

# c180 = CModel.objects.create( name="C180")
# c200 = CModel.objects.create(name="C200")
# CarModel.objects.all()

c180 = CModel.objects.get(name = "C180")
c200 = CModel.objects.get(name = "C200")

petrol  = Fueltype.objects.get(name = "Petrol")
diesel  = Fueltype.objects.get(name = "Diesel")
cng  = Fueltype.objects.get(name = "CNG")

# c180.fueltype.add(cng)
# c200.fueltype.add(petrol)             #add petrol fueltype to c200 model
# c200.fueltype.add(diesel,cng)         #add diesel and cng fueltype in same line
print(c200.fueltype.all())

# c200.fueltype.create(name = "Bio diesel")    # fueltype created and assigned to c200 model same time

book = Book.objects.all()
# print(book)
# for user in User.objects.all():
#     print(user)

for i in book:
    print(i.name)