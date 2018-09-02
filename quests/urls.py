from django.urls import path
from . import views

app_name = 'quests'

urlpatterns = [

    path('', views.index, name='index'),
    path('hero/<int:hero_id>', views.hero, name='hero'),
    path('quest/<int:quest_id>/hero/<int:hero_id>', views.quests, name='quests'),
    path('quest/<int:quest_id>/hero/<int:hero_id>/levelup', views.levelup, name='levelup'),

]