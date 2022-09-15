from django.urls import path,re_path as url 
from benie_app import views 


urlpatterns = [
    url(r'^profiles/$',views.UserProfiles.as_view(),name="user-profiles"),
]