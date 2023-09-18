from django.conf.urls import url
from ClothesApp import views

urlpatterns = [
    url(r'^category$',views.categoryApi),
    url(r'^category/([0-9]+)$',views.categoryApi),

    url(r'^brand$',views.brandApi),
    url(r'^brand/([0-9]+)$',views.brandApi),

    url(r'^product$',views.productApi),
    url(r'^product/([0-9]+)$',views.productApi),

    url(r'^customer$',views.customerApi),
    url(r'^customer/([0-9]+)$',views.customerApi),

    url(r'^order$',views.orderApi),
    url(r'^order/([0-9]+)$',views.orderApi),

    url(r'^orderitem$',views.orderitemApi),
    url(r'^orderitem/([0-9]+)$',views.orderitemApi),

    url(r'^contact$',views.contactApi),
    url(r'^contact/([0-9]+)$',views.contactApi),
    
    url(r'^feedback$',views.feedbackApi),
    url(r'^feedback/([0-9]+)$',views.feedbackApi),
]
