
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from sawo_app.views import index, receive, logout
from main_app.views import profile, travelreport, mymeds, newmed, deletemed
=======
from sawo_app.views import index, receive
from main_app.views import pills, profile, travelreport
>>>>>>> f38bf5ea40ee1567db5d7ed43e44a2f9805387a0

urlpatterns = [
    path('admin/', admin.site.urls),
    # Sawo
    path("", index, name='index'),
    path("receive/", receive, name='receive'),
    path("logout/", logout, name="logout"),

    # Main
    path("profile/", profile, name='profile'),
    path("travelreport/", travelreport, name='travelreport'),
<<<<<<< HEAD
    path("mymeds/", mymeds, name='mymeds'),
    path("newmed/", newmed, name='newmed'),
    path("deletemed/<med_id>", deletemed, name='deletemed'),
=======
    path("medication/", pills, name='pills'),
>>>>>>> f38bf5ea40ee1567db5d7ed43e44a2f9805387a0
]
