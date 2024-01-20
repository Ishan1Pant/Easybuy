from rest_framework import serializers 
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth.models import User 
from .models import * 

class userSerializer(serializers.ModelSerializer):
    _id=serializers.SerializerMethodField(read_only=True)
    name=serializers.SerializerMethodField(read_only=True)
    is_admin=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User
        fields=['id','email','username','_id','name','is_admin']

    def get_id(self,obj):
        return obj.id
    
    def get_is_admin(self,obj):
        return obj.is_staff 
    
    def get_name(self,obj):
        name=obj.first_name
        if name=='':
            name=obj.email
        return name
    
class UserSerializerWithToken(userSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','email','username','_id','name','is_admin','token']
    
    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)
    
class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=reviews
        fields='__all__'

class productsSerailizer(serializers.ModelSerializer):
    reviews=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=products
        fields='__all__'
    def get_reviews(self,obj):
        reviews=obj.review_set.all()
        serailizer=reviewSerializer(reviews,many=True)
        return serailizer.data
    
class shippingSerializer(serializers.ModelSerializer):
    class Meta:
        model=shipping_address
        fields='__all__'

class order_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model=order_items
        fields='__all__'

class ordersSerializer(serializers.ModelSerializer):
    order_items=serializers.SerializerMethodField(read_only=True)
    shipping_address=serializers.SerializerMethodField(read_only=True)
    user=serializers.SerializerMethodField(read_only=False)
    class Meta:
        model=orders
        fields='__all__'

    def get_order_items(self,obj):
        items=obj.order_items.all()
        serializer=order_itemSerializer(items,many=True)
        return serializer.data
    
    def get_shipping_address(self,obj):
        try:
            address=shippingSerializer(obj.shipping_address,many=False).data
        except:
            address=False
        return address
    
    def get_user(self,obj):
        item=obj.user
        serializer=userSerializer(item,many=False)
        return serializer



