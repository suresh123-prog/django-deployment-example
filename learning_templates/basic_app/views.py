#from django.shortcuts import render

# Create your views here.
#def index(request):
    #return render(request,'basic_app/index.html')

#def other(request):
    #return render(request,'basic_app/other.html')

#def relative(request):
    #return render(request,'basic_app/relative_url_templates.html')


#Django_Template_Filters
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','numbers':100}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
