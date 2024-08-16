from django.contrib import admin
from django.urls import path

from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^courses/', include('courses.urls')),
    path(r'^', include('accounts.urls')),
    path(r'^suggest/$', views.suggestion_view, name='suggestion'),
    path(r'^$', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)