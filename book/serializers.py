from rest_framework import serializers 
from .models import Book,User

#Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start with R')

class BookSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    desc=serializers.CharField(max_length=100)
    author=serializers.CharField(max_length=100)
    price=serializers.FloatField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
       
        instance.name=validated_data.get('name',instance.name)
        instance.desc=validated_data.get('desc',instance.desc)
        instance.author=validated_data.get('author',instance.author)
        instance.price=validated_data.get('price',instance.price)
        instance.save()
        return instance
        
    

    #Field Level Validation
    def validate_price(self, value):
        if value >=1000:
            raise serializers.ValidationError('High Price')
        return value 
    #Object  level Validation

    def validate(self,data):
        nm = data.get('name')
        au = data.get('author')
        if nm.lower() =='godan' and au.lower() !='premchand':
            raise serializers.ValidationError('Author must be Premchand')
        return data

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields=['email','name','tc','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

#validating Password and confirmPassword
    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password And Confirm Password doesn't match")
        return super().validate(attrs)
    
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email =serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields=['email','password']
