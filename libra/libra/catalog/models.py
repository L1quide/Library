from django.db import models
from django.urls import reverse
import uuid



class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='13312')
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='fsdfsd')
    isbn = models.CharField('ISBM', max_length=13, help_text='dsdf')
    genre = models.ManyToManyField(Genre, help_text='dfsdf')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='dfsbaa')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='ifd')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'(self.id) (self.book.title)'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        return f'(self.last_name) (self.first_name)'

# Create your models here.



