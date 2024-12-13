from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=100, default='')
    weight = models.FloatField(default=0.0)
    image = models.ImageField(blank=True, upload_to='images', default='/static/images/phone.jpg')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return '/static/images/phone.jpg'

