from django.core.management.base import BaseCommand
# db model
from characters.models import Postava 
import random

class Command(BaseCommand):
    help = 'Populates the database with sample D&D characters'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate data...'))

        Postava.objects.all().delete() # Smaže existující postavy, pokud chceš začít s čistou DB

        jmena = ["Aragorn", "Legolas", "Gimli", "Frodo", "Gandalf", "Boromir", "Sam", "Pipin", "Smíšek"]
        rasy = ["Člověk", "Elf", "Trpaslík"]
        tridy = ["Ranger", "Warrior", "Rogue", "Wizard", "Fighter", "Cleric", "Paladin", "Bard", "Druid", "Monk", "Warlock"]

        for i in range(10): # Vytvoří 10 postav
            postava = Postava(
                jmeno=f"{random.choice(jmena)} {i+1}",
                rasa=random.choice(rasy),
                trida=random.choice(tridy),
                uroven=random.randint(1, 20),
                zivotopis=f"Toto je automaticky generovaný životopis pro postavu číslo {i+1}.",
                sila=random.randint(3, 18) if random.choice([True, False]) else None, # Náhodně sílu nebo None
                je_aktivni=random.choice([True, False])
            )
            postava.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated data!'))