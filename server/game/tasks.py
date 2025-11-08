from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_win_email(player_name, email):
    send_mail(
        subject="🎉 You Won the Game!",
        message=f"Congratulations {player_name}! You guessed the correct number!",
        from_email="noreply@gameapp.com",
        recipient_list=[email],
    )
    return "Email sent successfully"
