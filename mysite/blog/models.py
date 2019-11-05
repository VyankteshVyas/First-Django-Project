from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    Note = models.TextField()
    Publisher = models.CharField(max_length=200)
    Issued_to = models.CharField(max_length=200)
    book_code=models.CharField(max_length=200)
    Isuued_date = models.DateField(blank=True,null=True)
    Return_date = models.DateField(blank=True, null=True)



    def __str__(self):
        return self.title