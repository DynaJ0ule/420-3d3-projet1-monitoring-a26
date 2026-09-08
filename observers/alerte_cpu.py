from observers.observer import Observateur
import tkinter as tk

class Alerte_cpu (Observateur):
    
    def __init__(self, parent, seuil : float = 80.0):
        self.label_alerte = tk.Label(parent.frame_cpu, fg="red", font=("Arial", 12, "bold"))
        self.label_alerte.pack()
        self._seuil = seuil
    
    def actualiser(self, sujet):
        cpu = sujet.get_donnees()["cpu"]
        if cpu >= self._seuil:
            self.label_alerte.config(text=f"Avertissement : {self._seuil}% ou +")
        else:
            self.label_alerte.config(text="")