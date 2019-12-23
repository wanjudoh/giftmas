from django.contrib import admin
from django.conf.urls.static import static 
from django.conf import settings
from django.urls import path, include
import letter.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('letter.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
