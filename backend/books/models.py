from django.db import models
from core.models import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.URLField()
    price = models.FloatField()
    rating = models.FloatField()

    def __str__(self):
        return self.title
