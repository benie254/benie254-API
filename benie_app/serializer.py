from rest_framework import serializers
from benie_app.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('id','first_name','last_name','username','email','phone_number','resume','bio','intro','about_me','profile_photo')