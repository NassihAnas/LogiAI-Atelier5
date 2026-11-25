

\# ADR 005 — Transformer LogiAI en package Python



\- \*\*Statut :\*\* Acceptée

\- \*\*Date :\*\* 25/11/2026



\## Contexte



Initialement, LogiAI était utilisé directement depuis son dossier source. Cette organisation obligeait les développeurs à disposer de toute l'arborescence du projet pour importer le code et effectuer des prédictions.



L'objectif est de rendre LogiAI installable et réutilisable comme un package Python indépendant.



\## Décision



Nous avons choisi de transformer LogiAI en package Python en utilisant `pyproject.toml` et setuptools.



Le package est installé avec :



```bash

pip install -e ".\[api,dev]"

```



Une distribution wheel est générée avec :



```bash

python -m build

```



Une commande CLI est également exposée :



```bash

logiai-predict livraison.json

```



Les modèles et les données ne sont pas intégrés dans le wheel. Leur emplacement est configurable avec la variable d'environnement `LOGIAI\_HOME`.



\## Conséquences positives



\- Installation simplifiée avec pip.

\- Réutilisation du code dans différents projets.

\- Séparation entre le code Python et les ressources externes.

\- Possibilité de distribuer le package sous forme de wheel.

\- Utilisation de LogiAI comme une commande système.



\## Conséquences négatives



\- Les modèles et les données doivent être fournis séparément.

\- Le développeur doit configurer `LOGIAI\_HOME` si les ressources ne sont pas dans le dossier courant.

\- Les dépendances doivent être correctement déclarées dans `pyproject.toml`.



\## Vérification



\- 52 tests réussis.

\- Installation du wheel dans un environnement virtuel indépendant.

\- Prédiction réussie après configuration de `LOGIAI\_HOME`.

\- Installation du package dans Docker dans `site-packages`.



