# home/urls.py
from django.urls import include,path
from .views import login
from .views import dashboard
from django.contrib import admin
from . import views
from .views import available_slot
from .views import feedback
from .views import find_spot
from .views import find_spot_result
from django.contrib.auth import views as auth_views
from .views import book_slot
from .views import end
from .views import submit_feedback

urlpatterns = [
    path('', login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('feedback/', views.feedback, name='feedback'),
    path('find_spot/', views.find_spot, name='find_spot'),
    path('find_spot_result/', views.find_spot_result, name='find_spot_result'),
    path('book_slot/', book_slot, name='book_slot'),
    path('available_slot/', available_slot, name='available_slot'),
    path('end/', end, name='end'),
    path('submit_feedback/', submit_feedback, name='submit_feedback')
]


