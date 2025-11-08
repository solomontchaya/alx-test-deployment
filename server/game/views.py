import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .tasks import send_win_email

# Create your views here.
@api_view(['POST'])
def start_game(request):
    name = request.data.get('player_name')
    if not name:
        return Response({"error": "Player name required"}, status=400)
    game = Game.objects.create(player_name=name, secret_number=random.randint(1, 100))
    return Response({"game_id": game.id, "message": "Game started! Guess a number between 1 and 100."})

@api_view(['POST'])
def guess_number(request, game_id):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return Response({"error": "Game not found"}, status=404)

    guess = int(request.data.get('guess'))
    game.attempts += 1

    if guess < game.secret_number:
        game.save()
        return Response({"result": "Too low!"})
    elif guess > game.secret_number:
        game.save()
        return Response({"result": "Too high!"})
    else:
        game.is_won = True
        game.save()
        send_win_email.delay(game.player_name, "test@example.com")
        return Response({"result": "Correct! You won!"})
