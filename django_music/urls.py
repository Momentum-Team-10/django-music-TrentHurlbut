"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from albums import views

urlpatterns = [
    path('', views.post_collection, name='post_collection'),
    path('album/add_album', views.add_album, name='add_album'),
    path('album/<int:pk>/', views.view_album, name='view_album'),
    path('album/<int:pk>/edit', views.edit_album, name='edit_album'),
    path('admin/', admin.site.urls),
]
