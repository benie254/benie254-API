from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from benie_app.models import MyUser, Profile
from benie_app.serializer import ProfileSerializer


# Create your views here.
class UserProfiles(APIView):
    def get_user_profiles(self):
        try:
            return Profile.objects.all()
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        user_profiles = Profile.objects.all()
        serializers = ProfileSerializer(user_profiles,many=True)
        return Response(serializers.data)
