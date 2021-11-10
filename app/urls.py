from django.urls import path
from app.views import ConvTemp


urlpatterns = [
    path('temp/',ConvTemp.as_view(),name='temp')
]
