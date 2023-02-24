from django.urls import path, include
from . import views


urlpatterns = [
    path('articles', views.ArticlesList.as_view()),
    path("articles/<slug:slug>", views.ArticlesDetail.as_view()),
    path("static_infos", views.StaticInfView.as_view()),
    path("translations", views.TranslationsView.as_view()),
    path('languages', views.LangsList.as_view()),
    path('partners', views.PartnersList.as_view()),
    path("add_aplication", views.NewAppliction.as_view()),
    path('services', views.ServicesList.as_view()),
    path("services/<slug:slug>", views.ServicesDetail.as_view()),
    path("reviews", views.ReviewsList.as_view()),
    path("projects", views.ProjectsList.as_view()),
    path('projects/<slug:slug>', views.ProjectsDetail.as_view())    
]
