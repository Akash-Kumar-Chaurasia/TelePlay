from re import template
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_view.LoginView.as_view(template_name = "Accounts/login.html"), name = "login"),
    path('logout/', auth_view.LogoutView.as_view(template_name = "Accounts/index.html"), name = "logout"),
    path('signup/', views.signup, name = "signup"),

    path('bhramstra/', views.bhramstra, name="bhramstra"),
    path('search/', views.search, name="search"),
    path('privacypolicy/', views.privacypolicy, name="privacypolicy"),
    path('TermsandCondition/', views.TermsandCondition, name="TermsandCondition"),
    path('AboutUs/', views.AboutUs, name="AboutUs"),
    path('THRUSDAY/', views.THRUSDAY, name="THRUSDAY"),
    path('massmail/', views.massmail, name ='massmail'),
    path('sangchi/', views.sangchi, name="sangchi"),
    path('uri/', views.uri, name="uri"),
    path('onenineoneseven/', views.onenineoneseven, name="onenineoneseven"),
    path('Red_notice/', views.Red_notice, name="Red_notice"),
    path('black_panther/', views.black_panther, name="black_panther"),
    path('dark_knight/', views.dark_knight, name="dark_knight"),
    path('casino_royale/', views.casino_royale, name="casino_royale"),
    path('dune/', views.dune, name="dune"),
    path('captainmarvel/', views.captainmarvel, name="captainmarvel"),
    path('wonderwoman/', views.wonderwoman, name="wonderwoman"),
    path('AvengersEndgame/', views.AvengersEndgame, name="AvengersEndgame"),
    path('SavingPrivateRyan/', views.SavingPrivateRyan, name="SavingPrivateRyan"),
    path('MatrixResurrections/', views.MatrixResurrections, name="MatrixResurrections"),
    path('lotr/', views.lotr, name="lotr"),
    path('venom/', views.venom, name="venom"),
    path('intersteller/', views.intersteller, name="intersteller"),
    path('SpiderManHomecoming/', views.SpiderManHomecoming, name="SpiderManHomecoming"),
    path('eternals/', views.eternals, name="eternals"),
    path('TVshows/', views.TVshows, name="TVshows"),
    path('LITTLETHINGS/', views.LITTLETHINGS, name="LITTLETHINGS"),
    path('Mismatched/', views.Mismatched, name="Mismatched"),
    path('Flames/', views.Flames, name="Flames"),
    path('KotaFactory/', views.KotaFactory, name="KotaFactory"),
    path('Aspirants/', views.Aspirants, name="Aspirants"),
    path('contactus/', views.contactus, name="contactus"),
    path('Comedy/', views.Comedy, name="Comedy"),
    path('Horror/', views.Horror, name="Horror"),
    path('Action/', views.Action, name="Action"),
   
]