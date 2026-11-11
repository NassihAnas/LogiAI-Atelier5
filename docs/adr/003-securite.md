# ADR 003 : sécurité de l'API LogiAI

## Décision 1 : où transmettre la clé (en-tête, URL ou corps) ?
- Choix : l'en-tête HTTP `X-API-Key`.
- Une clé placée dans l'URL peut être conservée dans l'historique du navigateur et les journaux
  des serveurs. Dans le corps, elle est moins standard et ne convient pas à tous les appels.

## Décision 2 : quelles origines autoriser (CORS) ? Une liste précise ou « * » ?
- Choix : une liste précise, limitée aux adresses locales de développement configurées dans
  `config.ALLOWED_ORIGINS`.
- Autoriser `*` permettrait à toute origine navigateur de lire les réponses de l'API. Une liste
  précise demande d'ajouter explicitement chaque origine de confiance, mais réduit l'accès
  accidentel. CORS ne remplace pas l'authentification par clé.
