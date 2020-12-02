from django.urls import path,include
from .views import pulse
urlpatterns = [
    path('api/<int:m_id>/<int:rdg>/',pulse,name="pulse")
]
