from django.shortcuts import render
from .models import Book
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts=Book.objects.filter(Isuued_date__lte=timezone.now()).order_by('Isuued_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
