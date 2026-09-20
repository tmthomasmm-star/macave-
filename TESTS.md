# Rapport de vérification — 20 septembre 2026

## Résultats automatisés

- `tests/model.test.js` : PASS. Déplacement à total constant, retraits, stock insuffisant refusé, quantités entières positives, sauvegarde JSON, validation des références de cases et prix.
- `tests/ui.test.js` : PASS dans Chromium, viewport 412 × 915. Bascule de vues et persistance, montants masqués puis activés, retrait et déplacement multi-emplacements, réduction d’un rangement occupé refusée, ajout/annotation/garde, sauvegarde et restauration, photo persistée, lecture OCR d’une étiquette synthétique avec nom et millésime 2020 retrouvés.
- `tests/edge.test.js` : PASS dans Chromium, viewport 360 × 800. Création de rangement, preset armoire, refus de 11 photos, grille 3 × 4 détectée sur image de test, échappement d’un nom ressemblant à du HTML, suppression de rangement avec transfert des neuf bouteilles vers À ranger, annulation, fond photo, absence de débordement horizontal.
- `node --check` : syntaxe JavaScript valide.
- Compilation Java et conversion DEX réussies.
- Signature APK vérifiée, schémas v2 et v3.
- Manifeste inspecté : package fr.macave.test, version 0.1.0-test, Android minimum 8 / API 26, cible API 35.

## Ce que ces tests ne démontrent pas

La reconnaissance fiable d’une vraie cave quelconque, l’OCR d’étiquettes difficiles et les performances sur une très grande collection ne sont pas établis. Pas de test sur téléphone ou émulateur Android dans cette session. Les parcours natifs caméra, sélecteur de fichiers, sauvegarde Android et cycle de vie doivent être essayés sur le téléphone de test.

Les images utilisées pour le test d’analyse et l’OCR sont synthétiques et sont incluses dans tests/. Elles vérifient l’intégration technique, pas un taux de réussite sur des photos réelles.

## Ajout recto/verso demandé pendant le développement

- `tests/profile.test.js` : PASS. Champs extraits de deux textes, description synthétique, cépages et alcool distincts, grand format reconnu, absence de style/arômes inventés quand ils ne sont pas mentionnés. Un pourcentage d’assemblage n’est pas lu comme un degré d’alcool.
- `tests/two-labels.test.js` : PASS. Deux photos synthétiques passées à l’OCR, couleur rouge, nom, millésime, Merlot et mentions de fruits rouges retrouvés ; description/profil/conseils produits ; garde laissée vide ; photos avant/arrière persistées ; proposition de place et déplacement effectués.

- Ressources embarquées : présence et égalité octet par octet de tous les fichiers d’interface, moteur de profil, OCR et dictionnaire français dans l’APK final. Dictionnaire intégré non compressé pour éviter le renommage automatique par aapt ; test recto/verso repassé après correction.
