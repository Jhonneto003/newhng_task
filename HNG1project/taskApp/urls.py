from django.urls import path
from .views import TaskView

urlpatterns=[
    path('api/hello',TaskView.as_view(), name='response')
]