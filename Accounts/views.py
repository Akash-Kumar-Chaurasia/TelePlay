from contextlib import redirect_stderr
import imp
import re
from urllib.robotparser import RequestRate
from django.shortcuts import  render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm

from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import email

# Create your views here.
def index(request):
    return render(request, 'Accounts/index.html')

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'ho gya bhai {username}')
            email = request.POST['email']
            ml = emails.objects.create(user_mail = email)
            return HttpResponseRedirect('../')
    else:
        form = UserRegistrationForm()
    return render (request, 'Accounts/Signup.html', context = {'form' : form})

def massmail(request):
    if request.method == "POST":    
        mail_list = emails.objects.values_list('user_mail', flat=True)
        
        print(list(mail_list))
        title = request.POST.get('title')
        message = request.POST.get('message')
        send_mail(title, message, 'teleplayvit@gmail.com', mail_list)
    return render(request, 'Accounts/massmail.html')
    
def bhramstra(request):
    return render (request, 'Accounts/Movie.html')
def search(request):
    return render (request, 'Accounts/seach.html')
def privacypolicy(request):
    return render (request, 'Accounts/privacy_policy.html')
def TermsandCondition(request):
    return render (request, 'Accounts/terms.html')
def AboutUs(request):
    return render (request, 'Accounts/about_us.html')
def THRUSDAY(request):
    return render (request, 'Accounts/THRUSDAY.html')
def sangchi(request):
    return render (request, 'Accounts/sangchi.html')
def uri(request):
    return render (request, 'Accounts/uri.html')
def onenineoneseven(request):
    return render (request, 'Accounts/1917.html')
def Red_notice(request):
    return render (request, 'Accounts/Red_notice.html')
def black_panther(request):
    return render (request, 'Accounts/black_panther.html')
def dark_knight(request):
    return render (request, 'Accounts/dark_knight.html')
def casino_royale(request):
    return render (request, 'Accounts/casino_royale.html')
def dune(request):
    return render (request, 'Accounts/dune.html')
def captainmarvel(request):
    return render (request, 'Accounts/captainmarvel.html')
def wonderwoman(request):
    return render (request, 'Accounts/wonderwoman.html')
def AvengersEndgame(request):
    return render (request, 'Accounts/AvengersEndgame.html')
def SavingPrivateRyan(request):
    return render (request, 'Accounts/SavingPrivateRyan.html')
def MatrixResurrections(request):
    return render (request, 'Accounts/MatrixResurrections.html')
def lotr(request):
    return render (request, 'Accounts/lotr.html')
def venom(request):
    return render (request, 'Accounts/venom.html')
def intersteller(request):
    return render (request, 'Accounts/intersteller.html')
def SpiderManHomecoming(request):
    return render (request, 'Accounts/SpiderManHomecoming.html')
def eternals(request):
    return render (request, 'Accounts/eternals.html')
def TVshows(request):
    return render (request, 'Accounts/TVshows.html')
def LITTLETHINGS(request):
    return render (request, 'Accounts/LITTLETHINGS.html')
def Mismatched(request):
    return render (request, 'Accounts/Mismatched.html')
def Flames(request):
    return render (request, 'Accounts/Flames.html')
def KotaFactory(request):
    return render (request, 'Accounts/KotaFactory.html')
def Aspirants(request):
    return render (request, 'Accounts/Aspirants.html')
def contactus(request):
    return render (request, 'Accounts/contactus.html')
def Comedy(request):
    return render (request, 'Accounts/Comedy.html')
def Horror(request):
    return render (request, 'Accounts/Horror.html')
def Action(request):
    return render (request, 'Accounts/Action.html')
