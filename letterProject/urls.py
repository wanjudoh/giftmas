from django.contrib import admin
from django.urls import path, include
import letter.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('letter.urls')),
]
