from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Meter,Readings
from django.db.models import Sum

# Create your views here.

def pulse(request,m_id , rdg):
	mtr = Meter.objects.get(m_id=m_id)
	addReading = Readings(meter=mtr,reading=rdg)
	addReading.save()
	total = Readings.objects.filter(meter=mtr).aggregate(Sum('reading'))

	# return HttpResponse("<h1>smart meter app {},{}</h1>".format(m_id,rdg))
	data  = {'mtr': m_id,'owner' : mtr.owner.username,'total' : total["reading__sum"]}
	return JsonResponse(data)


def charts(request, m_id):
	return render(request,"meters/charts.html")
