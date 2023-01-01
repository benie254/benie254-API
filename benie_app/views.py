from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import permission_classes 
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from benie_app.models import MyUser, Profile, Project, Technology, Feedback, Reaction, Contact
from benie_app.serializer import ProfileSerializer, ProjectSerializer, TechnologySerializer, FeedbackSerializer, ReactionSerializer, ContactSerializer

from django.shortcuts import render
from django.template.loader import render_to_string

import sendgrid
from sendgrid.helpers.mail import * 
from decouple import config 


# Create your views here.
def landing(request):
    return render(request,'landing.html',{})
  
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

@permission_classes([AllowAny,])
class AllProjects(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects,many=True)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class AddProject(APIView):
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

@permission_classes([AllowAny,])
class ProjectDetails(APIView):    
    def get(self, request, id, format=None):
        project = Project.objects.all().filter(pk=id).last()
        serializers = ProjectSerializer(project,many=False)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class UpdateProject(APIView):
    def put(self, request, id, format=None):
        project = Project.objects.all().filter(pk=id).last()
        serializers = ProjectSerializer(project,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, id, format=None):
        project = Project.objects.all().filter(pk=id).last()
        project.delete()
        return Response(status=status.HTTP_200_OK) 

@permission_classes([AllowAny,])
class AllTechnologies(APIView):
    def get(self, request, format=None):
        technologies = Technology.objects.all()
        serializers = TechnologySerializer(technologies,many=True)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class AddTechnology(APIView):
    def post(self, request, format=None):
        serializers = TechnologySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

@permission_classes([AllowAny,])
class TechnologyDetails(APIView):    
    def get(self, request, id, format=None):
        technology = Technology.objects.all().filter(pk=id).last()
        serializers = TechnologySerializer(technology,many=False)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class UpdateTechnology(APIView):
    def put(self, request, id, format=None):
        technology = Technology.objects.all().filter(pk=id).last()
        serializers = TechnologySerializer(technology,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, id, format=None):
        technology = Technology.objects.all().filter(pk=id).last()
        technology.delete()
        return Response(status=status.HTTP_200_OK) 

@permission_classes([AllowAny,])
class AllFeedbacks(APIView):
    def get(self, request, format=None):
        feedbacks = Feedback.objects.all()
        serializers = FeedbackSerializer(feedbacks,many=True)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class AddFeedback(APIView):
    def post(self, request, format=None):
        serializers = FeedbackSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

@permission_classes([AllowAny,])
class FeedbackDetails(APIView):    
    def get(self, request, id, format=None):
        feedback = Feedback.objects.all().filter(pk=id).last()
        serializers = FeedbackSerializer(feedback,many=False)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class UpdateFeedback(APIView):
    def put(self, request, id, format=None):
        feedback = Feedback.objects.all().filter(pk=id).last()
        serializers = FeedbackSerializer(feedback,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, id, format=None):
        feedback = Feedback.objects.all().filter(pk=id).last()
        feedback.delete()
        return Response(status=status.HTTP_200_OK) 

@permission_classes([AllowAny,])
class AllReactions(APIView):
    def get(self, request, format=None):
        reactions = Reaction.objects.all()
        serializers = ReactionSerializer(reactions,many=True)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class AddReaction(APIView):
    def post(self, request, format=None):
        serializers = ReactionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

@permission_classes([AllowAny,])
class ReactionDetails(APIView):    
    def get(self, request, id, format=None):
        reaction = Reaction.objects.all().filter(pk=id).last()
        serializers = ReactionSerializer(reaction,many=False)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class UpdateReaction(APIView):
    def put(self, request, id, format=None):
        reaction = Reaction.objects.all().filter(pk=id).last()
        serializers = ReactionSerializer(reaction,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, id, format=None):
        reaction = Reaction.objects.all().filter(pk=id).last()
        reaction.delete()
        return Response(status=status.HTTP_200_OK) 

@permission_classes([AllowAny,])
class AllContacts(APIView):
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializers = ContactSerializer(contacts,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ContactSerializer(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data['name']
            email = serializers.validated_data['email']
            message = serializers.validated_data['message']
            serializers.save()
            sg = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_API_KEY'))
            msg = render_to_string('email/new-contact.html', {
                'name': name,
                'email': email,
                "message": message,
            })
            message = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = 'beniewrites@gmail.com',
                subject = "New Contact",
                html_content= msg
            )
            try:
                sendgrid_client = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sendgrid_client.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)

            msg2 = render_to_string('email/message-delivered.html', {
                'name': name,
            })
            message2 = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = email,
                subject = "Message Delivered",
                html_content= msg2
            )
            try:
                sendgrid_client = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sendgrid_client.send(message2)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)
            status_code = status.HTTP_201_CREATED
            response = {
                'success' : 'True',
                'status code' : status_code,
                }
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

@permission_classes([AllowAny,])
class ContactDetails(APIView):    
    def get(self, request, id, format=None):
        contact = Contact.objects.all().filter(pk=id).last()
        serializers = ContactSerializer(contact,many=False)
        return Response(serializers.data)

@permission_classes([AllowAny,])
# @permission_classes([IsAdminUser,])
class UpdateContact(APIView):
    def put(self, request, id, format=None):
        contact = Contact.objects.all().filter(pk=id).last()
        serializers = ContactSerializer(contact,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, id, format=None):
        contact = Contact.objects.all().filter(pk=id).last()
        contact.delete()
        return Response(status=status.HTTP_200_OK) 
    