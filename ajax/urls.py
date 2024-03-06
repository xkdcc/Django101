"""djangoprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from . import views

app_name = 'ajax'

# When defining URLs in Django, it's generally a good practice to include a trailing slash (/) 
# at the end of each path. 
# This convention aligns with Django’s design philosophy and how it handles HTTP requests. 
# That's why we should use "v1/" instead of "v1".
# APPEND_SLASH setting is set to True (which is the default). 
# If a user requests a URL without a trailing slash, 
# Django will perform an HTTP redirect to the same URL with a trailing slash if the corresponding pattern exists. 
# This behavior ensures URL normalization and helps avoid duplicate content issues,
# which can affect SEO rankings.
urlpatterns = [
    path('', views.home, name='home'),
    path('demo_ajax_v1_addition/', views.demo_ajax_v1_addition, name='demo_ajax_v1_addition'),
    path('demo_ajax_v2_addition/', views.demo_ajax_v2_addition, name='demo_ajax_v2_addition'),
    path('demo_ajax_v3_addition/', views.demo_ajax_v3_addition, name='demo_ajax_v3_addition'),
]
