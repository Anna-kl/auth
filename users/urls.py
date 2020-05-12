from django.urls import path
from .views import  CreateUserAPIView

app_name='articles'

urlpatterns=[
    path('login/', CreateUserAPIView.as_view()),
    # path('sample/', sample)
]