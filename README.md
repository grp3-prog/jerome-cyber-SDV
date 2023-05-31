
# Projet d'études

Voici la présentation d'un script de reconnaissance et de penétrestation offensive dans le cadre du projet d'études pour l'année 2022-2023 à Sup De Vinci


## Description

Le script a été fais avec deux objectifs.

- *Reconnaissance passive* : récuperer un maximum d'informations sur un domaines afin de répérer passivement des potentielles failles ou informations pouvant nous aider lors de notre pentest. 

- *RedTeam offensif* : Automatisation de plusieurs outils offensifs afin de réaliser un aperçu des vulnérabilitées machines et web. Le but est d'orchestrer un pentest automatiser à 360° black box



### Avantages

#### [+] Gestion des rapports

Un gestion des rapports des résultats a été mis en place afin de pouvoir exporter puis analyser les différentes trouvailles que le script pourra trouver le cible.

Un dossier `"resultats"` sera créer et des fichiers `".txt"` seront créés avec le nom du domaine ciblé, ce qui permettra de stocker plusieurs résultats différents
#### [+] Script évolutif

Le script à été pensé dans sa structure pour une continuité évolutive un ajout relativement simple de nouveautés ou de nouveaux outils

#### [+] Installation simple

Grâce au fichier `setup.sh` l'ensemble des applications nécessaire au script sont téléchargés de façons automatique pour une rapidité d'accès et un comfort d'utilisation. De plus le code a été documenté afin de pouvoir être récupéré et amélioré par tous.



## Installation

Voici les commandes nécessaires pour l'installation du script

```bash
  git clone https://github.com/grp3-prog/jerome-cyber-SDV
  cd jerome-cyber-SDV
  chmod +x setup.sh
  ./setup.sh
```

Voici les commandes nécessaires pour utiliser le script

```bash
  python3 script.py
```




![App Screenshot](https://github.com/grp3-prog/jerome-cyber-SDV/assets/60225256/b1e67daa-4484-4d9b-bca3-f73b14f22b44)

### Outils utilisés

![Logo](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2M1M2NhNThlNWEwNmQ1ZTE2N2I3ZjkxNDgyODBmZDE5ZjQwNmU0ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/077i6AULCXc0FKTj9s/giphy.gif)


#### Reconnaissance
| Nom | Lien     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Dnsrecon`      | https://www.kali.org/tools/dnsrecon/ | **Reconnaissance DNS** |
| `AORT`      | https://github.com/D3Ext/AORT | **All in One Recon Tool** |
| `Gobuster`      | https://github.com/OJ/gobuster | **Url and file finder**. |



#### RedTeam offensif
| Nom | Lien     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Droopescan`      | https://github.com/SamJoan/droopescan | **Web & CMS scanner** |
| `NMAP`      | https://nmap.org/ | **Scanner réseau** |
