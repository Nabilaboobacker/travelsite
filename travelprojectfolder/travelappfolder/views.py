from django.shortcuts import render

from travelappfolder.models import travelgram, teams


def home(request):
    obj1 = travelgram.objects.all()
    obj2 = teams.objects.all()
    return render(request, 'index.html', {'result1': obj1, 'result2': obj2})

