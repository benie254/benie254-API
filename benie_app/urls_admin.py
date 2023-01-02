from django.urls import path,re_path as url 
from benie_app import views 

urlpatterns = [
    url(r'^projects/add/$',views.AddProject.as_view(),name="add-project"),
    url(r'^project/update/(\d+)$',views.UpdateProject.as_view(),name="edit-project"),
    url(r'^reactions/all/$',views.AllReactions.as_view(),name="all-reactions"),
    url(r'^reaction/details/(\d+)$',views.ReactionDetails.as_view(),name="reaction-details"),
    url(r'^feedbacks/all/$',views.AllFeedbacks.as_view(),name="all-feedbacks"),
    url(r'^feedback/details/(\d+)$',views.FeedbackDetails.as_view(),name="feedback-details"),
    url(r'^technologies/all/$',views.AllTechnologies.as_view(),name="all-technologies"),
    url(r'^technology/details/(\d+)$',views.TechnologyDetails.as_view(),name="technology-details"),
    url(r'^features/all/$',views.AllFeatures.as_view(),name="all-features"),
    url(r'^feature/details/(\d+)$',views.FeatureDetails.as_view(),name="feature-details"),
    url(r'^contacts/all/$',views.AllContacts.as_view(),name="all-contacts"),
    url(r'^contact/details/(\d+)$',views.ContactDetails.as_view(),name="contact-details"),
]