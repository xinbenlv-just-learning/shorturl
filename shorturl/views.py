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
import settings
import datetime
val = URLValidator(verify_exists=False)
def short_url_redirect(request,short):
    try:
        s_id = short_url_algorithm.decode_url(short)        
         
        sue = Sue.objects.get(id= s_id)
        original = sue.original
        sue.count = sue.count + 1
        sue.save()
        return redirect(original)
    except ObjectDoesNotExist,e :
        original = 'http://u.zzn.im' 
        return render_to_response('redirect.html', {
            'url':original
        },RequestContext(request))  
    except ValueError,e :
        original = 'http://u.zzn.im' 
 
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
            sue = sue_form.save(commit=False)
            sue.count=0;
            sue.created_date=datetime.datetime.now()
            print "xxx"
            o = sue.original
            o_lower = o.lower()
            if o_lower.startswith('http://') ==False and o_lower.startswith('https://') == False:
                sue.original = 'http://'+sue.original
            try:
                val(sue.original)
            except ValidationError, e:
                #TODO-victor: redirect with a error message
                return HttpResponseRedirect('/')
            try:
                # Check if we already have it
                sue = Sue.objects.get(original = sue.original)
            except :
                # Here we insert a new entry
                sue.save()
                return HttpResponseRedirect('/') # Redirect after POST
            return HttpResponseRedirect('/') # Redirect after POST
 
    else:
        sue_form = SueForm() # An unbound form
        
    return render_to_response('index.html', {
        'sue_form': sue_form,
        'stored': stored,
        'current_path': request.get_full_path(),
        'myurl': settings.PROJECT_DOMAIN,
    },RequestContext(request)) 

def contact(request):
    return HttpResponseRedirect('http://www.zzn.im')   
def about(request):
    return render_to_response('about.html', {},RequestContext(request))   
