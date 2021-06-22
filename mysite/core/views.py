from django.shortcuts import render
from django.http import JsonResponse

from mysite.core.models import Country
from mysite.core.methods import csv_to_db


def home(request):
    # WARNING: uncomment line below only first time you run the application if there is not any countries.json file to load data!!!
    # csv_to_db() 
    return render(request, 'home.html')


def bar_chart(request):
    labels = []
    data = []

    queryset = Country.objects.order_by('-appeared')
    for entry in queryset:
        if entry.appeared > 0:
          labels.append(entry.name)
          data.append(entry.appeared)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def pie_chart(request):
    labels = []
    data = []

    queryset = Country.objects.order_by('-appeared')[:7]
    for country in queryset:
        labels.append(country.code)
        data.append(country.appeared)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })
