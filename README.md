# RemotePC – Télécommande de PC via navigateur

RemotePC est une application légère permettant de contrôler un ordinateur à distance depuis un téléphone ou un navigateur, sur le même réseau local. Elle fournit des commandes multimédia, le contrôle du volume, la navigation des pistes, et un joystick virtuel pour déplacer la souris.

---

Structure du projet :

MyRemote/
│
├── server.py       # Serveur Flask principal
└── static/
    └── index.html  # Interface web de la télécommande

> Il n’existe pas d’installeur automatique. L’utilisateur doit ajouter manuellement l’application à la liste des programmes à démarrer automatiquement sur Windows si nécessaire.

---

Fonctionnalités :

Contrôle multimédia
- Play / Pause
- Piste suivante / précédente
- Avance / recule rapide

Volume
- Augmenter / diminuer le volume

Souris
- Joystick virtuel pour déplacer le curseur
- Clic gauche au tap sur le joystick

QR Code dynamique
- Lorsque la combinaison Shift + Q + R est pressée sur le clavier, un QR code apparaît à l’écran pendant 30 secondes.
- Ce QR code permet d’accéder directement à l’URL du serveur depuis un téléphone ou une tablette.

---

Installation et utilisation :

1. Téléchargez ou clonez le projet sur votre PC.

2. Installer les dépendances Python :

pip install flask pyautogui keyboard qrcode pillow

> `keyboard` nécessite des privilèges administrateur pour détecter les touches globales sous Windows.

3. Lancer le serveur :

python server.py

- Le serveur écoute sur port 5111 (modifiable dans server.py).  
- L’interface web sera disponible sur : http://<IP_LOCALE>:5111  
  - Pour connaître l’IP locale, utilisez `ipconfig` sous Windows et prenez l’adresse IPv4 de votre réseau local.

4. Scanner le QR code (optionnel) :  
- Appuyez sur Shift + Q + R sur le clavier du PC pour générer le QR code.  
- Scanner le QR code avec un téléphone pour ouvrir directement l’interface.

---

Interface web (index.html) :

- Conçue pour mobile / écran vertical.  
- Dispose de boutons pour le volume, les médias, et un joystick virtuel pour la souris.  
- Compatible avec tous les navigateurs modernes (Chrome, Firefox, Edge).

---

Ajouter l’application au démarrage de Windows :

Pour que RemotePC se lance automatiquement à l’ouverture de Windows :

1. Copier server.py et le dossier static/ dans un dossier fixe sur le PC (par ex. C:\RemotePC).  
2. Créer un raccourci vers server.py ou un script de lancement Python.  
3. Placer ce raccourci dans le dossier démarrage :

C:\Users\<VotreUtilisateur>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

- Le serveur démarrera automatiquement au lancement de Windows.  
- Vous pourrez ensuite scanner le QR code depuis le téléphone pour accéder à l’interface.

> Assurez-vous que Python est configuré pour s’exécuter sans demander de confirmation (ou créez un .bat qui lance le serveur).

---

Limitations :

- Fonctionne uniquement sur le même réseau local.  
- Pour détecter la combinaison de touches et afficher le QR code, Python doit être lancé en mode administrateur sous Windows.  
- L’application n’inclut pas de mécanisme d’authentification ou de chiffrement. Ne pas l’exposer à Internet sans configuration sécurisée.

---

Conseils :

- Pour plus de confort, créez un script .bat qui lance le serveur et ajoutez-le au démarrage.  
- Pour changer le port d’écoute, modifiez la ligne :

app.run(host="0.0.0.0", port=5111)

- Le QR code dynamique facilite l’accès depuis des appareils mobiles sans saisir manuellement l’IP et le port.

---

License :

Ce projet est open-source et peut être utilisé et modifié librement.

---

Amusez-vous à piloter votre PC depuis votre téléphone ! 🚀
