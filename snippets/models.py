from django.db import models

class DistributorDetail(models.Model):
    distributorid = models.IntegerField()
    ownername = models.CharField(max_length=100)
    firmname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dcontactno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class SalesmanDetail(models.Model):
    salesmanid = models.IntegerField()
    distributorid = models.CharField(max_length=100)
    salesmanname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contactno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Payment(models.Model):
    distributorid = models.CharField(max_length=100)
    salesman = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)
    shopname = models.CharField(max_length=100)
    payment = models.IntegerField(null=True)
    paymentdate = models.CharField(max_length=100,null=True)
    orderamount = models.IntegerField(null=True)
    orderdate = models.CharField(max_length=100,null=True)


class Order(models.Model):
    distributorid = models.CharField(max_length=100)
    salesman = models.CharField(max_length=100)
    shop = models.IntegerField()
    orderno = models.IntegerField()
    shopname = models.CharField(max_length=100)
    orderdate = models.CharField(max_length=100)
    orderamount = models.CharField(max_length=100)
    delstatus = models.BooleanField(default=False,null=True)
    deldate = models.CharField(max_length=100,null=True)
    delsalesman = models.CharField(max_length=100,null=True)


class OrderDetail(models.Model):
    distributorid = models.CharField(max_length=100)
    salesman = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)
    orderno = models.CharField(max_length=100)
    shopname = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

class Shop(models.Model):
    distributorid = models.CharField(max_length=100)
    shop = models.IntegerField()
    shopname = models.CharField(max_length=100)
    ownersname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contactno = models.CharField(max_length=100)
    pendingbalance = models.IntegerField(default=0,null=True)











