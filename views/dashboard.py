import tkinter as tk
from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDisque
from observers.logger import LoggerFichier
from observers.alerte_cpu import Alerte_cpu

class Dashboard (tk.Tk) :
    INTERVALLE_MS = 2000
 
    def __init__(self, metriques: MetriquesSysteme):
        super().__init__()
        self.title("Monitoring système")
        self._metriques = metriques
 
        # À compléter :
        # 1. Créez les observateurs (AffichageCPU, AffichageRAM,
        #    AffichageDisque, LoggerFichier)
        self._creer_observateurs()
        #Bouton log en dessous
        self.bouton_log = tk.Button(self, text="Désactiver log", command=self._toggle_log)
        self.bouton_log.pack(pady=10)
        # 2. Abonnez-les tous au sujet
        self._abonner_observateurs()
        # 3. Démarrez le rafraîchissement
        self._rafraichir()
 
    def _creer_observateurs(self) -> None:
        self._cpu = AffichageCPU(self)
        self._ram = AffichageRAM(self)
        self._disque = AffichageDisque(self)
        self._logger = LoggerFichier("monitoring.log")
        self._alerte_cpu = Alerte_cpu(self._cpu)
 
    def _abonner_observateurs(self) -> None:
        self._metriques.abonner(self._cpu)
        self._metriques.abonner(self._ram)
        self._metriques.abonner(self._disque)
        self._metriques.abonner(self._logger)
        self._metriques.abonner(self._alerte_cpu)
 
    def _rafraichir(self) -> None:
        # À compléter :
        # Appelez actualiser_metriques() sur les métriques
        self._metriques.actualiser_metriques()
        # Planifiez le prochain appel avec self.after()
        self.after(self.INTERVALLE_MS, self._rafraichir)
    
    def _toggle_log(self) -> None:
        if self._logger in self._metriques._observateurs :
            self._metriques.desabonner(self._logger)
            self.bouton_log.config(text="Activer log")
        else :
            self._metriques.abonner(self._logger)
            self.bouton_log.config(text="Désactiver log")