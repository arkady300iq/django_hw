from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    class Meta:
        ordering = ["author"]
        unique_together = ["isbn"]