# characters/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Postava
from .forms import PostavaForm

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
    'pk' (primary key)
    """
    postava = get_object_or_404(Postava, pk=pk) # Získá postavu podle id, nebo vrátí 404 pokud neexistuje
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

def postava_create(request):
    """
    View pro vytvoření nové postavy.
    """
    if request.method == 'POST':
        # Pokud byl formulář odeslán (metoda POST)
        form = PostavaForm(request.POST)
        if form.is_valid():
            # Pokud jsou data ve formuláři validní
            postava = form.save()
            # přidat zprávu pro uživatele (Django messages framework) ? přes nějaký middleware ?
            # messages.success(request, f"Postava '{postava.jmeno}' byla úspěšně vytvořena!")
            return redirect('characters:postava_detail', pk=postava.pk) # Přesměruje na detail nově vytvořené postavy
        # else:
            # Formulář není validní, chyby se automaticky předají zpět do šablony
            # a zobrazí se u příslušných polí.
    else:
        # Pokud je to GET požadavek (první načtení stránky s formulářem)
        form = PostavaForm() # Vytvoří prázdný formulář

    context = {
        'form': form,
        'page_title': 'Vytvořit Novou Postavu'
    }
    return render(request, 'characters/postava_form.html', context)
