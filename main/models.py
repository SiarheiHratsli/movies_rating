from django.db import models


class Articles(models.Model):
    title = models.CharField('nazwa', max_length=100, default='')
    name = models.CharField('name', max_length=50, default='')
    body = models.TextField('tresc', default='')
    rating = models.IntegerField('rating', default='')
    date = models.DateTimeField('data', default='')
    review_type = models.IntegerField('review_type', default='')
    img_route = models.CharField('img_route', max_length=200, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('article')
        verbose_name_plural = ('articles')