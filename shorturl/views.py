from django.shortcuts import render_to_response ,redirect
from shorturl.forms import SueForm
from shorturl.models import Sue
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import short_url_algorithm
from django.core.exceptions import ObjectDoesNotExist
import sys
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

val = URLValidator(verify_exists=False)
def short_url_redirect(request,short):
    try:
        s_id = short_url_algorithm.decode_url(short)        
        original = Sue.objects.get(id= s_id).original
        return redirect(original)
    except ObjectDoesNotExist,e :
        original = 'http://google.com' 
        return render_to_response('redirect.html', {
            'url':original
        },RequestContext(request))  
    except ValueError,e :
        original = 'http://google.com' 
 
        return render_to_response('redirect.html', {
            'url':original
        },RequestContext(request))  
     
def home(request):
    stored = Sue.objects.all()
    for s in stored:
      s.short = short_url_algorithm.encode_url(s.id)

    if request.method == 'POST': # If the form has been submitted...
        sue_form = SueForm(request.POST) # A form bound to the POST data
        
        if sue_form.is_valid():
            o = sue_form.cleaned_data['original']
            o_lower = o.lower()
            if o_lower.startswith('http://') ==False and o_lower.startswith('https://') == False:
                o = 'http://'+o
            try:
                val(o)
            except ValidationError, e:
                #TODO-victor: redirect with a error message
                print e
                return HttpResponseRedirect('/')
            try:
                print 'xxx3'
                sue = Sue.objects.get(original = o)
            except :
                # Here we insert a new entry
                sue_form.save()
                return HttpResponseRedirect('/') # Redirect after POST
            return HttpResponseRedirect('/') # Redirect after POST
 
    else:
        sue_form = SueForm() # An unbound form
        
    return render_to_response('index.html', {
        'sue_form': sue_form,
        'stored': stored,
    },RequestContext(request))  
