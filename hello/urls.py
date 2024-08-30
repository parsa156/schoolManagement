from django.urls import path
from . import views
urlpatterns = [
    path('parsa/',views.hello_world)
]
