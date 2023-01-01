from django.urls import path,re_path as url 
from benie_app import views 


urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^profiles/$',views.UserProfiles.as_view(),name="user-profiles"),
    url(r'^projects/all$',views.AllProjects.as_view(),name="all-projects"),
    url(r'^projects/add/$',views.AddProject.as_view(),name="add-project"),
    url(r'^project/details/(\d+)$',views.ProjectDetails.as_view(),name="user-profiles"),
    url(r'^reactions/all$',views.AllReactions.as_view(),name="all-reactions"),
    url(r'^reactions/add/$',views.AddReaction.as_view(),name="add-reaction"),
    url(r'^reaction/details/(\d+)$',views.ReactionDetails.as_view(),name="reaction-details"),
    url(r'^feedbacks/all$',views.AllFeedbacks.as_view(),name="all-feedbacks"),
    url(r'^feedbacks/add/$',views.AddFeedback.as_view(),name="add-feedback"),
    url(r'^feedback/details/(\d+)$',views.FeedbackDetails.as_view(),name="feedback-details"),
    url(r'^technologies/all$',views.AllTechnologies.as_view(),name="all-technologies"),
    url(r'^technologies/add/$',views.AddTechnology.as_view(),name="add-technology"),
    url(r'^technology/details/(\d+)$',views.TechnologyDetails.as_view(),name="technology-details"),
    url(r'^contacts/all$',views.AllContacts.as_view(),name="all-contacts"),
    url(r'^contact/details/(\d+)$',views.ContactDetails.as_view(),name="contact-details"),
]