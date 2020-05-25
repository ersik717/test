from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Customer, Product, ProductForm, ProductStuff, ProductTopping, Baker, Order, Catalog, Review, ImageModel
import json
import datetime
from django.core.serializers.json import DjangoJSONEncoder
from passporteye import read_mrz

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

	@classmethod
	def get_token(cls, user):
		token = super(MyTokenObtainPairSerializer, cls).get_token(user)

		token['user_phone'] = user.user_phone
		token['user_address'] = user.user_address

		return token


class CustomUserSerializer(serializers.ModelSerializer):

	email = serializers.EmailField(
			required = True
		)
	username = serializers.CharField()
	password = serializers.CharField(min_length=8, write_only=True)

	class Meta:
		model = CustomUser
		fields = ('email', 'username', 'password')
		extra_kwargs = {'password':{'write_only': True}}

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance	

class UserListSerializer(serializers.ModelSerializer):
	# snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomerListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = '__all__'

class CustomerDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = '__all__'

class BakerListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Baker
		fields = '__all__'

class BakerDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductFormListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = ProductForm
		fields = '__all__' 

class ProductFormDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductForm
        fields = '__all__'

class ProductStuffListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = ProductStuff
		fields = '__all__' 

class ProductStuffDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductStuff
        fields = '__all__'

class ProductToppingListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = ProductTopping
		fields = '__all__' 

class ProductToppingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTopping
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Order
		fields = '__all__' 

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class CatalogListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Catalog
		fields = '__all__' 

class CatalogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Review
		fields = '__all__' 

class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ImageModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = ImageModel
		fields = ('imageUpload', 'name', 'surname')

	def create(self, validated_data):
		from passporteye import read_mrz
		img = validated_data['imageUpload']
		mrz = read_mrz(img.read(), save_roi=True)
		mrz_data = mrz.to_dict()
		print(mrz_data['names'])
		content = ImageModel(imageUpload=img, name=mrz_data['names'], surname=mrz_data['surname'])
		content.save()
		return content
