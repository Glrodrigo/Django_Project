from django.shortcuts import render

def domingo(request):
    contexto = {'domingo': True,
                'segunda': False}
    return render(request, 'domingo.html', contexto)
    #return render(request, 'domingo.html')