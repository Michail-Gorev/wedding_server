from django.contrib import admin
from django.urls import path, include

from guests.views import save_guest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save/', save_guest, name='save_guest'),
]