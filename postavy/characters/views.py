# characters/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Postava
from .forms import PostavaForm
from django.contrib import messages

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
    if request.method == 'POST':
        form = PostavaForm(request.POST)
        if form.is_valid():
            postava = form.save()
            # messages.success(request, f"Postava '{postava.jmeno}' byla úspěšně vytvořena!")
            return redirect('characters:postava_detail', pk=postava.pk)
    else:
        form = PostavaForm()

    context = {
        'form': form,
        'page_title': 'Vytvořit Novou Postavu',
        'form_action_text': 'Vytvořit postavu' # Přidáno pro konzistenci
        # 'postava': None # Není nutné, pokud šablona správně testuje existenci 'postava'
    }
    return render(request, 'characters/postava_form.html', context)

def postava_update(request, pk):
    """
    View pro úpravu existující postavy.
    'pk' (primary key) je ID postavy
    """
    postava = get_object_or_404(Postava, pk=pk)

    if request.method == 'POST':
        form = PostavaForm(request.POST, instance=postava) # Předáme instanci postavy, aby formulář věděl, že upravujeme
        if form.is_valid():
            form.save() # Uloží změny do existující instance postavy
            # messages.success(request, f"Postava '{postava.jmeno}' byla úspěšně aktualizována!")
            return redirect('characters:postava_detail', pk=postava.pk)
    else:
        # Pokud je to GET požadavek (první načtení stránky s formulářem pro úpravu)
        form = PostavaForm(instance=postava) # Vytvoří formulář předvyplněný daty z existující postavy

    context = {
        'form': form,
        'postava': postava, # Přidáme postavu do kontextu pro případné použití v šabloně
        'page_title': f'Upravit Postavu: {postava.jmeno}',
        'form_action_text': 'Uložit změny' # Text pro tlačítko formuláře
    }
    return render(request, 'characters/postava_form.html', context)

def postava_delete(request, pk):
    """
    View pro smazání postavy.
    Zobrazí potvrzovací stránku před smazáním.
    'pk' (primary key) je ID postavy
    """
    postava = get_object_or_404(Postava, pk=pk)

    if request.method == 'POST':
        # Pokud uživatel potvrdil smazání (odeslal formulář metodou POST)
        jmeno_smazane_postavy = postava.jmeno # Uložíme si jméno pro zprávu
        postava.delete()
        messages.success(request, f"Postava '{jmeno_smazane_postavy}' byla úspěšně smazána.")
        return redirect('characters:postava_list') # Přesměrujeme na seznam postav

    # Pokud je to GET požadavek, zobrazíme potvrzovací stránku
    context = {
        'postava': postava,
        'page_title': f'Smazat Postavu: {postava.jmeno}'
    }
    return render(request, 'characters/postava_confirm_delete.html', context)