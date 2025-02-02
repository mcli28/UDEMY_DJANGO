from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    #Paths del core
    path('', include('core.urls')),
    #Paths de service
    path('services/', include('services.urls')),
    #Paths de blog
    path('blog/', include('blog.urls')),
    #Paths de page
    path('page/', include('pages.urls')),
    #Paths de contact
    path('contact/', include('contact.urls')),
    #Paths de admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom titles for admin
admin.site.site_header = "La caffetiera"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "La caffetiera"
