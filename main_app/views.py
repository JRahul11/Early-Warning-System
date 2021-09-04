from django.shortcuts import render, redirect
from .models import ProfileModel
from .forms import NewHomePageForm
from datetime import datetime
from datetime import date
import requests


def profile(request):
    user = request.user
    if request.POST.get("uname") and request.POST.get("udob") and request.POST.get("gender") and request.POST.get("uphone"):
        name = request.POST.get("uname")
        dob = request.POST.get("udob")
        gender = request.POST.get("gender")
        phone = int(request.POST.get("uphone"))
        today = date.today()
        print(dob)
        print(type(dob))
        age = today.year - datetime.strptime(dob, '%Y-%m-%d').year
        profile = ProfileModel.objects.create(
            user=user, name=name, age=age, gender=gender, phone=phone)
        return redirect("profile")
    else:
        return render(request, "main_app/profile.html")

    # if request.method == 'POST':
    #     form = NewProfileForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         dob = form.cleaned_data['dob']
    #         gender = form.cleaned_data['gender']
    #         phone = form.cleaned_data['phone']
    #         today = date.today()
    #         age = today.year - dob.year - \
    #             ((today.month, today.day) < (dob.month, dob.day))
    #         profile = ProfileModel.objects.create(
    #             user=user, name=name, age=age, gender=gender, phone=phone)
    # else:
    #     form = NewProfileForm()
    # context = {
    #     'form': form
    # }
    # return render(request, "main_app/profile.html", context)


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


def meds(request):
    return render(request, 'main_app/meds.html')
