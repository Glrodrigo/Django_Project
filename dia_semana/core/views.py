from django.shortcuts import render
from asyncore import dispatcher_with_send
from datetime import datetime
from .models import Dia_semanaModel

def verifica_domingo(request):
    #contexto = {'domingo': True,
                #'segunda': False}
    #return render(request, 'domingo.html', contexto)
    #return render(request, 'domingo.html')
    today = datetime.today()
    result = Dia_semanaModel.objects.filter(day=today.day).filter(month=today.month)
    if len(result) > 0:
        contexto = {'dia da semana': True, 'nome': result[0].name}
    else:
        contexto = {'dia da semana': False}
    return render(request, 'domingo.html', contexto)

