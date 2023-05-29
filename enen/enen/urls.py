"""
URL configuration for enen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core.views import index
from core import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'assistances', views.AssistanceViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('contact', views.contact, name = "contact"),
    path('onlinehelp', views.onlinehelp, name = "onlinehelp"),
    path('requests', views.requests, name = "requests"),
    path('profile', views.profile, name = "profile"),
    path('update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('delete_profile_picture/', views.delete_profile_picture, name='delete_profile_picture'),
    path('about', views.about, name = "about"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.page_not_found'