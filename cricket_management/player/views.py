from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from cricket.models import Player, Match

@login_required
def dashboard(request):
    if request.user.role != 'player':
        return HttpResponseForbidden("Not allowed")

    return render(request, 'player/dashboard.html')

@login_required
def player_profile(request):
    player = Player.objects.get(user=request.user)
    return render(request, 'player/profile.html', {
        'player': player
    })


@login_required
def player_matches(request):
    player = Player.objects.get(user=request.user)

    matches = Match.objects.none()

    if player.team:
        matches = Match.objects.filter(
            team1=player.team
        ) | Match.objects.filter(
            team2=player.team
        )

    return render(request, 'player/matches.html', {
        'matches': matches,
        'team': player.team
    })

