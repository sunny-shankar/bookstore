from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from books.models import Book
from order.models import Order
from api.serializers import BookSerializer, OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED


@api_view(["GET"])
def get_books(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            obj = serializer.save()
            return {"id": obj.id}
    obj = Book.objects.all().order_by("-created_at")
    serializer = BookSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        order = serializer.save()
        order.user = request.user
        order.save()
    return Response(serializer.data, status=HTTP_201_CREATED)
