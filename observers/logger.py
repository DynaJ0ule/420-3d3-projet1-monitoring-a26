from observers.observer import Observateur
from datetime import datetime

class LoggerFichier(Observateur):

    def __init__(self, nom: str):
        self.nomFichier = nom
    
    def actualiser(self, sujet) -> None:
        metriques = sujet.get_donnees()
        cpu = metriques["cpu"]
        ram = metriques["ram"]
        disque = metriques["disque"]
        self._ecrire_log(cpu, ram, disque)
    
    def _ecrire_log(self, cpu: float, ram: float, disque: float) -> None:
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = (
            f"{horodatage} | "
            f"CPU: {cpu:.1f}% | "
            f"RAM: {ram:.1f}% | "
            f"Disque: {disque:.1f}%\n"
        )
        with open(self.nomFichier, 'a') as f:
            f.write(ligne)