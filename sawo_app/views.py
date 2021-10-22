from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Config

# imported sawopy
from sawo import createTemplate, getContext, verifyToken
import json
from django.http import HttpResponse

load = ''
loaded = 0
un = ''

createTemplate("templates/partials")


def index(request):
    config = Config.objects.order_by('-api_key')[:1]
    setLoaded()
    setPayload(load if loaded < 2 else '')
    context = {"sawo": getContext(config, "receive/") if(config) else {},
               "load": load, "title": "Home"}
    if load:
        return redirect('travelreport')
    else:
        return render(request, "sawo_app/index.html", context)


def receive(request):
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        setLoaded(True)
        setPayload(payload)

        un = load['identifier']
        try:
            usr = User.objects.get(username=un)
        except User.DoesNotExist:
            usr = User.objects.create_user(username=un)
            usr.save()
        login(request, usr)

        status = 200 if verifyToken(payload) else 404
        response_data = {"status": status}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def setPayload(payload):
    global load
    load = payload


def setLoaded(reset=False):
    global loaded
    if reset:
        loaded = 0
    else:
        loaded += 1


def user_logout(request):
    logout(request)
    return redirect("index")
