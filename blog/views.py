from django.shortcuts import render
from .models import Article,bureau,motpresident,eglise
from PIL import Image
import pytesseract
import cv2

def home(request):
    list_article = Article.objects.all()
    context = {'liste_article':list_article}
    return render(request,'index.html',context)

def detail(request,id_article):
    article = Article.objects.get(id=id_article)
    return render(request,'detail.html',{"article":article})

def acceuil(request):
    lebureau = bureau.objects.all()
    lepresident = motpresident.objects.all()
    context = {'lepresident':lepresident,'lebureau':lebureau}
    return render(request,'acceuil.html',context)

def membrebureau(request):
    list_membre = bureau.objects.all()
    context = {'liste_membre':list_membre}
    return render(request,'bureau.html',context)

def left(request):
    return render(request,'left-sidebar.html')

def right(request):
    return render(request,'right-sidebar.html')

def no(request):
    return render(request,'no-sidebar.html')

def carte(request):
        # récupération des coordonnées depuis le modèle Django
    locations = eglise.objects.all()

    # création d'une liste de dictionnaires contenant les coordonnées
    coordinates = [{'lat': loc.lat, 'lng': loc.lng, 'nom': loc.nom} for loc in locations]

    # passage des coordonnées à la vue
    context = {'coordinates': coordinates}
    return render(request,'carte.html',context)