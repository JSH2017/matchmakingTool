from django.http import HttpResponse

def home(request):
    return HttpResponse('Home de las listas de ofertas de empleos')