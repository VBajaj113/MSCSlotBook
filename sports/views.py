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
def book(request, sport, date):
    game = Sport.objects.get(code = sport)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            user = request.user
            n = 0
            for i in list(game.slot_set.filter(date=date)):
                if i.is_booked and user == i.bookrequest.user:
                    n+=1
            if (n>=3):
                messages.warning(request, 'Sorry, you have already reached the maximum amount of bookings for a day!')
            else:
                slot_request = form.save(commit=False)
                slot = form.cleaned_data.get('slot')
                slot_request.user = request.user
                slot_request.slot = slot
                slot_request.reason = form.cleaned_data.get('reason')
                slot_request.is_accepted = True
                slot_request.is_pending = False
                slot.is_booked = True
                slot.save()
                slot_request.save()

                messages.success(request, 'A confirmation mail would be sent shortly \
    after the confirmation of the slot booking!')
            return redirect('home')

    else:
        form = BookingForm(instance=request.user)
    
    slot_lis = list(game.slot_set.filter(date=date))
    return render(request, 'sports/booking_page.html', {'game':game, 'form':form, 'slot_lis':slot_lis})


@login_required
def slot_date(request, sport, date = None):
    if request.method == 'POST':
        form = SlotDate(request.POST)

        if form.is_valid():
            date = form.cleaned_data.get('date')
            game = Sport.objects.get(code=sport)
            return redirect(f'{date}/')
    
    else:
        form = SlotDate(instance=request.user)
    
    game = Sport.objects.get(code=sport)
    return render(request, 'sports/date.html', {'game':game, 'form':form})