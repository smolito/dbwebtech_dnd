# characters/views.py

from django.shortcuts import render, get_object_or_404
from .models import Postava

def postava_list(request):
    """
    View pro zobrazení seznamu všech postav.
    """
    postavy = Postava.objects.all().order_by('jmeno') # Získání všech postav, seřazených podle jména
    context = {
        'postavy': postavy,
        'page_title': 'Seznam D&D Postav' # Příklad předání dalšího kontextu do šablony
    }
    # Renderuje šablonu 'characters/postava_list.html' s daným kontextem
    return render(request, 'characters/postava_list.html', context)

def postava_detail(request, pk):
    """
    View pro zobrazení detailu jedné postavy.
    'pk' (primary key) je ID postavy.
    """
    postava = get_object_or_404(Postava, pk=pk) # Získá postavu podle PK, nebo vrátí 404 pokud neexistuje
    context = {
        'postava': postava,
        'page_title': f"Detail Postavy: {postava.jmeno}"
    }
    # Renderuje šablonu 'characters/postava_detail.html' s daným kontextem
    return render(request, 'characters/postava_detail.html', context)

def home_page(request):
    """
    View pro domovskou stránku.
    """
    # Můžeš zde přidat nějaký dynamický obsah, např. počet postav, naposledy přidané apod.
    # Prozatím jednoduchá statická stránka.
    pocet_postav = Postava.objects.count()
    context = {
        'page_title': 'Vítejte v Přehledu D&D Postav',
        'pocet_postav': pocet_postav
    }
    return render(request, 'characters/home_page.html', context)
