from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home,name='home'),   #for first page or home page | but slash kuduthapo varala
    path('donate/', views.donate, name='donate'),
    path('detail/', views.detail, name='news-detail'),
    path('news/', views.news, name='news'),
    path('donation_submit/', views.donation_submit, name='donation_submit'),
    path('con/', views.contacts, name='contacts'),
    path('signup/', views.volunteer_signup, name='volunteer_signup'),
    path('news-form/', views.news_form, name='news_form')
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)