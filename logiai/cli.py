
import argparse
import json
import sys
from pathlib import Path

from logiai.predict import Predictor


def main():
    parser = argparse.ArgumentParser(
        description="Prédire le retard d'une livraison"
    )
    parser.add_argument(
        "fichier",
        help="Chemin vers le fichier JSON de la livraison"
    )
    args = parser.parse_args()

    chemin = Path(args.fichier)

    if not chemin.exists():
        print(f"Erreur : fichier introuvable : {chemin}", file=sys.stderr)
        return 1

    try:
        features = json.loads(chemin.read_text(encoding="utf-8"))
        resultat = Predictor().predict(features)

        probabilite = resultat["probabilite_retard"]
        alerte = resultat["alerte"]

        statut = "ALERTE" if alerte else "PAS D'ALERTE"

        print(
            f"Probabilité de retard : {probabilite:.0%} ({statut})"
        )
        return 0

    except Exception as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
