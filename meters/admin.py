import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum,Count
from .models import Meter,Readings
from django.utils.html import format_html
from django.template.response import TemplateResponse
from django.urls import path

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
	list_display = ('m_id' , 'owner' , 'address','Pulses','units','amount', 'charts')
	search_fields = ('owner',)
	list_filter = ('owner',)
	
	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
		path('<int:m_id>/charts/', self.analyse),
		]
		return my_urls + urls

	def analyse(self, request, m_id):
		meter = Meter.objects.get(pk=m_id)
		readings = Readings.objects.filter(meter=meter)
		data = {}
		for pulse in range(len(readings)):
			time  = readings[pulse].time_stamp.strftime("%m/%d/%Y")
			if data.get(time,None)==None:
				data[time] = readings[pulse].reading
			else:
				data[time]+=readings[pulse].reading 


		print(list(data.items()))
		# ...
		context = dict(
			# Include common variables for rendering the admin template.
			self.admin_site.each_context(request),
			# Anything else you want in the context...
			meter=m_id,
			data = list(data.items())
			)
		return TemplateResponse(request, "admin/charts.html", context)



	def Pulses(self,obj):
		total_pulses = Readings.objects.filter(meter=obj).aggregate(Sum('reading'))
		return total_pulses["reading__sum"]
	
	def units(self,obj):
		total_Units = self.Pulses(obj)/3200
		return total_Units


	def amount(self,obj):
		one_unit_rate = 4
		total_amt   = self.units(obj)*one_unit_rate   
		return total_amt

	def charts(self, obj):
		id = obj.pk;
		url = f'{id}/charts/'
		return format_html('<a href="{}">usage</a>', url)



@admin.register(Readings)
class ReadingsAdmin(admin.ModelAdmin):
	list_display = ('time_stamp' , 'reading')
	readonly_fields = ['reading']
	list_filter = ('meter',)
