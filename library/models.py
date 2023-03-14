from django.db import models

# Create your models here.

class Category(models.Model):
    """Model representing a category"""
    name = models.CharField(max_length=200, help_text="Enter a Category for books and videos")

    def __str__(self):
        """String representation of the Model Object"""
        return self.name
    

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief summary of the book')
    cover_image = models.ImageField(upload_to='book_imgs', blank=True, null=True)
    copy = models.FileField(upload_to='books', blank=False)

    category = models.ManyToManyField(Category, help_text='Select category for this book')

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String representation of the Model Object"""
        return self.title
    

class Author(models.Model):
    """Model representing an Author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String representation of the Model Object"""
        return f'{self.last_name}, {self.first_name}'


class Video(models.Model):
    """Model representing a Video"""
    title = models.CharField(max_length=100)
    copy = models.FileField(upload_to='videos', blank=False)
    category = models.ManyToManyField(Category, help_text='Select category for this video')
    thumbnail = models.ImageField(upload_to='video_imgs', blank=True, null=True)

    def __str__(self):
        """String representation of the Model Object"""
        return self.title