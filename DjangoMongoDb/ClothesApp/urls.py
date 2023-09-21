from django.conf.urls import url
from django.urls import path
from .views import CateViewset, BrandViewset, ProdViewset, CusViewset, Orderiewset, OrderItemiewset, ContactViewset, FeedbackViewset

urlpatterns = [
    
    path('cate/', CateViewset.as_view()),
    path('cate/<int:id>', CateViewset.as_view()),

    path('brand/', BrandViewset.as_view()),
    path('brand/<int:id>', BrandViewset.as_view()),

    path('cate/', ProdViewset.as_view()),
    path('cate/<int:id>', ProdViewset.as_view()),

    path('cate/', CusViewset.as_view()),
    path('cate/<int:id>', CusViewset.as_view()),

    path('cate/', Orderiewset.as_view()),
    path('cate/<int:id>', Orderiewset.as_view()),

    path('cate/', OrderItemiewset.as_view()),
    path('cate/<int:id>', OrderItemiewset.as_view()),

    path('cate/', ContactViewset.as_view()),
    path('cate/<int:id>', ContactViewset.as_view()),

    path('cate/', FeedbackViewset.as_view()),
    path('cate/<int:id>', FeedbackViewset.as_view()),

]
