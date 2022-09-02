from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from PIL import Image


@login_required
def SportPage(request, sport):
    game = Sport.objects.get(code=sport)
    return render(request, 'sports/sport_page.html', {'game':game})


@login_required
def book(request, sport):
    game = Sport.objects.get(code=sport)
    return render(request, 'sports/booking_page.html', {'game':game})
    