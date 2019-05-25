from django.urls import path
from . import views
urlpatterns = [
    path('api/customers/', views.LeadListCreate.as_view() ),
]