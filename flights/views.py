
from django.shortcuts import render, redirect
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "flights/home.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

#  crud opertions
# create
""" def add_flight(request):
    if request.method == "POST":
        origin = request.POST['origin']
        destination = request.POST['destination']
        duration = request.POST['duration']
        flight = Flight(origin=origin, destination=destination, duration=duration)
        flight.save()
        return redirect('home')
    return render(request, "flights/add_flight.html")

from .models import Flight, Airport, Passenger
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse """

def add_flight(request):
    if request.method == "POST":
        origin_code = request.POST['origin']
        destination_code = request.POST['destination']
        duration = request.POST['duration']

        origin = Airport.objects.get(code=origin_code)
        destination = Airport.objects.get(code=destination_code)

        flight = Flight(origin=origin, destination=destination, duration=duration)
        flight.save()

        return redirect('home')
    return render(request, "flights/add_flight.html", {
        "airports": Airport.objects.all()
    })

# update
def edit_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if request.method == "POST":
        flight.origin = request.POST['origin']
        flight.destination = request.POST['destination']
        flight.duration = request.POST['duration']
        flight.save()
        return redirect('home')
    return render(request, "flights/edit_flight.html", {
        "flight": flight
    })

# delete
def delete_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if request.method == "POST":
        flight.delete()
        return redirect('home')
    return render(request, "flights/delete_flight.html", {
        "flight": flight
    })
