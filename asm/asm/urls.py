from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/anime/$', views.anime_list),
    path('api/anime/<slug:slug>', views.anime_detail),
    re_path(r'^api/series/$', views.series_list),
    path('api/series/<slug:slug>', views.series_detail),
    re_path(r'^api/movies/$', views.movies_list),
    path('api/movies/<slug:slug>', views.movies_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
