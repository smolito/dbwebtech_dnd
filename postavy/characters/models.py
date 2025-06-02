#postavy/characters/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Postava(models.Model):
    jmeno = models.CharField(max_length=100, help_text="Jméno postavy (povinné)")
    rasa = models.CharField(max_length=50, help_text="Rasa postavy, např. Člověk, Elf, Trpaslík (povinné)")
    trida = models.CharField(max_length=50, help_text="Třída postavy, např. Válečník, Kouzelník, Tulák (povinné)")
    uroven = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        default=1,
        help_text="Úroveň postavy (1-20, povinné)"
    )
    zivotopis = models.TextField(blank=True, null=True, help_text="Krátký životopis nebo poznámky k postavě (volitelné)")
    datum_vytvoreni = models.DateTimeField(auto_now_add=True, help_text="Datum a čas vytvoření záznamu postavy")
    sila = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        blank=True,
        null=True,
        help_text="Hodnota síly postavy (1-30, volitelné)"
    )
    #jiný typ
    je_aktivni = models.BooleanField(default=True, help_text="Označuje, zda je postava aktivně používána (povinné)")

    def __str__(self):
        return f"{self.jmeno} ({self.rasa} {self.trida}, Úroveň {self.uroven})"

    class Meta:
        verbose_name = "Postava"
        verbose_name_plural = "Postavy"
        ordering = ['jmeno']