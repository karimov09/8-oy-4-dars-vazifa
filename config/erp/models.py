from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator

class StudentApiView(models.Model):  
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(5),   
        MaxValueValidator(100)
    ])
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name 

class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='category_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='article_photos/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.article.title}"

class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='author_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
