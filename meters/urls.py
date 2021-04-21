from django.urls import path,include
from .views import pulse,charts




urlpatterns = [
    path('api/<int:m_id>/<int:rdg>/',pulse,name="pulse"),
    path('charts/<int:m_id>', charts, name="charts")
]
