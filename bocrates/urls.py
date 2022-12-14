"""bocrates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from bocrates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bocrates/',views.RatesList),
    path('bankrate/', views.GetBankRate),
    path('targetrate/', views.GetTargetRate),
    path('10yearbond/',views.Get10yearBondRate),
    path('2yearbond/',views.Get2yearBondRate),
    path('5yearbond/',views.Get5yearBondRate),
    path('3yearbond/',views.Get3yearBondRate),
    path('7yearbond/',views.Get7yearBondRate),
    path('longtermbond/',views.GetLongTermBondRate),
    path('mmfinancing/',views.GetMMFinancingRate)
]
