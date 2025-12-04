from .models import User 
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','role', 'email', 'first_name', 'last_name', 'profile_image', 'password']
        read_only_fields = ['id']


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'password', 'password2']
        write_only_fields = ['password']
        read_only_fields = ['id']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields doesn't match"})
        
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            role=validated_data.get('role', 'GENERAL'),
            password=validated_data['password']
        )
        # user.set_password(validated_data['password'])
        # user.save()
        return user

