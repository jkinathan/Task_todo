from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100) 
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be shown in admin dashboard
class TodoList(models.Model): 
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general",on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE) 
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called