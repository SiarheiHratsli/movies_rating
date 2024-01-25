from django.db import models


class Articles(models.Model):
    title = models.CharField('nazwa', max_length=100)
    body = models.TextField('tresc')
    rating = models.IntegerField('rating', default=0)
    date = models.DateTimeField('data')
    review_type = models.IntegerField('review_type', default=0)
    img_route = models.CharField('img_route', max_length=200, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('article')
        verbose_name_plural = ('articles')