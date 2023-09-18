from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ClothesApp.models import Category, Brand, Product, Customer, Order, OrderItem, Contact, Feedback
from ClothesApp.serializers import CategorySerializers, BrandSerializers, ProductSerializers, CustomerSerializers, OrderSerializers, OrderItemSerializers, ContactSerializers, FeedbackSerializers

# CRUD Cate
@csrf_exempt
def categoryApi(request,id=0):
    if request.method == 'GET':
        category = Category.objects.all()
        category_serializer = CategorySerializers(category,many=True)
        return JsonResponse(category_serializer.data,safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializers(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(id=category_data['id'])
        category_serializer = CategorySerializers(category,data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse("Delete Successfully",safe=False)

# CRUD Brand
@csrf_exempt
def brandApi(request,id=0):
    if request.method == 'GET':
        brand = Brand.objects.all()
        brand_serializer = BrandSerializers(brand,many=True)
        return JsonResponse(brand_serializer.data,safe=False)
    elif request.method == 'POST':
        brand_data = JSONParser().parse(request)
        brand_serializer = BrandSerializers(data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        brand_data = JSONParser().parse(request)
        brand = Brand.objects.get(id=brand_data['id'])
        brand_serializer = BrandSerializers(brand,data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        brand = Brand.objects.get(id=id)
        brand.delete()
        return JsonResponse("Delete Successfully",safe=False)
    
# CRUD Prod 
@csrf_exempt
def productApi(request,id=0):
    if request.method == 'GET':
        product = Product.objects.all()
        product_serializer = ProductSerializers(product,many=True)
        return JsonResponse(product_serializer.data,safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializers(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(id=product_data['id'])
        product_serializer = ProductSerializers(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Delete Successfully",safe=False)

# CRUD Cus
@csrf_exempt
def customerApi(request,id=0):
    if request.method == 'GET':
        customer = Customer.objects.all()
        customer_serializer = CustomerSerializers(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializers(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer = Customer.objects.get(id=customer_data['id'])
        customer_serializer = CustomerSerializers(customer,data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        customer = Customer.objects.get(id=id)
        customer.delete()
        return JsonResponse("Delete Successfully",safe=False)
    
# CRUD Order
@csrf_exempt
def orderApi(request,id=0):
    if request.method == 'GET':
        order = Order.objects.all()
        order_serializer = OrderSerializers(order,many=True)
        return JsonResponse(order_serializer.data,safe=False)
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializers(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        order = Order.objects.get(id=order_data['id'])
        order_serializer = OrderSerializers(order,data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        order = Order.objects.get(id=id)
        order.delete()
        return JsonResponse("Delete Successfully",safe=False)

# CRUD OrderItem
@csrf_exempt
def orderitemApi(request,id=0):
    if request.method == 'GET':
        orderitem = OrderItem.objects.all()
        orderitem_serializer = OrderItemSerializers(orderitem,many=True)
        return JsonResponse(orderitem_serializer.data,safe=False)
    elif request.method == 'POST':
        orderitem_data = JSONParser().parse(request)
        orderitem_serializer = OrderItem(data=orderitem_data)
        if orderitem_serializer.is_valid():
            orderitem_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        orderitem_data = JSONParser().parse(request)
        orderitem = OrderItem.objects.get(id=orderitem_data['id'])
        orderitem_serializer = OrderItemSerializers(orderitem,data=orderitem_data)
        if orderitem_serializer.is_valid():
            orderitem_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        orderitem = OrderItem.objects.get(id=id)
        orderitem.delete()
        return JsonResponse("Delete Successfully",safe=False)

# CRUD Contact
@csrf_exempt
def contactApi(request,id=0):
    if request.method == 'GET':
        contact = Contact.objects.all()
        contact_serializer = ContactSerializers(contact,many=True)
        return JsonResponse(contact_serializer.data,safe=False)
    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializers(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact = Contact.objects.get(id=contact_data['id'])
        contact_serializer = ContactSerializers(contact,data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        contact = Contact.objects.get(id=id)
        contact.delete()
        return JsonResponse("Delete Successfully",safe=False)
    
# CRUD Feedback
@csrf_exempt
def feedbackApi(request,id=0):
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        feedback_serializer = FeedbackSerializers(feedback,many=True)
        return JsonResponse(feedback_serializer.data,safe=False)
    elif request.method == 'POST':
        feedback_data = JSONParser().parse(request)
        feedback_serializer = FeedbackSerializers(data=feedback_data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        feedback_data = JSONParser().parse(request)
        feedback = Feedback.objects.get(id=feedback_data['id'])
        feedback_serializer = FeedbackSerializers(feedback,data=feedback_data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        feedback = Feedback.objects.get(id=id)
        feedback.delete()
        return JsonResponse("Delete Successfully",safe=False)