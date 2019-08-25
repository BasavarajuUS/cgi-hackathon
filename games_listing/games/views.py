# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from django.db.models import Q

from .models import Game


def home(request):
    context = {}
    return render(request, 'index.html', context)


class GameView(View):
    def get(self, request, game_id=None):

        if game_id:
            try:
                game = Game.objects.get(id=game_id)

            except Exception as e:
                return JsonResponse(
                    {"games": []},
                    reason="Game not Found",
                    status=404)

            return JsonResponse(
                {"games": [game.as_json()]},
                status=200)

        games = Game.objects.all()[:10]
        return JsonResponse(
            {"games": [game.as_json() for game in games]},
            status=200)

    def post(self, request):
        # Code block for POST request
        pass


class GameSearchView(View):
    def get(self, request):

        name = request.GET.get('name', '')
        value = request.GET.get('value', '')

        if name == 'title':
            games = Game.objects.filter(title__icontains=value).all()
        elif name == 'platform':
            games = Game.objects.filter(platform__icontains=value).all()
        elif name == 'genre':
            games = Game.objects.filter(genre__icontains=value).all()
        elif name == 'editors_choice':
            games = Game.objects.filter(editors_choice__icontains=value).all()
        else:
            games = Game.objects.filter(Q(title__icontains=value) |
                                        Q(platform__icontains=value) |
                                        Q(genre__icontains=value) |
                                        Q(editors_choice__icontains=value)).all()

        return JsonResponse(
            {"games": [game.as_json() for game in games]},
            status=200)
