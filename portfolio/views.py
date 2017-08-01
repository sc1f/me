from django.shortcuts import render
from .models import UserMeta, Category, Post
# Create your views here.
def homepage(request):
    user = UserMeta.objects.get(id=1)
    ctx = {
        "user": user
    }
    return render(request, 'index.html', context=ctx)

def category(request):
    return render(request, 'category.html')

def post(request):
    return render(request, 'post.html')