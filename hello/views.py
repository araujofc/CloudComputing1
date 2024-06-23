from django.http import HttpResponse

def home(request):
    return HttpResponse("Nome: Fabricio Coutinho de Araujo Disciplina:Cloud Computing & Site Reliability Engineering")