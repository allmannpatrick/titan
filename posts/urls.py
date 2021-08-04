from django.urls import path
#from .views import CreatePostView
from . import views
urlpatterns = [
    path('fluff_result/', views.fluff_result,  name='fluff_result' ),
    #path('result/', CreatePostView.as_view(), name='result'),
]

