from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month")
#
# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes everyday")

challenges = {
        "january": "Eat no meat for the entire month!",
        "february":"Walk for atleast 20 minutes everyday",
        "march":"Learn Django for atleast 20 minutes everyday",
        "april":"Learn TypeScript in one month",
        "may":"Learn mongodb for atleast 1 hour daily",
        "june":"Learn how to draw",
        "july":"Learn how to play Guitar",
        "august":"Make atleast 5 new friends in the entire month",
        "september":"Save atleast INR 20000 in the whole month",
        "october":"Donate to poor people for the whole month",
        "november": "Learn a foriegn language",
        "december": "Do meditation for atleast half an hour daily"

        }

def index(request):
   
    months = list(challenges.keys())
    list_elements = ""
    for month in months:
        month_url = reverse("month-challenge",args=[month])
        list_elements += f"<li><a href=\"{month_url}\">{month}</a></li>"
    response_data = f"<ul>{list_elements}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months = list(challenges.keys())
    month_index = month-1
    if(month_index >= 0 and month_index <12):
        redirect_month = months[month-1]
        redirect_url = reverse("month-challenge",args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound("<h1>It is not a valid month</h1>")

def monthly_challenge(request,month):
    challenge_text = ""
    if(month in challenges.keys()):
        challenge_text = challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    else:
        challenge_text = "This month is not supported"
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponseNotFound(response_data)
