from django.shortcuts import render
from scoreBoard.models import scoreBoard
# Create your views here.

def index(request):
    return render(request, 'scoreBoard/index.html')

def scores(request):
    teamscore_list = scoreBoard.objects.order_by('-team_score')
    team_dict = {'team_name':teamscore_list}
    return render(request, 'scoreBoard/scoreBoard.html', context=team_dict)
