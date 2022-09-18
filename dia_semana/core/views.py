from django.http import HttpResponse

def domingo(request):
   return HttpResponse("Não é domingo...")