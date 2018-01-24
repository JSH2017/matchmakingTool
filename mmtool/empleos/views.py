from django.http import HttpResponse
from empleos import services


#def home(request):
#    return HttpResponse('Home de las listas de ofertas de empleos')


def home(request):
	categorias_name = []
	categorias =  services.get_categorias()

	for categoria in categorias:
		categorias_name.append(categoria.name)
		response_html = '<br>'.join(categorias_name)
	return HttpResponse(response_html)

 