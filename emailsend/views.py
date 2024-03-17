from django.shortcuts import render, redirect
from .models import UserEmail
from django.contrib import messages

# To Send Email
from django.core.mail import send_mail

# Create your views here.
def Home(request):
    if request.method == "POST":
        clientName = request.POST.get('clientName')
        clientEmail = request.POST.get('clientEmail')
        clientMessage = request.POST.get('clientMessage')

        send_mail(
            f"New Email From { clientName}",
            clientMessage,
            clientEmail,
            ['kipkuruijapheth11@gmail.com'],
            fail_silently=False,
        )


        email = UserEmail(clientEmail=clientEmail, clientName=clientName, clientMessage=clientMessage)
        email.save()
        messages.success(request, "Your message has been sent successfully!", extra_tags="message-div")
        return redirect("home")
    return render(request, 'emailsend/index.html')