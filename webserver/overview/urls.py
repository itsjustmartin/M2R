from django.urls import path ,include
from overview import views

urlpatterns = [
    path('',views.mainoverview,name='overview')

]