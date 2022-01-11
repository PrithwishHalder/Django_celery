from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('async/', async_view),
    path('def/', default),
    path('class/', MyView.as_view()),
]
