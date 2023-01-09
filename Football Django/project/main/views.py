from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Team, Championship, Achievement, Message
from django.db.models import Count
from .forms import CreateNewMessage
from datetime import datetime

def teamIndex(response, id):
    team = Team.objects.get(id=id)
    achievements = Achievement.objects.filter(team_id=id).values('championship__name','date','id').order_by('-date')[:15]
    return render(response, "main/team.html", {"team":team, "achievements": achievements})

def teamsList(response):
    teams = Team.objects.all().values('name','theme_color', 'country', 'id').annotate(count=Count('achievement__id'))
    return render(response, "main/teams.html", {"teams":teams})

def championshipIndex(response, id):
    championship = Championship.objects.get(id=id)
    achievements = Achievement.objects.filter(championship_id=id).values('team__name').annotate(count=Count('team_id')).order_by('-count')[:5]
    return render(response, "main/championship.html", {"championship":championship, "achievements": achievements})

def championshipsList(response):
    championships = Championship.objects.all()
    return render(response, "main/championships.html", {"championships":championships})

def visitorPlace(response):
    form = CreateNewMessage()
    if response.method == "POST":
        form = CreateNewMessage(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            favTeam = form.cleaned_data["favTeam"]
            t = Message(name=name,message=message,favTeam=favTeam,date=datetime.now())
            t.save()
            return HttpResponseRedirect(f'/visitor')
    print(form.__dict__)
    messages = Message.objects.all().values('favTeam__name','name','date','message').order_by('-date')[:5]
    return render(response,"main/visitor.html", {"messages": messages,"form": form})

def home(response):
    numberRecords = {'teams': 0, 'achievements': 0, 'championships': 0}
    numberRecords['teams'] = Team.objects.all().annotate(count=Count('id'))
    numberRecords['championships'] = Championship.objects.all().annotate(count=Count('id'))
    numberRecords['achievements'] = Achievement.objects.all().annotate(count=Count('id'))
    return render(response, "main/home.html", {'numberRecords': numberRecords})

