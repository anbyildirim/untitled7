from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import Teacher
from forms import Student
from forms import Course


def index(request):
    if request.method=="GET":
        teacher= Teacher
        return render_to_response("base_html.html",{"types":teacher})


    #return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    if request.method=="Get":
        student= Student
        return render_to_response("base_html.html", {"types": student})




def search(request):
    if 'q' in request.GET:
        message = 'You searched for : %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


'''
from  forms import AuthorForm
def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
        a.save()
        return HttpResponseRedirect('/all-authors/')
    else:
        form = AuthorForm()
    return render_to_response('addauthor.html',
                {'form': form},RequestContext(request))  '''



