from django.shortcuts import render_to_response 
from shorturl.forms import SueForm
from shorturl.models import Sue
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def short_from_id(key):
import short_url
  return str(id)
def home(request):
    stored = Sue.objects.all()
    for s in stored:
      s.short = short_from_id(s.id)
    if request.method == 'POST': # If the form has been submitted...
        sue_form = SueForm(request.POST) # A form bound to the POST data
        if sue_form.is_valid(): # All validation rules pass
            sue_form.save() 
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        sue_form = SueForm() # An unbound form
        
    return render_to_response('index.html', {
        'sue_form': sue_form,
        'stored': stored,
    },RequestContext(request))  
