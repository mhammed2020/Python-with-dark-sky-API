from django.shortcuts import render

# Create your views here.
from darksky import forecast
from datetime import datetime, timedelta
from datetime import date
key = 'cc3aae97f4aa5697aa47c5624a085e10'
def home(request) :
    boston = 42.3601, -71.0589
    weekday = date.today()

    with forecast('cc3aae97f4aa5697aa47c5624a085e10', *boston) as boston:
        print("boston daily summary :")
        for day in boston.daily:
            day = dict(day = date.strftime(weekday, '%a'),
                    sum = day.summary,
                    tempMin = day.temperatureMin,
                    tempMax = day.temperatureMax
                    )
            print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
            weekday += timedelta(days=1)


    return render(request,'home.html',{})