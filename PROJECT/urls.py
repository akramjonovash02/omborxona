
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *
from statsApp.views import Stats
from userApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Bolimlar.as_view(), name='bolimlar'),
    path('main/', include('mainApp.urls')),
    path('stats/', include('statsApp.urls')),
    path('user/', include('userApp.urls')),
    path('login', LoginView.as_view())

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
