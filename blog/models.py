#from django.db import models
#above line was previously present here still added for extra 
# Create your models here.

#The following code is entered by me

from django.conf import settings #imports settings from configuration
from django.db import models #models are similar to database
from django.utils import timezone #imports timezone from utilitys


class Post(models.Model):
    #A AUTH_USER_MODEL will delay the retrieval of the actual model class until all apps are loaded.
    # The on_delete=models. CASCADE tells Django to cascade the deleting effect i.e. continue deleting the dependent models as well.
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    #On next line field is blank so you you have to allow it to be null
    published_date=models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title
'''class Post(models.Model): – this line defines our model (it is an object).


class is a special keyword that indicates that we are defining an object.
Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
Now we define the properties we were talking about: title, text, created_date, published_date and author. To do that we need to define the type of each field (Is it text? A number? A date? A relation to another object, like a User?)

models.CharField – this is how you define text with a limited number of characters.
models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
models.DateTimeField – this is a date and time.
models.ForeignKey – this is a link to another model.
We will not explain every bit of code here since it would take too much time. You should take a look at Django's documentation if you want to know more about Model fields and how to define things other than those described above (https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types).

What about def publish(self):? This is exactly the publish method we were talking about before. def means that this is a function/method and publish is the name of the method. You can change the name of the method if you want. The naming rule is that we use lowercase and underscores instead of spaces. For example, a method that calculates average price could be called calculate_average_price.

Methods often return something. There is an example of that in the __str__ method. In this scenario, when we call __str__() we will get a text (string) with a Post title.

Also notice that both def publish(self): and def __str__(self): are indented inside our class. Because Python is sensitive to whitespace, we need to indent our methods inside the class. Otherwise, the methods won't belong to the class, and you can get some unexpected behavior.

If something is still not clear about models, feel free to ask your coach! We know it is complicated, especially when you learn what objects and functions are at the same time. But hopefully it looks slightly less magic for you now!
'''
#you have to save everytime you edit in visual studio
#output of above code will be
'''
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post
'''