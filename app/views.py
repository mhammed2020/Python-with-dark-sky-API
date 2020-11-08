from django.shortcuts import render

# Create your views here.
from darksky import forecast
from datetime import datetime, timedelta
from datetime import date
key = 'cc3aae97f4aa5697aa47c5624a085e10'
def home(request) :
    # boston = 42.3601, -71.0589
    boston = 34.005143,-6.823645
    weekday = date.today()
    weekly_weather = {}
    with forecast('cc3aae97f4aa5697aa47c5624a085e10', *boston) as boston:
        print(boston.daily.summary)
        for day in boston.daily:
            day = dict(day = date.strftime(weekday, '%a'),
                    sum = day.summary,
                    tempMin = int((day.temperatureMin-32) *(5/9)),
                    tempMax = int ((day.temperatureMax-32) *(5/9))
                    )
            print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
            weekday += timedelta(days=1)

            #------------------------#
            pic = ''
            summary = ('{sum}'.format(**day).lower())

            if 'drizzle' in summary :
                pic ='rain.png'
            if 'rain' in summary :
                pic ='rain.png'
            if 'cloudy' in summary :
                pic ='clouds.png'

            
            if 'clear' in summary :
                pic ='sun.png'
            if 'party cloudy' in summary :
                pic ='rain.png'
            if 'drizzle' in summary :
                pic ='party-cloudy-day.png'
    hour = datetime.now().hour
    location = forecast('cc3aae97f4aa5697aa47c5624a085e10',34.005143,-6.823645)
    i= 0 

    while hour < 24 :
        temp = location.hourly[i].temperature

        if hour > 12 :
            print('{} pm - {}'.format(hour,temp))

        else :
            print('{} am - {}'.format(hour,temp))

        hour += 1
        i+=1






    return render(request,'home.html',{})