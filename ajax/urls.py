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
urlpatterns = [
    path('', views.home, name='home'),
    path('demo_ajax_v1_addition', views.demo_ajax_v1_addition, name='demo_ajax_v1_addition'),
    path('demo_ajax_v2_addition', views.demo_ajax_v2_addition, name='demo_ajax_v2_addition'),
    path('demo_ajax_v3_addition', views.demo_ajax_v3_addition, name='demo_ajax_v3_addition'),
]
