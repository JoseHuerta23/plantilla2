from django.contrib import admin
from .models import Estacion, Estado, Tipos, Estatus, Responsable, User, Extranjeros
# Register your models here.

admin.site.register(Estacion)
admin.site.register(Estado)
admin.site.register(Tipos)
admin.site.register(Estatus)
admin.site.register(Responsable)
admin.site.register(User)
admin.site.register(Extranjeros)