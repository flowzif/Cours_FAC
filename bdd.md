# Schemas des BDD

## Cours

* ID "Primary key"
* nom cours
* createur du cours "Foreign key User"
* url dossier des fichiers (ID_nomcours/)
* matiere "Foreign key Matiere"
* type (td/tp/cm/annexe/fichederevision)
* visibilite : all/private

## Matière

* ID matiere "Primary key"
* nom matière "Unique"

## Utilisateur

* EXTENSION DE DJANGO USER
* liste de matiere
* liste de cours
* liste d'amis

## Annonce

* ID annonce "Primary key"
* titre
* createur Annonce "Foreign key user"
* url dossier des fichiers ID_titre
