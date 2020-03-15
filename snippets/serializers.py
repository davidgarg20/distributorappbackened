from rest_framework import serializers
from snippets.models import Payment,Order,Shop,OrderDetail ,DistributorDetail,SalesmanDetail
from django.core.validators  import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{10}$', message="Not a valid Phone Number")

class DistributorDetailSerializer(serializers.ModelSerializer):
    distributorid = serializers.IntegerField()
    ownername = serializers.CharField(max_length=100)
    firmname = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    dcontactno = serializers.CharField(max_length=100,validators=[phone_regex])
    password = serializers.CharField(max_length=100)
    class Meta:
        model = DistributorDetail
        fields = ['distributorid','ownername','firmname','address','dcontactno','password']
        def validate_contactno(self,dcontactno):
            if DistributorDetail.objects.filter(contactno=dcontactno).count()!=0:
                raise serializers.ValidationError("Distributor Already Exists")
            return dcontactno

    def create(self, validated_data, **kwargs):
        if DistributorDetail.objects.count() != 0:
            validated_data['distributorid']=DistributorDetail.objects.last().distributorid+1
        else:
            validated_data['distributorid'] = 1
        return DistributorDetail.objects.create(**validated_data)


class SalesmanDetailSerializer(serializers.ModelSerializer):
    salesmanid = serializers.IntegerField()
    distributorid = serializers.CharField(max_length=100)
    salesmanname = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    contactno = serializers.CharField(max_length=100,validators=[phone_regex])
    password = serializers.CharField(max_length=100)
    class Meta:
        model = SalesmanDetail
        fields = ['salesmanid','distributorid','salesmanname','address','contactno','password']
        def validate_contactno(self,contactno):
            if SalesmanDetail.objects.filter(contactno=contactno).count()!=0:
                raise serializers.ValidationError("Distributor Already Exists")
            return contactno
    def create(self, validated_data, **kwargs):
        if SalesmanDetail.objects.count() != 0:
            validated_data['salesmanid']= SalesmanDetail.objects.last().salesmanid+1
        else:
            validated_data['salesmanid'] = 1
        return SalesmanDetail.objects.create(**validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    distributorid =serializers.CharField(max_length=100)
    salesman = serializers.CharField(max_length=100)
    shop = serializers.CharField(max_length=100)
    shopname = serializers.CharField(max_length=100)
    payment = serializers.IntegerField(required=False)
    paymentdate = serializers.CharField(max_length=100,required=False)
    orderamount = serializers.IntegerField(required=False)
    orderdate = serializers.CharField(max_length=100,required=False)
    class Meta:
        model = Payment
        fields = ['distributorid','salesman', 'shop',  'shopname', 'payment', 'paymentdate','orderamount','orderdate']
    def create(self, validated_data):
        validated_data['shop'] = Shop.objects.get(shopname=validated_data['shopname']).shop
        obj = Shop.objects.filter(distributorid=validated_data['distributorid']).get(shopname=validated_data['shopname'])
        if validated_data['payment'] == 0 :
            obj.pendingbalance = obj.pendingbalance + validated_data['orderamount']
        else:
            obj.pendingbalance = obj.pendingbalance - validated_data['payment']
        obj.save()
        return Payment.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    distributorid = serializers.CharField(max_length=100)
    salesman = serializers.CharField(max_length=100,required=False)
    shop = serializers.CharField(max_length=100,required=False)
    orderno = serializers.IntegerField()
    shopname = serializers.CharField(max_length=100,required=False)
    orderdate = serializers.CharField(max_length=100,required=False)
    orderamount = serializers.CharField(max_length=100,required=False)
    delstatus = serializers.BooleanField(default=False,required=False)
    deldate = serializers.CharField(required=False)
    delsalesman = serializers.CharField(required=False)
    class Meta:
        model = Order
        fields = ['distributorid','salesman','shop','orderno','shopname','orderdate','orderamount','delstatus','deldate','delsalesman']
    def create(self, validated_data, **kwargs):
        if Order.objects.filter(distributorid=validated_data['distributorid']).filter(orderno=validated_data['orderno']).count()==1 :
            obj = obj = Order.objects.filter(distributorid=validated_data['distributorid']).get(orderno=validated_data['orderno'])
            obj.delstatus = True
            obj.deldate = validated_data['deldate']
            obj.delsalesman = validated_data['delsalesman']
            obj.save()
        else:
            if Order.objects.filter(distributorid=validated_data['distributorid']).count() != 0:
                validated_data['orderno'] = Order.objects.filter(
                    distributorid=validated_data['distributorid']).last().orderno + 1
            else:
                validated_data['orderno'] = 1
            validated_data['shop'] = Shop.objects.get(shopname=validated_data['shopname']).shop
            return Order.objects.create(**validated_data)



    def updatedel(self,validated_data):
        obj = obj = Shop.objects.filter(distributorid=validated_data['distributorid']).get(shopname=validated_data['shopname'])
        obj.delstatus = True
        obj.deldate = validated_data['deldate']
        obj.delsalesman = validated_data['delsalesman']
        obj.save()


class OrderDetailSerializer(serializers.ModelSerializer):
    distributorid = serializers.CharField(max_length=100)
    salesman = serializers.CharField(max_length=100)
    shop = serializers.CharField(max_length=100)
    orderno = serializers.IntegerField()
    shopname = serializers.CharField(max_length=100)
    item = serializers.CharField(max_length=100)
    qty = serializers.CharField(max_length=100)
    price = serializers.CharField(max_length=100)
    amount = serializers.CharField(max_length=100)
    class Meta:
        model = OrderDetail
        fields = ['distributorid','salesman', 'shop', 'orderno', 'shopname', 'item', 'qty','price','amount']
    def create(self, validated_data, **kwargs):
        if OrderDetail.objects.filter(distributorid=validated_data['distributorid']).count() != 0:
            validated_data['orderno']= Order.objects.filter(distributorid=validated_data['distributorid']).last().orderno
        else:
            validated_data['orderno'] = 1
        validated_data['shop'] = Shop.objects.get(shopname=validated_data['shopname']).shop
        return OrderDetail.objects.create(**validated_data)




class ShopSerializer(serializers.ModelSerializer):
    distributorid = serializers.CharField(max_length=100)
    shop = serializers.IntegerField()
    shopname = serializers.CharField(max_length=100)
    ownersname = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    contactno = serializers.CharField(max_length=100, validators=[phone_regex])
    pendingbalance = serializers.IntegerField(required=False)
    class Meta:
        model = Shop
        fields = ['distributorid','shop', 'shopname', 'ownersname', 'address', 'contactno','pendingbalance']

    def validate_shopname(self,shopname):
        if Shop.objects.filter(shopname=shopname).count()!=0:
            raise serializers.ValidationError("Shop Already Exists")
        return shopname


    def create(self, validated_data, **kwargs):
        if Shop.objects.count() != 0:
            validated_data['shop']= Shop.objects.last().shop+1
        else:
            validated_data['shop'] = 1
        return Shop.objects.create(**validated_data)




