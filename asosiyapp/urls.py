from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('blog/', BlogView.as_view()),
    path('maqola/<int:son>/', MaqolaView.as_view()),
]