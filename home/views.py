from django.shortcuts import render

def result(request):
    return render(request, 'result.html')

def home(request):
    return render(request, 'home/main.html')

def reservation(request):
    return render(request, 'reservation.html')
    
def reservation_ok(request):
    return render(request, 'reservation_ok.html')

def info(request):
    return render(request, 'info.html')