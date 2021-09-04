
from django.contrib import admin
from django.urls import path
from sawo_app.views import index, receive
from main_app.views import profile, travelreport, meds

urlpatterns = [
    path('admin/', admin.site.urls),
    # Sawo
    path("", index, name='index'),
    path("receive/", receive, name='receive'),

    # Main
    path("profile/", profile, name='profile'),
    path("travelreport/", travelreport, name='travelreport'),
    path("meds/", meds, name='meds')
]
