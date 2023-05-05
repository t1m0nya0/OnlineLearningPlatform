from django.db import models
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    is_free = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='photos/')
    favorites = models.BooleanField(default=False)
    cat = models.ForeignKey("Category", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

