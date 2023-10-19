from django.urls import path
from .views import *

urlpatterns = [path("emotions/", Emotions_data.as_view(), name="emotions_data")]
