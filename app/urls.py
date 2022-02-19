from django.urls import path
from .views import index
app_name="spline"
urlpatterns = [
    path('',index,name="index"),
]
