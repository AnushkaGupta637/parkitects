# from django.shortcuts import render,HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("this is a homepage")
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Slot
from django.urls import reverse
# from .forms import FeedbackForm


def login(request):
    return render(request, 'home/login.html')

def dashboard(request):
    # Your dashboard view logic goes here
    return render(request, 'home/dashboard.html')

# def book_slot(request):
#     return render(request, 'home/book_slot.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user
            login(request, user)
            # Redirect to the dashboard page
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'home/signup.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        # Process the form data here (save to the database, send email, etc.)
        # Example: Save the feedback to the database (replace this with your actual logic)
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        # Add your logic to save the feedback to the database
        # ...

        # Redirect to a thank you page or the home page
        # return redirect('thank_you')  # You need to define a 'thank_you' URL in your urls.py

    # If the form is not submitted, render the feedback form page
    return render(request, 'home/feedback.html')

# def submit_feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             return redirect('submit_feedback')
#     else:
#         form = FeedbackForm()

#     return render(request, 'submit_feedback.html', {'form': form})
def submit_feedback(request):
    return render(request, 'home/submit_feedback.html')

def find_spot(request):
    if request.method == 'POST':
        # Assuming you have a model named Vehicle with a field 'plate_number'
        plate_number = request.POST.get('plate_number')
        
        try:
            # Retrieve the vehicle information from the database
            vehicle = vehicle.objects.get(plate_number=plate_number)
            slot_number = vehicle.slot_number

            # Redirect to find_spot_result with parameters
            return redirect(reverse('find_spot_result') + f'?slot_number={slot_number}&plate_number={plate_number}')
        except vehicle.DoesNotExist:
            # Vehicle not found, handle this case as needed
            context = {'error_message': 'Vehicle not found'}
            return render(request, 'find_spot.html', context)

    return render(request, 'find_spot.html')
def find_spot_result(request):
    # Retrieve slot_number and plate_number from the request or session
    slot_number = request.GET.get('slot_number')
    plate_number = request.GET.get('plate_number')

    context = {'slot_number': slot_number, 'plate_number': plate_number}
    return render(request, 'find_spot_result.html', context)
def available_slot(request):
    available_slot = Slot.objects.filter(booked=False)[:10]
    return render(request, 'available_slot.html', {'available_slot': available_slot})

def book_slot(request, slot_number=None):
    if slot_number:
        slot = Slot.objects.get(slot_number=slot_number)

        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booked_slot = Slot.objects.create(
                    slot_number=slot_number,
                    booked=True,
                    name=form.cleaned_data['name'],
                    car_plate=form.cleaned_data['car_plate'],
                    phone=form.cleaned_data['phone'],
                )
                return redirect('dashboard')
        else:
            form = BookingForm()

        return render(request, 'book_slot.html', {'form': form, 'slot': slot})
    else:
        return render(request, 'book_slot.html', {'form': BookingForm()})
def end(request):
    return render(request, 'end.html')
