from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    pages = models.IntegerField(default=100)
    
    def is_classic(self):
        return self.published_year < 1980
    
    def is_long(self):
        return self.pages > 300
