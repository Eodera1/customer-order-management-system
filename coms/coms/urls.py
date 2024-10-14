from django.urls import path, include
from django.contrib import admin

# from coms.orders import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # Other URL patterns...
]