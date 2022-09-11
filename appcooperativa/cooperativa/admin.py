from django.contrib import admin
from .models import cliente
from .models import Lineas_De_Credito
from .models import credito

admin.site.register(cliente)
admin.site.register(Lineas_De_Credito)
admin.site.register(credito)
# Register your models here.
