from django.shortcuts import render, redirect
import uuid ##If all you want is a unique ID, you should probably call uuid1() or uuid4(). Note that uuid1() may compromise privacy since it creates a UUID containing the computer's network address. uuid4() creates a random UUID.
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):##rendering index.html file
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST': # #cheking method is post are not. 
        link = request.POST['link']  #accesing the input long url from user.
        uid = str(uuid.uuid4())[:5] # creating a ranadam id(by using univeselly unique identifier(uuid) module).
        new_url = Url(link=link,uuid=uid)  # creating url in data base as 2 argumentss link as long url uuid as new url  
        new_url.save() # saving the new url in data base
        return HttpResponse(uid) # returning uid(short url)
    
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)

