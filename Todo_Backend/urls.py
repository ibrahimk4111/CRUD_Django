from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('noteApi.urls')),
] 

urlpatterns += staticfiles_urlpatterns()
