"""AppK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sport.urls')),
    path('api/', include('user.urls')),
    path('api/api-token-auth/',  obtain_jwt_token),
    #path('refresh-token-auth/',  refresh_jwt_token, name='refresh'),
    #path('verify-token-auth/',  verify_jwt_token, name='refresh')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
