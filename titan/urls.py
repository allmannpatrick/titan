# urls.py
from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('result/', views.result,  name='result' ),

]
