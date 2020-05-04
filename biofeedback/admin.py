from django.contrib import admin
from .models import Paciente, HistoriaMedica, Terapia
from django.utils.html import format_html
# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    list_filter = ['religion','lateralidad']
    search_fields = ['nombre', 'apellido','cedula' ]

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>Historias Clinicas</a>", url='../historiamedica/?q='+str( obj.cedula)) 
    show_firm_url.short_description = 'Sesion' 

    list_display = ('cedula', 'nombre', 'apellido','carrera','telefono', 'show_firm_url')

class HistoriaMedicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'created_date', 'show_firm_url' ]
    list_filter = ['created_date']
    search_fields = ['paciente__nombre','paciente__apellido','paciente__cedula','enfermedad']

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>Iniciar</a>", url='../../../bio/test/') 
    show_firm_url.short_description = 'Sesion'


class TerapiaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'ruta', 'created_date' ]
    list_filter = ['created_date']
    search_fields = ['paciente__nombre','paciente__apellido','paciente__cedula']



admin.site.register(Paciente,PacienteAdmin)
admin.site.register(HistoriaMedica,HistoriaMedicaAdmin)
admin.site.register(Terapia,TerapiaAdmin)