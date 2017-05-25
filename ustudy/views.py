from django.shortcuts import HttpResponse, render

def home(request):
    '''
    Renders the home page 
    '''
    return render(request, 'home.html', context=None)