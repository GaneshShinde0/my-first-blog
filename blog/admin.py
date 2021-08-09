from django.contrib import admin

# Register your models here.
from .models import Post#Post we created earlier(modified) in models.py file
admin.site.register(Post)#