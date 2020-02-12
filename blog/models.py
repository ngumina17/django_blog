from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    photo_url = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title
