from django.urls import path,re_path as url 
from benie_app import views 


urlpatterns = [
    url(r'^profiles/$',views.UserProfiles.as_view(),name="user-profiles"),
    url(r'^projects/all$',views.AllProjects.as_view(),name="all-projects"),
    url(r'^projects/add/$',views.AddProject.as_view(),name="add-project"),
    url(r'^project/details/(\d+)$',views.ProjectDetails.as_view(),name="user-profiles"),
]