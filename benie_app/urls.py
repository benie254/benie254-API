from django.urls import path,re_path as url 
from benie_app import views 

urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^profiles/$',views.UserProfiles.as_view(),name="user-profiles"),
    url(r'^projects/all/$',views.AllProjects.as_view(),name="all-projects"),
    url(r'^project/details/(\d+)$',views.ProjectDetails.as_view(),name="user-details"),
    url(r'^project/reactions/$',views.ProjectReactions.as_view(),name="project-reactions"),
    url(r'^project/feedbacks/$',views.ProjectFeedbacks.as_view(),name="project-feedbacks"),
    url(r'^project/technologies/$',views.ProjectTechnologies.as_view(),name="project-technologies"),
]