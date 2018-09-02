from django.shortcuts import render, get_object_or_404, redirect
from .models import Hero, Quest
from django.template import RequestContext


def hero(request, hero_id):
    #all_quests = Quest.objects.all()
    hero = get_object_or_404(Hero, pk=hero_id)
    all_quests = hero.quests.all
    exp = hero.exp
    context = {'hero': hero, 'level' : '11', 'exp' : exp, 'all_quests': all_quests}

    return render(request, 'quests/hero.html', context)


def levelup(request, quest_id, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    quest = get_object_or_404(Quest, pk=quest_id)
    all_quests = hero.quests.all
    exp = hero.exp
    gained_exp = 100
    hero.exp += gained_exp
    hero.save()
    context = {'quest': quest, 'hero': hero, 'level': '11', 'exp': exp, 'all_quests': all_quests}

    return redirect('quests:quests', quest_id, hero_id)


def quests(request, quest_id, hero_id):
    quest = get_object_or_404(Quest, pk=quest_id)
    hero = get_object_or_404(Hero, pk=hero_id)
    exp = hero.exp
    context = {'quest': quest, 'level': '11', 'exp': exp, 'hero': hero, }

    return render(request, 'quests/quests_details.html', context)


def index(request):
    all_quests = Quest.objects.all()
    context = {'all_quests': all_quests}
    return render(request, 'quests/index.html', context)



