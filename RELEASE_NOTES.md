# CalcPro v3.0.0 — Release Notes

## Résumé
La version 3.0.0 apporte une refonte majeure de l'API pour harmoniser l'ensemble des modules de calcul et préparer l'intégration des fonctionnalités avancées.

## Nouveautés
- Ajout du calcul de la médiane (`mediane()`).
- Intégration de l'export des résultats en format texte (`export_resultat()`).
- Nouvelle structure pour l'API v3.

## Corrections
- Refus explicite et sécurisé des entrées `None` (levée d'exception claire).
- Correction du calcul de la moyenne sur des collections contenant une seule note.

## Breaking Changes ⚠️
- La fonction `moyenne()` a été renommée en `moyenne_notes()`.

## Guide de Migration
Mettez à jour vos appels de fonctions :
```python
# Avant (v1.x)
from calcpro import moyenne
res = moyenne([10, 20])

# Après (v3.0.0)
from calcpro import moyenne_notes
res = moyenne_notes([10, 20])