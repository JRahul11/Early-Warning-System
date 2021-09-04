
from django.contrib import admin
from django.urls import path
from sawo_app.views import index, receive, logout
from main_app.views import profile, travelreport, mymeds, newmed, deletemed

urlpatterns = [
    path('admin/', admin.site.urls),
    # Sawo
    path("", index, name='index'),
    path("receive/", receive, name='receive'),
    path("logout/", logout, name="logout"),

    # Main
    path("profile/", profile, name='profile'),
    path("travelreport/", travelreport, name='travelreport'),
    path("mymeds/", mymeds, name='mymeds'),
    path("newmed/", newmed, name='newmed'),
    path("deletemed/<med_id>", deletemed, name='deletemed'),
]
