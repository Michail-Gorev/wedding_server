from django.urls import path
from .views import save_guest

urlpatterns = [
    path('save/', save_guest, name='save_guest'),
]