from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]