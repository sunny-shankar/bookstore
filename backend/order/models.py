from django.db import models
from core.models import BaseModel
from django.conf import settings
from uuid import uuid4


def generate_order_id():
    return f"{str(uuid4()).split('-')[-1]}"


class Order(BaseModel):
    books = models.ManyToManyField("books.Book")
    order_id = models.CharField(
        default=generate_order_id,
        max_length=150,
        null=False,
        blank=False,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True
    )

    def __str__(self) -> str:
        return self.order_id
