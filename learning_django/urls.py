"""learning_django URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from pages.views import education_view
from pages.views import achievement_view
from pages.views import index_view
from User.views import user_output_data_view
from User.views import user_input_data_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path("home/", home_view, name='home'),
    path("achievement/", achievement_view, name='achievement'),
    path("education/", education_view, name='education'),
    path("user/output/", user_output_data_view, name="user_output"),
    path("user/input/", user_input_data_view, name="user_input")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

