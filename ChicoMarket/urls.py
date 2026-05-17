
from django.contrib import admin
from django.urls import include, path
from ChicoMarket import settings
from app1 import views as app1_views
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path('', app1_views.home),
    path('admin/', admin.site.urls),

    path('additem/', app1_views.additem),
    path('puppies/', app1_views.about),
    path('contact/', app1_views.contact),
    path('join/', app1_views.join),
    path('login/', app1_views.user_login),
    path('logout/', app1_views.user_logout),

    path("__reload__/", include("django_browser_reload.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)