from django.db import models

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

