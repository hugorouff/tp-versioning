# Politique de Versioning et Livraison — Équipe CalcPro

## 1. Format des versions et incrémentation
Le projet applique la norme Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`) :
- MAJOR : Modifications incompatibles avec l'API publique (Breaking Changes).
- MINOR : Ajout de fonctionnalités rétrocompatibles.
- PATCH : Corrections de bugs rétrocompatibles.

## 2. Préversions
Les préversions utilisent les suffixes `-alpha.N` (dev), `-beta.N` (validation), et `-rc.N` (Release Candidate, gel des fonctionnalités).

## 3. Typologie des tags et responsabilités
- Seuls les tags annotés (`git tag -a`) sont autorisés pour marquer une version.
- La création d'un tag de release est strictement réservée au Lead Dev ou au Release Manager.

## 4. Contrôles obligatoires avant toute release
- Execution validée de la suite de tests automatiques (CI au vert).
- Verification d'ascendance Git (`git merge-base --is-ancestor`).
- Mise à jour préalable des fichiers `README.md` et `RELEASE_NOTES.md`.

## 5. Règle d'immuabilité et correction d'un tag
- Interdiction absolue de réécrire, déplacer ou supprimer un tag publié sur `origin`.
- Si une erreur est identifiée après publication, une version PATCH supérieure doit être immédiatement publiée.

## 6. Procédure de Hotfix
Tout correctif d'urgence sur une version antérieure doit être créé sur une branche `hotfix/X.Y.Z` issue du tag concerné. Une fois tagué, le correctif est reporté sur `main` via `cherry-pick`.
```[cite: 1]

---

# 📝 Questions Q20 à Q22 (à inclure dans RAPPORT.md)

### **Q20. Règle absolue concernant les tags déjà publiés**[cite: 1]
* **Règle interdite** : Modifier, déplacer ou supprimer un tag qui a déjà été poussé sur le dépôt distant (`origin`)[cite: 1].
* **Pourquoi** : Les tags publiés sont consommés par des serveurs d'intégration continue (CI/CD), des environnements de production ou mis en cache par d'autres développeurs[cite: 1]. Déplacer un tag rompt la reproductibilité des builds, introduit des désynchronisations indétectables et casse la traçabilité des livraisons[cite: 1].

---

### **Q21. Créer le tag `v2.4.0` avec des tests au rouge "pour gagner du temps" ?**[cite: 1]
* **Non, c'est totalement proscrit.**[cite: 1]
* **Argumentation** : Un tag de release certifie qu'un incrément logiciel est stable, vérifié et prêt à être déployé[cite: 1]. Poser un tag sur du code défaillant :
  1. Rompt la confiance dans la qualité globale du dépôt[cite: 1].
  2. Risque de déclencher des déploiements automatiques en production d'une version corrompue[cite: 1].
  3. Fait perdre du temps lors des investigations ultérieures en masquant l'origine exacte des régressions[cite: 1].

---

### **Q22. Versioning adapté à un rythme de 20 publications par jour**[cite: 1]
* **Adaptabilité du SemVer manuel** : Le versioning sémantique géré manuellement à chaque commit est inadapté à ce rythme, car il crée une surcharge administrative constante et augmente le risque d'erreurs humaines[cite: 1].
* **Stratégie recommandée** :
  1. **Trunk-Based Development + CI/CD** : Intégrer les modifications en continu sur la branche principale[cite: 1].
  2. **Automatisé via Semantic Release / Conventional Commits** : Analyser automatiquement les messages de commit (`feat:`, `fix:`, `feat!:`) pour incrémenter le numéro SemVer et publier les tags sans intervention humaine[cite: 1].
  3. **Horodatage / Numéros de build pour l'interne** : Utiliser des versions internes de type `v2.4.0+build.1042` ou le SHA court pour la traçabilité continue, tout en exposant des versions lisibles pour les clients lors des jalons importants[cite: 1].