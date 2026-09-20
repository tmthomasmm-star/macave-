# macave — application Android de gestion de cave

Version test 0.1. Sources du prototype Ma Cave.

Pour obtenir un APK compilé depuis ce dépôt : onglet **Actions** → **Android test APK** → exécution réussie → artefact **Ma-Cave-Test-APK**. Le fichier APK initial reste disponible dans la conversation du projet.

Nom provisoire. Prototype destiné à un essai personnel ; non publié sur Google Play.

## Installer et essayer

1. Transférer `Ma-Cave-Test-0.1.apk` sur le téléphone et ouvrir le fichier.
2. Si Android le demande, autoriser cette source à installer l’APK. Android 8 ou ultérieur nécessaire.
3. Ouvrir « Ma Cave · Test ». Au démarrage, la cave est vide. « Explorer une cave d’exemple » crée trois fiches fictives pour essayer les commandes.
4. Passer de Réaliste à Casiers. Toucher un casier, puis un vin : Ajouter / Retirer / Déplacer.
5. Pour revenir à une cave vide après l’exemple, Réglages → Annuler la dernière action immédiatement après sa création. Sinon retirer les bouteilles puis supprimer leurs fiches, ou repartir avec les données d’application effacées après avoir exporté ce qui doit être conservé.
6. Créer un rangement réel, puis ajouter deux ou trois vins pour un premier essai.
7. Exporter une sauvegarde dans Réglages avant toute désinstallation ou changement de téléphone.

Une fois installée, l’application fonctionne sans connexion. Aucun compte n’est nécessaire. Pas de publicité, télémétrie ni appel à une API d’IA. La permission Internet sert au chargement des composants de l’application depuis un serveur interne, limité à 127.0.0.1 ; aucun service distant n’est utilisé.

## Fonctions de cette version

- Deux vues mémorisées : rendu bois avec bouteilles et plan de casiers.
- Fond photographique personnel facultatif, avec compteurs superposés. La photo elle-même reste fixe.
- Plusieurs lieux et rangements, dimensions et capacité déclarée, types usuels, presets adaptés.
- Grille personnalisable, cases nommables, taille et position réglables en pourcentages ; ajout et retrait de cases vides.
- Agrandissement et défilement des grands rangements.
- Jusqu’à dix photos par rangement, dont une photo principale ; choix dans les fichiers ou prise de vue via l’application caméra du téléphone.
- Proposition expérimentale du nombre de lignes/colonnes à partir des séparations visibles sur la photo principale, à valider manuellement.
- Fiche par vin/millésime : photo, domaine, appellation, couleur, format, description, notes, prix unitaire facultatif, garde personnelle facultative.
- Deux photos par fiche : étiquette avant et contre-étiquette arrière, galerie ou caméra. Lecture locale en français via Tesseract. Une description simple est composée à partir des informations reconnues ; un profil rassemble couleur, cépages, alcool et mentions de dégustation présentes dans le texte. Les informations absentes restent inconnues. Tous les champs sont modifiables et les textes OCR restent consultables.
- Conseils généraux de conservation/rangement modifiables, distincts de la garde personnelle. Proposition d’emplacements selon les capacités libres et la présence du même vin ; format physique et conditions de conservation à vérifier par l’utilisateur.
- Quantités réparties dans plusieurs casiers, zone « À ranger », recherche et fiches à stock zéro conservées.
- Ajout, retrait (bue, offerte, correction), déplacement ; contrôle du stock ; avertissement de dépassement de capacité.
- Historique des 200 derniers mouvements ; annulation de la dernière modification pendant la session.
- Montants masqués par défaut dans l’accueil et les fiches ; choix explicite dans les réglages. Les prix restent accessibles en modification.
- Coût d’achat du stock restant et nombre de bouteilles dont le prix est absent, lorsque les montants sont activés.
- Enregistrement local automatique et atomique ; export/import JSON avec photos et validation avant remplacement.

## Limites importantes du prototype

- **Pas de reconstruction automatique fidèle d’une pièce à partir de dix photos.** Les photos appartiennent à un rangement et restent consultables dans sa modification. Seule la photo principale est analysée pour une suggestion de grille. Les perspectives, reflets, bouteilles et formes irrégulières peuvent fausser cette suggestion.
- La géométrie éditable est rectangulaire. Les types de rangements sont des presets et métadonnées ; les véritables compartiments triangulaires/losanges et les courbes ne sont pas reconstruits. Les dimensions déterminent les proportions, pas une capacité physique calculée.
- Le rendu bois est stylisé et n’est pas le rendu photoréaliste des maquettes. Le fond photo permet de reconnaître le meuble réel, mais les bouteilles visibles dessus sont celles de la photo ; les compteurs sont la référence du stock actuel.
- L’OCR lit les inscriptions visibles et un analyseur à règles en fait une synthèse simple. Ce n’est pas un sommelier IA ni une identification certaine : pas de catalogue de vins ni de fiche technique externe. Les arômes et le style ne sont proposés que lorsqu’ils sont mentionnés dans les textes lus. Aucune estimation de garde ni valeur de marché. Le français est la langue de lecture intégrée ; les étiquettes étrangères sont moins fiables.
- Un prix d’achat unitaire par fiche. Les différents lots acquis à des prix différents ne sont pas suivis séparément. L’utilisateur peut renseigner un prix moyen ou faire des fiches distinctes.
- Pas de synchronisation entre téléphones ni de sauvegarde cloud automatique. La désinstallation efface les données locales.
- Photos réduites à 1 400 pixels sur le grand côté. Import limité à 60 Mo. Limites de validation : 200 rangements, 500 cases par rangement, 20 000 fiches ; ces plafonds ne constituent pas une garantie de performance sur un téléphone.
- Test effectué sur moteur métier et interface Chromium, pas sur téléphone Android réel. La caméra, les sélecteurs Android, l’installation et l’OCR dans la WebView du téléphone restent à valider sur appareil.
- Chaque compilation utilise une clé de TEST locale dans tools/. Elle n’est pas publiée dans ce dépôt. Conservez-la localement pour signer vos mises à jour ; les compilations GitHub Actions génèrent une nouvelle clé et ne peuvent donc pas remplacer directement un APK signé avec une autre clé. Exportez vos données avant de désinstaller une précédente version. Une clé de production distincte sera nécessaire pour la publication.

## Petit parcours de test conseillé

- Créer 1 rangement, 3 niveaux, 4 cases ; choisir une photo.
- Ajouter un vin avec 6 bouteilles à 15 € en A1. Vérifier que le prix n’apparaît pas sur l’accueil.
- Déplacer 2 bouteilles de A1 vers A2 : le total doit rester 6.
- Retirer 1 bouteille de A2 : total 5.
- Activer les montants : achats du stock restant 75 € si ce vin est seul.
- Ajouter une note et une garde personnelle, quitter puis rouvrir l’application.
- Exporter une sauvegarde, modifier la quantité puis restaurer : retrouver les 5 bouteilles et les photos.
- Photographier les étiquettes avant et arrière : appuyer sur « Créer la fiche depuis les photos », vérifier description, profil et conseil de rangement, corriger et enregistrer.
- Ouvrir « Trouver une place disponible » depuis la fiche : choisir une case, contrôler le format et confirmer le déplacement.

## Sources et compilation

Le dossier `app` contient une activité Android Java et une interface locale HTML/CSS/JavaScript. Le moteur métier est dans `app/assets/model.js`.

Avec Java 17+ (runtime et keytool), Python 3 et une connexion pour télécharger les outils :

```sh
python3 build.py
```

Le script télécharge Android SDK Platform 35, Build Tools 35.0.0 et Eclipse ECJ 3.33.0. Les ressources OCR sont téléchargées dans des versions figées et leurs archives vérifiées par SHA-256 avant extraction. Elles sont ensuite intégrées à l’APK pour son fonctionnement hors connexion. Il produit `out/Ma-Cave-Test-0.1.apk`, vérifie sa signature et son manifeste.

Les outils téléchargés impliquent leurs propres conditions/licences, notamment celles du SDK Android. Les bibliothèques OCR sont accompagnées de leurs licences dans `app/assets/licenses`. Tesseract.js 6.0.1, Tesseract.js-core 6.0.0, modèle français Tesseract fast 4.0.0.

## Vérifications effectuées

Voir `TESTS.md`. Les tests d’interface peuvent produire des captures dans `out/`, dossier exclu du dépôt.

## Références pour les conseils généraux

Les recommandations générales sur l’obscurité, la fraîcheur et la stabilité thermique ont été vérifiées dans [How (and why) to store your wine properly — Financial Times](https://www.ft.com/content/261d0e97-c351-4f31-8ea7-3a565cb122fc). Elles ne constituent pas une recommandation particulière pour le vin identifié et ne déterminent aucune durée de garde.
