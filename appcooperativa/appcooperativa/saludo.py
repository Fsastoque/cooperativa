from django.http import HttpResponse
def saludar(request, nombre):
    return HttpResponse(f'Buenas noches {nombre}')