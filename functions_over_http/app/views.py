from django.shortcuts import render
from django.http import HttpResponse
from .forms import HeyYouForm, AgeInForm, OrderForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def hey_you_view(request):
    if request.method == 'POST':
        form = HeyYouForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return HttpResponse(f"Hey, {name.capitalize()}!")
    else:
        form = HeyYouForm()
    return render(request, 'hey_you.html', {'form': form})

# Age In View
def age_in_view(request):
    if request.method == 'POST':
        form = AgeInForm(request.POST)
        if form.is_valid():
            end_year = form.cleaned_data['end_year']
            birth_year = form.cleaned_data['birth_year']
            age = end_year - birth_year
            return HttpResponse(f"You will be {age} years old in {end_year}.")
    else:
        form = AgeInForm()
    return render(request, 'age_in.html', {'form': form})

# Order Total View
def order_total_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            burgers = form.cleaned_data['burgers']
            fries = form.cleaned_data['fries']
            drinks = form.cleaned_data['drinks']
            total = (burgers * 4.50) + (fries * 1.5) + (drinks * 1)
            return HttpResponse(f"Your order total is: ${total:.2f}")
    else:
        form = OrderForm()
    return render(request, 'order_total.html', {'form': form})