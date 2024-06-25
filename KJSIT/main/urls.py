from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('medscan/', views.medscentry, name='medscentry'),
    path('medscan/result/', views.medscresults, name='medscentry_res'),
    path('medpred/', views.home, name='home'),
    path('login/', views.userlogin, name='login'),
    path('dashboard/', views.dashboard, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('signup/', views.handlesignup, name='signup'),
    path('about/', views.about, name='about'),
    path('medpred/contact/', views.contact, name='contact'),
    path('medpred/diabetes/', views.diabetes, name='diabetes'),
    path('medpred/heart-disease/', views.heart, name='heart-disease'),
    path('medpred/cancer/', views.Breast_cancer, name='cancer'),
    path('medpred/covid/', views.covid, name='covid'),
    path('medpred/diabetes-result/', views.diabetes_result, name='diabetes_result'),
    path('medpred/heart-disease-result/', views.heart_result, name='heart_result'),
    path('medpred/cancer-result/', views.cancer_result, name='cancer_result'),
    path('medpred/covid-result/', views.covid_result, name='covid_result'),
    path('personal_dashboard/', views.personal_dashboard, name='personal_dashboard'),   
    
    path('card_dashboard/', views.card_dashboard, name='card_dashboard'),
    
]