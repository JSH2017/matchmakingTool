from django.http import HttpResponse
from django.template import loader
from empleos import services
import logging
import logging.config


#def home(request):
#    return HttpResponse('Home de las listas de ofertas de empleos')
logger = logging.getLogger(__name__)

def home(request):
	#categorias_name = []
	categorias =  services.get_categorias()
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	logger.debug(categorias)
	template = loader.get_template('empleos/home.html')
	context = {
	'categorias': categorias,
	}
	return HttpResponse(template.render(context, request))

 