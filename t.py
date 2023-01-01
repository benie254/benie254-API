url(r'^technologies/all$',views.AllTechnologies.as_view(),name="all-technologies"),
url(r'^technologies/add/$',views.AddTechnology.as_view(),name="add-technology"),
url(r'^technology/details/(\d+)$',views.TechnologyDetails.as_view(),name="technology-details"),