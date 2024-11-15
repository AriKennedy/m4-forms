from django.shortcuts import render
from django.http import HttpResponse
from .forms import FrontTimesForm, NoTeenSumsForm, XyzThereForm, CenteredAverageForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

# Front Times
def front_times_view(request):
    if request.method == 'GET':
        form = FrontTimesForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['text']
            n = form.cleaned_data['n']
            front = text[:3]
            result = front * n
            return HttpResponse(f"Result: {result}")
        else:
            form = FrontTimesForm()
        return render(request, 'front_times.html', {'form': form})

# No Teen Sums
def no_teen_sums_view(request):
    if request.method == 'GET':
        form = NoTeenSumsForm(request.GET)
        if form.is_valid():
            a, b, c = form.cleaned_data['a'], form.cleaned_data['b'], form.cleaned_data['c']
            def fix_teen(n):
                return 0 if n in [13, 14, 17, 18, 19] else n
            result = fix_teen(a) + fix_teen(b) + fix_teen(c)
            return HttpResponse(f"Result: {result}")
        else:
            form = NoTeenSumsForm()
        return render(request, 'no_teen_sums.html', {'form': form})

# XYZ There
def xyz_there_view(request):
    if request.method == 'GET':
        form = XyzThereForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = 'xyz' in text.replace('.xyz', '')
            return HttpResponse(f"Result: {result}")
        else:
            form = XyzThereForm()
        return render(request, 'xyz_there.html', {'form': form})

# Centered Average
def centered_average_view(request):
    if request.method == 'GET':
        form = CenteredAverageForm(request.GET)
        if form.is_valid():
            numbers = list(map(int, form.cleaned_data['numbers'].split(',')))
            def centered_average(nums):
                small = min(nums)
                big = max(nums)
                return (sum(nums) - small - big) // (len(nums) - 2)
            result = centered_average(numbers)
            return HttpResponse(f"Result: {result}")
        else:
            form = CenteredAverageForm()
        return render(request, 'centered_average.html', {'form': form})
