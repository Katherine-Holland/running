from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Includes home.urls at the root
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('blog/', include('blog.urls')),  
]