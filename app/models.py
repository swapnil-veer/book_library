from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length= 25)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default= True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name
