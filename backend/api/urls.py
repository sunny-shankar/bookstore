from django.urls import path
from api.views import get_books, create_order

urlpatterns = [
    path("books", get_books, name="books"),
    path("order", create_order),
]
