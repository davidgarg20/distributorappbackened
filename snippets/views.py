from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Payment , Order, Shop ,OrderDetail,DistributorDetail,SalesmanDetail
from snippets.serializers import PaymentSerializer , OrderSerializer  ,ShopSerializer ,OrderDetailSerializer ,DistributorDetailSerializer,SalesmanDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class DistributordetailList(generics.ListCreateAPIView):
    queryset=DistributorDetail.objects.all()
    serializer_class = DistributorDetailSerializer
    def get_queryset(self):
        queryset = DistributorDetail.objects.all()
        u = self.request.query_params.get('u',None)
        d = self.request.query_params.get('d',None)
        if u is not None:
            queryset = queryset.filter(dcontactno=u)
            return queryset
        if d is not None:
            queryset = DistributorDetail.objects.latest('distributorid')
            return queryset
        return queryset


class SalesmanDetailList(generics.ListCreateAPIView):
    queryset=SalesmanDetail.objects.all()
    serializer_class = SalesmanDetailSerializer
    def get_queryset(self):
        queryset = SalesmanDetail.objects.all()
        u = self.request.query_params.get('u',None)
        if u is not None:
            queryset = queryset.filter(contactno=u)
            return queryset
        return queryset



class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        s = self.request.query_params.get('shopname', None)
        d = self.request.query_params.get('distributorid', None)
        if s is not None:
            queryset = Payment.objects.filter(distributorid=d).filter(shopname=s)
            return queryset
        return queryset



class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        d = self.request.query_params.get('d', None)
        queryset = Order.objects.all()
        s = self.request.query_params.get('s', None)
        l = self.request.query_params.get('l', None)
        shop = self.request.query_params.get('shop',None)
        deli = self.request.query_params.get('del',None)
        last = Order.objects.count()
        if s is not None and shop is None and deli is None:
            if int(l) < Order.objects.filter(distributorid=d).count() :
                queryset = Order.objects.filter(distributorid=d).order_by('-orderno')[int(s):int(l)]
                return queryset
            queryset = Order.objects.filter(distributorid=d).order_by('-orderno')[int(s):last]
            return queryset
        if s is not None and shop is not None and deli is None:
            if int(l) < Order.objects.filter(distributorid=d).count() :
                queryset = Order.objects.filter(distributorid=d).filter(shopname=shop).order_by('-orderno')[int(s):int(l)]
                return queryset
            queryset = Order.objects.filter(distributorid=d).filter(shopname=shop).order_by('-orderno')[int(s):last]
            return queryset
        if s is None and shop is not None and deli is not None:
            if int(l) < Order.objects.filter(distributorid=d).filter(delstatus=False).count() :
                queryset = Order.objects.filter(distributorid=d).filter(shopname=shop).filter(delstatus=False).order_by('-orderno')[int(s):int(l)]
                return queryset
            queryset = Order.objects.filter(distributorid=d).filter(shopname=shop).filter(delstatus=False).order_by('-orderno')[int(s):last]
            return queryset
        if s is None and shop is None and deli is not None:
            queryset = Order.objects.filter(distributorid=d).filter(delstatus=False).order_by('-orderno')
            return queryset
        return queryset


class OrderDetailList(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        queryset=OrderDetail.objects.all()
        orderno = self.request.query_params.get('orderno',None)
        if orderno is not None:
            if orderno is "0":
                orderno1 = OrderDetail.objects.last().orderno
                return queryset.filter(orderno=orderno1)
            return queryset.filter(orderno=orderno)
        return queryset


class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        queryset=Shop.objects.all()
        shopname = self.request.query_params.get('shopname',None)
        distributorid= self.request.query_params.get('distributorid',None)
        if shopname is not None:
            queryset = queryset.filter(distributorid=distributorid).filter(shopname=shopname)
            return queryset
        if distributorid is not None and shopname is None:
            queryset = queryset.filter(distributorid=distributorid)
            return queryset
        return queryset




