from rest_framework import serializers
from ClothesApp.models import Category, Brand, Product, Customer, Order, OrderItem, Contact, Feedback

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name')

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model =Brand
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','name','description','price','category','image')

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','first_name','last_name','email','phone')

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('id','customer','products','total_price','date_ordered')

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=('id','product','order','quantity')

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'