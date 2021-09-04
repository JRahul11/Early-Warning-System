from django.shortcuts import render, redirect, get_object_or_404
from .models import ProfileModel, MedModel
from .forms import NewHomePageForm
from datetime import datetime
from datetime import date
import requests
from early_warning_system.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# import schedule
# import time


def profile(request):
    user = request.user
    if request.POST.get("uname") and request.POST.get("udob") and request.POST.get("gender") and request.POST.get("uphone"):
        name = request.POST.get("uname")
        dob = request.POST.get("udob")
        gender = request.POST.get("gender")
        phone = int(request.POST.get("uphone"))
        today = date.today()
        age = today.year - datetime.strptime(dob, '%Y-%m-%d').year
        profile = ProfileModel.objects.create(
            user=user, name=name, age=age, gender=gender, phone=phone)
        return redirect("newmed")
    else:
        return render(request, "main_app/profile.html")


def newmed(request):
    user = request.user
    profilecheck = ProfileModel.objects.filter(user=user)
    if not profilecheck.exists():
        return redirect("profile")
    if request.POST.get("pill_name") and request.POST.get("pill_time") and request.POST.get("pill_frequency"):
        pill_name = request.POST.get("pill_name")
        pill_time = request.POST.get("pill_time")
        pill_dosage = int(request.POST.get("dosage"))
        pill_frequency = request.POST.get("pill_frequency")
        pill = MedModel.objects.create(
            user=user, pill_name=pill_name, pill_time=pill_time,pill_dosage=pill_dosage, pill_frequency=pill_frequency)
        return redirect("newmed")
    else:
        return render(request, "main_app/newmed.html")


def mymeds(request):
    user = request.user
    empty = False
    mymeds = MedModel.objects.filter(user=user)
    if not mymeds.exists():
        empty = True
    context = {
        'mymeds': mymeds,
        'empty': empty,
    }
    return render(request, 'main_app/mymeds.html', context)


def deletemed(request, med_id):
    user = request.user
    meds = get_object_or_404(MedModel, user=user, id=med_id)
    meds.delete()
    return redirect('mymeds')


def travelreport(request):
    if request.method == 'POST':
        loc = request.POST.get("city")
        date = request.POST.get("date")
        try:
            # Latitude and Longitude api
            parameters = {
                "key": "4oCcZopsrIq16HniXX8hKFiAZfJPb6mv",
                "location": loc
            }
            response = requests.get(
                "http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
            data = response.json()
            d1 = data['results'][0]
            d2 = d1['locations'][0]
            lat = d2['latLng']['lat']
            lng = d2['latLng']['lng']

            # Weather Api
            a1 = "http://api.openweathermap.org/data/2.5/forecast?"
            a2 = "lat=" + str(lat) + "&lon=" + str(lng)
            a3 = "&appid=c6e315d09197cec231495138183954bd"
            wa = a1 + a2 + a3
            response = requests.get(wa)
            data = response.json()
            d = data['list']
            res = [sub['main'] for sub in d]
            temp = [t['temp'] for t in res]
            hum = [t['humidity'] for t in res]
            mini = [t['temp_min'] for t in res]
            maxim = [t['temp_max'] for t in res]
            time = [sub['dt_txt'] for sub in d]
            degree_sign = u"\N{DEGREE SIGN}" + "C"
            weather = [sub['weather'] for sub in d]
            wind = [sub['wind']for sub in d]
            windspeed = [sub['speed']for sub in wind]
            weatherm, weatherd, icon = [], [], []
            for i in range(len(temp)):
                for sub in weather[i]:
                    weatherm.append(sub['main'])
                    weatherd.append(sub['description'])

            # Aqi Api
            a11 = "http://api.openweathermap.org/data/2.5/air_pollution/forecast?"
            a22 = "lat=" + str(lat) + "&lon=" + str(lng)
            a33 = "&appid=c6e315d09197cec231495138183954bd"
            api_address1 = a11 + a22 + a33
            res = requests.get(api_address1)
            data1 = res.json()
            list2 = data1['list']
            res2 = [sub1['main'] for sub1 in list2]
            aqi = [a['aqi'] for a in res2]

        except Exception as e:
            context = {
                'errormsg': "Something went wrong"
            }
            print(e)
        context = {
            'time': time,
            'temp': temp,
            'mini': mini,
            'maxim': maxim,
            'hum': hum,
            'weatherm': weatherm,
            'weatherd': weatherd,
            'windspeed': windspeed,
            'aqi': aqi,
            'loc': loc
        }
        return render(request, 'main_app/report.html', context)

    form = NewHomePageForm()
    context = {
        "form": form
    }
    return render(request, 'main_app/home.html', context)
