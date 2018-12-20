from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def entrance(request):
    return HttpResponseRedirect(reverse('booking_system:login'))


def index(request):
    if request.session.get('is_login'):
        context = {
            'session' : request.session,
        }
        return render(request, 'booking_system/index.html', context)
    else:
        return HttpResponseRedirect(reverse('booking_system:login'))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['is_login'] = True
        request.session['username'] = username
        request.session['password'] = password
        return HttpResponseRedirect(reverse('booking_system:index'))
    else:
        return render(request, 'booking_system/login.html')


def register(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        return render(request, 'booking_system/login.html')
    else:
        return render(request, 'booking_system/register.html')


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('booking_system:login'))


def flight_query(request):
    context = {
        'session' : request.session,
    }
    return render(request, 'booking_system/flight_query.html', context)


def flight_display(request):
    context = {
        'session' : request.session,
    }
    return render(request, 'booking_system/flight_display.html', context)