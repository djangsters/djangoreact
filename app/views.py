from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    context = {
        "Hello" : "Hello World - App"
    }
    return HttpResponse(template.render(context, request))
