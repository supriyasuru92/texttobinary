from django.urls import path  
from .views import *


urlpatterns = [  
    path('model_form_upload/', model_form_upload, name = 'model_form_upload'),  
    
]  