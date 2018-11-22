from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField(max_length=50)
    author = models.CharField(max_length=25)
    vote = models.IntegerField(default=0)
    created_on = models.DateField(auto_now_add=True)

    class Meta: 
        db_table = 'ARTICLE'
        ordering = ['-vote']

    def __str__(self):
        return self.title