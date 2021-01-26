from rest_framework import serializers
# Project Profile Chapter 10
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

# Project Profile Chapter 10
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile # point to UserProfileModel
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True, # only use when create or update, don't retrieve
                'style': {'input_type': 'password'} # enter pw by stars
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
        
    # otherwise updating user_profile will save PW as plain text
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            # pop the pw from the fields
            # use set_password to use encrypt
            password = validated_data.pop('password')
            instance.set_password(password)

        # pass value to existing DRF
        return super().update(instance, validated_data)
