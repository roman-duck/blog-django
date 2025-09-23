from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': {'posts': PostSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
    path('__debug__/', include('debug_toolbar.urls')),
]
