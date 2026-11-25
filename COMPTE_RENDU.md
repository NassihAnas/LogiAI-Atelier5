# Compte rendu : tester, sécuriser et appeler l'API LogiAI

**Noms :** ............................  **Groupe :** ........

## 1. Casser son API (activité 1)
| Cas | Requête (corps ou URL) | Prévu | Obtenu |
|---|---|---|---|
| champ manquant | | | |
| valeur absurde | | | |
| texte au lieu d'un nombre | | | |
| champ en trop | | | |
| mauvaise route | | | |

- Une requête acceptée alors qu'elle devait être refusée ? Laquelle ?

## 2. Les 2 bugs (activité 2)
| Bug | Test qui l'a révélé | Comportement avant | Correction |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

- Sortie de `python -m pytest` à la fin de l'activité 2 :

## 3. La clé API (sprint 1)
- Ma fonction `verify_api_key()` (collez le code) :

| Requête | Code obtenu |
|---|---|
| `/v1/predict` sans clé | |
| `/v1/predict` fausse clé | |
| `/v1/predict` clé utilisateur | |
| `/v1/model-info` clé utilisateur | |
| `/v1/model-info` clé administrateur | |
| `/health` sans clé | |

- Preuve que `.env` n'est pas dans Git (sortie de `git status`) :

## 4. Le client web (sprint 2)
- Mon `fetch` (collez le code) :
- Ce qui s'affiche : livraison normale / pluie de 500 mm / fausse clé :
- Expérience CORS (page servie sur le port 5501) : que disent la page et la console (F12) ? Pourquoi `curl` marche-t-il quand même ?
- Où voyez-vous la clé dans F12 ?

## 5. Questions de compréhension
1. Quelle différence entre 401, 403 et 422 ?
2. Pourquoi la clé n'est-elle ni dans le code ni dans Git ?
3. Pourquoi comparer avec `compare_digest` plutôt qu'avec `==` ?
4. Pourquoi `curl` fonctionne-t-il alors que la page du port 5501 est bloquée ?
5. Pourquoi la validation faite par le navigateur ne remplace-t-elle pas celle de l'API ?

## 6. Lien de la pull request


---

# 7. Atelier 6 — Faire de LogiAI un package Python

## 7.1 Création du package

- Nom du package : `logiai`
- Version : `0.1.0`
- Outil de construction : setuptools
- Fichier de configuration : `pyproject.toml`
- Installation en mode développement :

```bash
pip install -e ".[api,dev]"
```

## 7.2 Tests automatisés

Résultat final :

```text
52 passed, 1 warning
```

Le warning concerne une dépréciation Starlette avec httpx et n'empêche pas les tests de réussir.

## 7.3 Commande CLI

Commande utilisée :

```bash
logiai-predict livraison.json
```

Résultat obtenu :

```text
Probabilité de retard : 73% (ALERTE)
```

Test d'un fichier inexistant :

```text
Erreur : fichier introuvable : fichier_inexistant.json
Code de sortie : 1
```

## 7.4 Distribution du package

Commande :

```bash
python -m build
```

Fichiers générés :

- `logiai-0.1.0.tar.gz`
- `logiai-0.1.0-py3-none-any.whl`

Le wheel contient le code Python, mais pas les dossiers `models/`, `data/` et `tests/`.

## 7.5 Simulation chez un autre développeur

Le wheel a été installé dans un environnement virtuel indépendant.

Sans `LOGIAI_HOME`, le modèle est introuvable.

Après configuration :

```powershell
$env:LOGIAI_HOME = "C:\Users\user\Desktop\logiai_Atelier4\starter2"
```

La prédiction fonctionne :

```text
Probabilité de retard : 73% (ALERTE)
```

## 7.6 Intégration Docker

Le Dockerfile installe désormais LogiAI comme un package Python.

Vérification :

```text
/usr/local/lib/python3.11/site-packages/logiai/__init__.py
```

Les ressources restent dans `/app` :

- `data/`
- `models/`

Le conteneur API est `Healthy`.

## 7.7 Décision architecturale

ADR 005 : Transformer LogiAI en package Python distribuable.

## 7.8 Conclusion personnelle

Cet atelier m'a permis de comprendre comment transformer un projet Python classique en package installable et distribuable. J'ai appris à utiliser pyproject.toml, setuptools, les fichiers wheel, les commandes CLI et la variable d'environnement LOGIAI_HOME. J'ai également compris comment intégrer un package Python dans Docker en séparant le code des données et du modèle.

