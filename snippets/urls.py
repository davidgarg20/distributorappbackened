from django.urls import path
from snippets import views
from snippets.views import *

urlpatterns = [
    path('payment/', PaymentList.as_view()),
    path('order/', OrderList.as_view()),
    path('orderdetail/', OrderDetailList.as_view()),
    path('shop/', ShopList.as_view()),
    path('distributor/',DistributordetailList.as_view()),
    path('salesman/',SalesmanDetailList.as_view()),
]