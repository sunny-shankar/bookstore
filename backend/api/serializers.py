from rest_framework import serializers
from books.models import Book
from order.models import Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "image", "price", "rating"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "books"]
        read_only_fields = ["order_id"]
