from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, \
    ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    prod = Product.objects.all()
    ser = ProductListSerializer(prod, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(pk=product_id)
            ser = ProductDetailsSerializer(product, many=False)
            return Response(ser.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')
        # try:
        #     prod = Product.objects.get(id=product_id)
        #     # review = Review.objects.all()
        #     ser = ProductDetailsSerializer(prod)
        #     # ser_rev = ReviewSerializer(review)
        #     # data = {'ser': ser.data, 'ser_rev': ser_rev.data}
        #     return Response(ser.data)
        # except Product.DoesNotExist:
        #     raise Http404()


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару
        с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
