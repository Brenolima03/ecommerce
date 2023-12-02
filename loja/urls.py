from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Debug Toolbar URL
    path("__debug__/", include("debug_toolbar.urls")) if settings.DEBUG else None,

    # Admin URLs
    path('admin/', admin.site.urls),

    # Your other app URLs
    path('', include('produto.urls')),
    path('perfil/', include('perfil.urls')),
    path('pedido/', include('pedido.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Remover
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # ...
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
