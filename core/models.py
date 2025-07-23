from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def classic_books_count(self):
        """
        Retourne le nombre de livres 'classiques' de cet auteur,
        c'est-à-dire publiés avant 1980.
        """
        return self.books.filter(published_year__lt=1980).count()
        # Si tu n’as pas mis related_name, remplace self.books par self.book_set

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_year = models.IntegerField()
    pages = models.IntegerField(default=100)
    
    def is_classic(self):
        return self.published_year < 1980
    
    def is_long(self):
        return self.pages > 300
