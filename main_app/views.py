from django.shortcuts import render
from .models import ProfileModel
from .forms import NewProfileForm, NewHomePageForm
from datetime import date
import requests


def profile(request):
    user = request.user
    if request.POST.get("name") and request.POST.get("dob") and request.POST.get("gender") and request.POST.get("phone"):
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        phone = int(request.POST.get("phone"))
        today = date.today()
        age = today.year - datetime.strptime(dob, '%d/%m/%y %H:%M:%S').year
        profile = ProfileModel.objects.create(
            user=user, name=name, age=age, gender=gender, phone=phone)
        return redirect("home")
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
        data_list = []
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
            print(d1)
            d2 = d1['locations'][0]
            print(d2)
            lat = d2['latLng']['lat']
            lng = d2['latLng']['lng']
            print(lat)
            print(lng)

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

            # Put all data in list
            data_list.append([time, temp, mini, maxim, hum,
                             weatherm, weatherd, windspeed, aqi])
            print(data_list)

        except Exception as e:
            context = {
                'errormsg': "Something went wrong"
            }
            print(e)
        context = {
            'data_list': data_list
        }
        return render(request, 'main_app/data.html', context)

    form = NewHomePageForm()
    context = {
        "form": form
    }
    return render(request, 'main_app/home.html', context)
