# Projet 1 — Tableau de bord de monitoring système

Application de surveillance des ressources système (CPU, RAM, disque) avec interface graphique tkinter.

## Travail à faire avant le cours de la semaine 2

1. Faites les instructions ci-dessous pour installer et configurer le projet sur votre machine locale
3. Lancez le projet et assurez-vous qu'il fonctionne correctement 
2. **Lisez attentivement le code**
3. Posez-vous les questions suivantes afin de vous préparer pour le quiz de compréhension en début de cours :
   - Quel est le nom de la ou des classes de cette application ?
   - Combien d'objets sont instanciés à partir de cette ou ces classes ? Où sont-ils instanciés ?
   - Que fait le constructeur de la classe principale ?
   - Que fait la méthode `rafraichir()` exactement ?
   - Est-ce que la méthode `rafraichir()` est appelée automatiquement ou manuellement ? Si elle est appelée automatiquement, comment est-ce que ça se fait ? Indice: faites des recherches sur la méthode `after()` de tkinter et localisez son appel dans le code.


## Installation et configuration

### Clonage du dépôt

En premier lieu, clonez ce dépôt sur votre machine locale, tel que nous l'avons fait en cours :
1. Récupérez l'URL du dépôt (bouton "Code" puis "HTTPS")
2. Dans votre terminal, tapez la commande suivante (en remplaçant `<URL>` par l'URL que vous avez copiée) :
```bash
git clone <URL>
```
3. Ouvrez VS Code et ouvrez le dossier du projet cloné.
4. Vous devrez voir les fichiers du projet dans l'explorateur de fichiers de VS Code.

### Création de l'environnement virtuel

En guise de rappel, un environnement virtuel est un espace isolé pour installer des dépendances Python. Il est recommandé d'en créer un pour ce projet afin de ne pas polluer votre installation globale de Python.

Dans le terminal de VS Code, tapez la commande suivante pour créer un environnement virtuel nommé `venv` :
```bash
python -m venv venv
```

Ensuite, activez l'environnement virtuel avec la commande appropriée pour votre système d'exploitation :
- Sur Windows :
```bash
venv\Scripts\activate
```
- Sur macOS et Linux :
```bash
source venv/bin/activate
```

Vous devriez voir le nom de l'environnement virtuel (par exemple `(venv)`) au début de la ligne de commande, indiquant que l'environnement virtuel est actif.

### Installation des dépendances

En vous assurant que l'environnement virtuel est activé (soit en voyant `(venv)` sur l'invite de commande), installez les dépendances du projet en utilisant la commande suivante :

```bash
pip install -r requirements.txt
```

## Lancement

Finalement, pour lancer l'application, assurez-vous que l'environnement virtuel est activé et exécutez la commande suivante dans le terminal de VS Code :

```bash
python app.py
```

