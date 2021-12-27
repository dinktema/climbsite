"""climbsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.views import home, post, posts, add_post, post_o, add_user, posts_filter, team
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', post_o, name='post_o'),
    path('home/', home, name='home'),
    path('posts/', posts, name='posts'),
    path('posts/add/', add_post, name='add'),
    path('posts/<int:id>/', post, name='post'),
    path('posts/<str:id>/', post, name='post'),
    path('register/', add_user, name='register'),
    path('posts/filter_by/<str:post_type>/', posts_filter, name='posts_filter'),
    path('team/', team, name='team'),
]
urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)