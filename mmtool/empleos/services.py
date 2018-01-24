from __future__ import print_function
from empleos.models import Empleo
from empleos.models import Empresa
from empleos.models import Categoria
from empleos.rest import ApiException
from pprint import pprint
from empleos.api import empleos_api

import time
import empleos

def get_empleos(limit=None, **filters):
    """ simple service function for retrieving books can be widely extended """
    if limit:
        return Empleo.objects.filter(**filters)[:limit]
    return Empleo.objects.filter(**filters)


def get_centroscomunitarios(id_banco_alimentos):
	
	# create an instance of the API class
	api_instance = empleos.CentroComunitarioApi() 

	try:
	    # Lista los centros comunitarios asignados al banco de alimentos
	    api_response = api_instance.centrocomunitario_find_by_bancode_alimento_id_banco_alimentos_get(id_banco_alimentos)
	    pprint(api_response)
	except ApiException as e:
	    print("Exception when calling CentroComunitarioApi->centrocomunitario_find_by_bancode_alimento_id_banco_alimentos_get: %s\n" % e)

def get_empleos_by_centro_comunitario(centro_comunitario_id):
	
	api_instance = empleos_api.EmpleoApi()
	api_instance.find_jobs_by_centro_comunitario(centro_comunitario_id)

def get_categorias():
	lista=[]
	for i in range(10):
		categoria = Categoria(id=i,name="categoria ")
		lista.append(categoria)
	return lista