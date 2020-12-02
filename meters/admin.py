import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum,Count
from .models import Meter,Readings


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
	list_display = ('m_id' , 'owner' , 'address','Pulses','units','amount')
	search_fields = ('owner',)
	list_filter = ('owner',)

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


@admin.register(Readings)
class ReadingsAdmin(admin.ModelAdmin):
	list_display = ('time_stamp' , 'reading')
	readonly_fields = ['reading']
	list_filter = ('meter',)
