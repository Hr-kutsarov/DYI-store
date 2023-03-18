from django.core import exceptions
from django.contrib.auth import password_validation
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

    # to use hashing for the password
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user
    
    def validate(self, data):
        user = UserModel(**data)
        password = data.get('password')
        errors = {}
        try:
            password_validation.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)
    
    # will only return the username
    def to_representation(self, instance):
        user_repr = super().to_representation(instance)
        user_repr.pop('password')
        return user_repr