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
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            slot_request = form.save(commit=False)
            slot = form.cleaned_data.get('slot')
            slot_request.user = request.user
            slot_request.slot = slot
            slot_request.reason = form.cleaned_data.get('reason')
            slot.is_booked = True
            slot_request.save()

            messages.success(request, f'A confirmation mail would be sent shortly \
after the confirmation of the slot booking!')
            return redirect('home')

    else:
        form = BookingForm(instance=request.user)
    
    game = Sport.objects.get(code=sport)
    return render(request, 'sports/booking_page.html', {'game':game, 'form':form})
    