from rest_framework import serializers
from benie_app.models import Profile, Project, Technology, Reaction, Feedback, Contact

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('id','first_name','last_name','username','email','phone_number','resume','bio','intro','about_me','profile_photo')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('__all__')

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ('__all__')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('__all__')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')