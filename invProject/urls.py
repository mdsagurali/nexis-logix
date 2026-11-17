
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authApp import views as auth_views

urlpatterns = [
    path('', auth_views.login_view, name='login'),

    path('admin/', admin.site.urls),

    path('inv/', include('invApp.urls')),

    path('auth/', include('authApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
