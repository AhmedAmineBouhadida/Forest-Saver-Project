Suijet du projet : 

--> Partie Client (une simple personne )

Le projet consiste à créer une application web utilisant le framework Django pour déclarer des zones de déforestation. 
Les utilisateurs pourront soumettre des photos de lieux déforestés et sélectionner l'emplacement exact sur une carte interactive basée sur Leaflet.js. 
# Facultatif :  Un système de reconnaissance d'image analysera automatiquement les photos pour vérifier la présence d'arbres coupés. 
Les utilisateurs recevront des notifications pour suivre l'état de leurs déclarations. 

-- > Partie Admin 

Les administrateurs auront accès à une interface de gestion avancée avec des outils de visualisation de données pour analyser les déclarations
,des règles d'automatisation pour traiter les demandes courantes, et des algorithmes de priorisation pour traiter les cas les plus urgents. 
Le projet inclura des fonctionnalités de sécurité robustes, des capacités de scalabilité, / * un chatbot d'assistance, des tutoriels interactifs,
et un système de feedback utilisateur */ .
 Les utilisateurs pourront partager leurs déclarations sur les réseaux sociaux pour sensibiliser davantage de personnes à la déforestation.
Enfin, des collaborations avec des ONG permettront de vérifier et d'agir sur les déclarations, renforçant ainsi l'impact environnemental de l'application.

___________________________________________________________________________________________

Project Steps : 

1 - La creation d'un environment avec python version 3.8 a l'aide de conda 

2 - Installation Django ..  La creation d'un projet Django 

3 - La creation de l'application homepage et configuration des settings ... 

4 - error :   File "C:\Users\LENOVO\miniconda3\envs\forest_env\lib\site-packages\django\contrib\gis\gdal\libgdal.py", line 64, in <module>
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Could not find the GDAL library (tried "gdal306", "gdal305", "gdal304", "gdal303", "gdal302", "gdal301", "gdal300", "gdal204", "gdal203", "gdal202"). Is GDAL installed? If it is, try setting GDAL_LIBRARY_PATH in your settings.

5 -  Solution in settings.py : 
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from osgeo import gdal
gdal.SetConfigOption('GDAL_DRIVER_PATH', 'C:/Users/LENOVO/Downloads/GDAL-3.4.3-cp38-cp38-win_amd64.whl')



6 - Note :  css files + js files + images files are called static files in Django because they are static the always stay the same 

7-la creation d'un admin Django  :  python manage.py createsuperuser

8 - Mon admin : username : admin 
		password :  admin1234


9 - J'ai fait la class superviseur et ensuite je doit met ce code : 
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models.supervisor import Supervisor

class SupervisorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            form.add_error(None, e.message)

admin.site.register(Supervisor, SupervisorAdmin)

Pour que je puisse faire la migration 


___________________________________________________________________________________________

Phase de login avec google et facebook ..  : 

1 - google : vaster le site pour prendre un api :  console.cloud.google.com

_____________________________________________________________________________________________

*  Remarques Django en stockage des photo ( confusion avec la BD )  : 

En Django, lorsque vous stockez une image, elle n'est pas directement enregistrée dans la base de données. Au lieu de cela, Django stocke le chemin relatif du fichier image dans la base de données et l'image elle-même est stockée dans le système de fichiers du serveur. Cela signifie que lorsque vous voyez une entrée comme images/node_1_4TgujOJ.jpg dans la base de données, c'est le chemin relatif à l'image stockée sur le serveur.
