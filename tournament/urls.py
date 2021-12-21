"""tournament URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('part/', include('part.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from part import views as user_views

urlpatterns = [
    path('', user_views.CreatedListView.as_view(), name='home'),
    path('create/', user_views.CreatedListViewMore.as_view(), name='take-participate'),
    path('view_participated/', user_views.CreatedListViewMoreMore.as_view(), name='participated'),
    path('admin/', admin.site.urls),
    path('organizer/', user_views.organizer, name='organizer'),
    path('participate/', user_views.participate, name='participate'),
    path('organize/', user_views.organize.as_view(), name='organize'),
    path('view/', user_views.ParticipantListView.as_view(), name='participants'),
    path('organize/<int:pk>/',user_views.OrganizeDetailView.as_view(), name='organize-detail'),
    path('organize/<int:pk>/edit/',user_views.EditOrganize.as_view(), name='organize-edit'),
    path('organize/<int:pk>/delete/', user_views.DeleteOrganize.as_view(), name='organize-delete'),
    path('organize/<int:pk>/participate-team/',user_views.participatingTeam.as_view(), name='participate-team'),
    path('organize/<int:pk>/participate-player/',user_views.participatingPlayer.as_view(), name='participate-player'),
    path('register/', user_views.register, name='register'),
    path('contact_us/', user_views.ContactUs, name='contact_us'),    
    path('post/', user_views.Post, name='post'),    
    path('FAQ_and_Guide/', user_views.FaqAndGuide, name='faq'),    
    path('accounts/', user_views.accounts, name='accounts'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='part/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='part/home.html'), name='logout'),
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)