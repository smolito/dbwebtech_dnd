# characters/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Postava
from .forms import PostavaForm
from django.contrib import messages
from collections import deque

def postava_list(request):
    """
    View pro zobrazení seznamu všech postav.
    """
    # Načtení informace o poslední akci ze session
    last_actioned_char_name = request.session.pop('last_actioned_char_name', None)
    last_action_type = request.session.pop('last_action_type', None)

    if last_actioned_char_name and last_action_type:
        messages.success(request, f"Postava '{last_actioned_char_name}' byla úspěšně {last_action_type}.")

    postavy = Postava.objects.all().order_by('jmeno')
    context = {
        'postavy': postavy,
        'page_title': 'Seznam D&D Postav'
    }
    # Renderuje šablonu 'characters/postava_list.html' s daným kontextem
    return render(request, 'characters/postava_list.html', context)

def postava_detail(request, pk):
    """
    View pro zobrazení detailu jedné postavy.
    'pk' (primary key)
    """
    postava = get_object_or_404(Postava, pk=pk) # Získá postavu podle id, nebo vrátí 404 pokud neexistuje

    # správa seznamu naposledy prohlížených postav
    recently_viewed = request.session.get('recently_viewed_characters', [])

    # data pro aktuální postavu
    current_char_info = {'id': postava.pk, 'jmeno': postava.jmeno}

    # odstranit postavu ze seznamu, pokud tam už je, abychom ji přidali na začátek
    recently_viewed = [char for char in recently_viewed if char['id'] != postava.pk]

    # přidání aktuální postavy na začátek seznamu (jako deque pro snadné přidání na začátek)
    temp_deque = deque(recently_viewed, maxlen=5) # Omezíme na 5 položek
    temp_deque.appendleft(current_char_info)
    request.session['recently_viewed_characters'] = list(temp_deque)

    context = {
        'postava': postava,
        'page_title': f"Detail Postavy: {postava.jmeno}"
    }
    return render(request, 'characters/postava_detail.html', context)

def home_page(request):
    """
    View pro domovskou stránku.
    """
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

            request.session['last_actioned_char_name'] = postava.jmeno
            request.session['last_action_type'] = 'vytvořena'
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
            updated_postava = form.save()

            request.session['last_actioned_char_name'] = updated_postava.jmeno
            request.session['last_action_type'] = 'aktualizována'
            # messages.success(request, f"Postava '{postava.jmeno}' byla úspěšně aktualizována!")
            return redirect('characters:postava_list') # zpět na seznam
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
        # jmeno_smazane_postavy = postava.jmeno
        postava.delete()
        #messages.success(request, f"Postava '{jmeno_smazane_postavy}' byla úspěšně smazána.")

        # Odstranění ze seznamu naposledy prohlížených, pokud tam byla
        recently_viewed = request.session.get('recently_viewed_characters', [])
        recently_viewed = [char for char in recently_viewed if char['id'] != pk]
        request.session['recently_viewed_characters'] = recently_viewed

        return redirect('characters:postava_list') # Přesměrujeme na seznam postav

    # Pokud je to GET požadavek, zobrazíme potvrzovací stránku
    context = {
        'postava': postava,
        'page_title': f'Smazat Postavu: {postava.jmeno}'
    }
    return render(request, 'characters/postava_confirm_delete.html', context)
