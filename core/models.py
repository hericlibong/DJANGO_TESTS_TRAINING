from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.IntegerField()
    pages = models.IntegerField(default=100)
    
    def is_classic(self):
        return self.published_year < 1980
    
    def is_long(self):
        return self.pages > 300
