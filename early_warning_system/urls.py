
from django.contrib import admin
from django.urls import path
from sawo_app.views import index, receive

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),
    path("receive/", receive, name='receive'),
]
