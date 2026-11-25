

\# Étude de conception — Architecture LogiAI



\## 1. Présentation



LogiAI est une application de prédiction du retard des livraisons utilisant un modèle de Machine Learning.



L'objectif de cet atelier est de transformer le projet en package Python installable et distribuable.



\## 2. Architecture du projet



Le projet est organisé en plusieurs parties :



\- `logiai/` : code source Python, API, prédiction et interface CLI.

\- `data/` : données utilisées par le projet.

\- `models/` : modèle Machine Learning et informations associées.

\- `tests/` : tests automatisés.

\- `docs/` : documentation et décisions architecturales.

\- `pyproject.toml` : configuration du package et dépendances.



\## 3. Installation du package



Le package peut être installé en mode développement avec :



```bash

pip install -e ".\[api,dev]"

```



Cette installation permet de modifier le code source sans reconstruire le package à chaque changement.



\## 4. Distribution



La commande suivante construit les distributions :



```bash

python -m build

```



Deux formats sont générés :



\- `.whl` : package Python installable avec pip.

\- `.tar.gz` : archive contenant les sources.



Le wheel contient le code Python et les métadonnées, mais pas les dossiers `data/`, `models/` et `tests/`.



\## 5. Gestion des ressources externes



Le chemin des ressources est configurable grâce à la variable d'environnement `LOGIAI\_HOME`.



Exemple sous PowerShell :



```powershell

$env:LOGIAI\_HOME = "C:\\chemin\\vers\\LogiAI"

```



Cette configuration permet de séparer le code installé des ressources nécessaires à la prédiction.



\## 6. Interface en ligne de commande



Une commande est disponible après installation :



```bash

logiai-predict livraison.json

```



Elle charge les caractéristiques de la livraison, utilise le modèle et affiche la probabilité de retard ainsi que le statut de l'alerte.



\## 7. Intégration Docker



Dans Docker, le package est installé avec pip à partir de `pyproject.toml`.



Le code est installé dans :



`/usr/local/lib/python3.11/site-packages/logiai/`



Les ressources restent dans `/app` :



\- `/app/data`

\- `/app/models`



La variable `LOGIAI\_HOME=/app` permet à l'application de retrouver ces ressources.



\## 8. Conclusion



La transformation de LogiAI en package Python facilite son installation, sa distribution et sa réutilisation.



La séparation du code, des données et du modèle rend l'architecture plus claire, modulaire et maintenable.



