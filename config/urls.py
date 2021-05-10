from django.contrib import admin
from django.urls import path, include
from page.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('page/', include('page.urls')),
    path('', home, name='home'),
]
