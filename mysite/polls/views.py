import smtplib
import ssl
import glob
import os
from PIL import Image
import sys
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Profile
import asyncio

# Create your views here.
home_actions = ["Home", "Services", "Contacts", "About"]


def index(request):
    # Homepage actions

    return render(request, "polls/Home.html", {"home_actions": home_actions})


def sendmail(useremail, message):
    senderemail = "yellowredpidemi@gmail.com"
    receiveremail = "djaliloua@gmail.com"
    port = 465
    pwd = "betnivjooxiutxle"
    message1 = f"You received message from: {useremail}\n\n {message}"
    # Create context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderemail, pwd)
        server.sendmail(senderemail, receiveremail, "You received message from:" + " " + useremail + "\n" + message)
        print("Mail sent...")


def contacts(request):
    if request.method == "POST":
        useremail = request.POST.get("email")
        subject = request.POST["subject"]
        usertext = request.POST.get("text")

        message = f"Sent by: {useremail}\nSubject: {subject}\n\n {usertext}"
        try:
            # sendmail(useremail, message)
            send_mail(subject, message, "yellowredpidemi@gmail.com",
                      ["djaliloua@gmail.com"])
            return render(request, "polls/success.html", {"home_actions": home_actions})
        except:
            # print(Exception)
            return render(request, "polls/failurepage.html", {"home_actions": home_actions})

    return render(request, "polls/Contacts.html", {"home_actions": home_actions})


profiles = list(Profile.objects.all())


def resizeimage():
    listofimagepaths = [p.photo.path for p in profiles]
    for path in listofimagepaths:
        image = Image.open(path)
        new_image = image.resize((256, 256))
        pathlist = path.split(".")
        new_image.save(path)
    print("done.")
    # image = Image.open()

# Process the image profiles
# resizeimage()


def about(request):
    # resizeimage()
    return render(request, "polls/About.html", {
        "home_actions": home_actions,
        "profiles": profiles,
    }
                  )


def services(request):
    if request.method == "POST":
        x = request.POST["x"]
        y = request.POST["y"]
        if x == "":
            x = 0
        if y == "":
            y = 0

        return render(request, "polls/Services.html", {"home_actions": home_actions, "results": int(x) + int(y)})

    return render(request, "polls/Services.html", {"home_actions": home_actions})
