from rest_framework import serializers
from benie_app.models import MyInfo, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('id','first_name','last_name','username','email','phone_number',)


class MyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInfo
        fields = ('resume','bio','intro','about_me','profile_photo',)