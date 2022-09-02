from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from PIL import Image


def SportPage(request, sport):
    game = Sport.objects.get(name=sport)
    return render(request, 'sports/sport_page.html', {'sport':sport, 'game':game})
