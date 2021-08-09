from django.shortcuts import render

# Create your views here.
#first created post_list function 
from django.utils import timezone
from .models import Post
def post_list(request):
    # GT, LT, GTE, LTE indicates less than/greater than ...
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts': posts})
