"""questions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work import views


urlpatterns = [
    # HTTP pages
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('top5paxorigin/', views.top5paxorigin, name="top5paxorigin"),
    path("top5paxdestination", views.top5paxdestination, name="top5paxdestination"),
    path("top5forigin", views.top5forigin, name="top5forigin"),
    path("top5fdestination", views.top5fdestination, name="top5fdestination"),
    path("top5mailorigin", views.top5mailorigin, name="top5mailorigin"),
    path("top5maildestination", views.top5maildestination,
         name="top5maildestination"),
    path("top5origdistance", views.top5origdistance, name="top5origdistance"),
    path("top5destdistance", views.top5destdistance, name="top5destdistance"),
    path("highdistancexmonth", views.highdistancexmonth, name="highdistancexmonth"),
    path("highpaxxmonth", views.highpaxxmonth, name="highpaxxmonth"),
    path("Highfreight", views.Highfreight, name="Highfreight"),
    path("highpax", views.highpax, name="highpax"),
    path("highmail", views.highmail, name="highmail"),
    path("PaxXmonthairlines", views.PaxXmonthairlines, name="PaxXmonthairlines"),
    path("Avgpaxtowards", views.Avgpaxtowards, name="Avgpaxtowards"),
    path("avgfreightfrom", views.avgfreightfrom, name="avgfreightfrom"),
    path("pairhighfreightfar", views.pairhighfreightfar, name="pairhighfreightfar"),
    path("pairhighmailshort", views.pairhighmailshort, name="pairhighmailshort"),
    # Other
    # path('hello/', MarketList.as_view())
]
