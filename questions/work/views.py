import pdb
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Max, Sum
import datetime

from work.models import MarketData

# Create your views here.


class MarketList(ListView):
    model = MarketData


def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})


def top5paxorigin(request):
    return render(request, "top5paxorigin.html", {"number": 5})


def top5paxdestination(request):
    return render(request, "top5paxdestination.html", {"number": 5})


def top5forigin(request):
    return render(request, "top5forigin.html", {"number": 5})


def top5mailorigin(request):
    return render(request, "top5mailorigin.html", {"number": 5})


def top5origdistance(request):
    return render(request, "top5origdistance.html", {"number": 5})


def top5fdestination(request):
    return render(request, "top5fdestination.html", {"number": 5})


def top5maildestination(request):
    return render(request, "top5maildestination.html", {"number": 5})


def top5destdistance(request):
    return render(request, "top5destdistance.html", {"number": 5})


def highdistancexmonth(request):
    return render(request, "top5destdistance.html", {"number": 5})


def highpaxxmonth(request):
    return render(request, "highdistancexmonth.html", {"number": 5})


def Highfreight(request):
    return render(request, "Highfreight.html", {"number": 5})


def highpax(request):
    return render(request, "highpax.html", {"number": 5})


def highmail(request):
    return render(request, "highmail.html", {"number": 5})


def PaxXmonthairlines(request):
    return render(request, "PaxXmonthairlines.html", {"number": 5})


def avgfreightfrom(request):
    return render(request, "avgfreightfrom.html", {"number": 5})


def Avgpaxtowards(request):
    return render(request, "Avgpaxtowards.html", {"number": 5})


def pairhighfreightfar(request):
    return render(request, "pairhighfreightfar.html", {"number": 5})


def pairhighmailshort(request):
    return render(request, "pairhighmailshort.html", {"number": 5})
