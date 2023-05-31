import os
import subprocess
from tqdm import tqdm



os.system('clear')


#Fonction de démarrage qui va demander des choix à l'utilisateur et lancer les fonctions correspondantes aux réponses
def demarrage():
    os.system('clear')
    print("\033[1mQuelle mode voulez-vous choisir ?\033[0m") 
    print("1. \033[91mReconnaissance passive\033[0m")  
    print("2. \033[92mRedteam offensif\033[0m")
    print("3. \033[93mQuitter\033[0m")  

    while True:
        choix = input("\nVotre choix (1, 2 ou 3) : ")
        if choix == "1":
            os.system('clear')
            print("\033[91m[+] Initialisation de la reconnaissance passive...\033[0m")
            verifier_et_creer_repertoire()
            reconnaissance()
            break
        elif choix == "2":
            os.system('clear')
            print("\033[92m[+] Activation du mode Redteam offensif...\033[0m")
            verifier_et_creer_repertoire()
            redteam()
            break
        elif choix == "3":
            exit()
        else:
            os.system('clear')
            print("\033[91m[!] Choix invalide. Veuillez sélectionner 1, 2 ou 3.\033[0m")

#Fonction qui ajoute https://www. au lien si jamais la réponse de l'utilisateur n'est pas complète
def ajouter_https_www(domaine):
    if domaine.startswith("https://www"):
        return domaine
    elif domaine.startswith("https://"):
        return "https://www." + domaine[8:]
    elif domaine.startswith("www"):
        return "https://" + domaine
    else:
        return "https://www." + domaine

#La fonction va demander le domaine cible à l'utilisateur et créer un dossier de résultats pour stockés les résultats
def verifier_et_creer_repertoire():
    global domaine
    domaine = input("Indiquer le nom de domaine :")
    repertoire = "resultats"
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)
    else:
        pass


#La fonction reconnaissance va regrouper trois outils qui vont fonctionner de manière 100% automatiser et s'embriquer les uns aux autres
def reconnaissance():
    try:
        with tqdm(total=2, desc="Reconnaissance passive") as pbar:

            # Scan DNS
            pbar.set_description("Scan des enregistrements dns en cours")
            dns_fichier = 'resultats/dns-'+domaine+'.txt'
            with open(dns_fichier, 'w') as f:
                try:
                    commande_dns = ["dnsrecon", "-d", domaine]
                    dns_recon_lancement = subprocess.run(commande_dns, text=True, check=True, stdout=f)
                except:
                    print("Un problème avec DNS RECON")
            pbar.update(1)
            
            # Scan AORT
            pbar.set_description("Scan des sous-domaines en cours ")
            try : 
                commande_aort = ["aort", "-d", domaine, '-o', 'resultats/subdomains.txt']
                aort_lancement = subprocess.run(commande_aort, text=True, check=True, stdout=subprocess.DEVNULL)
            except:
                print("Un problème avec le module AORT, réessayer avec un nom de domaine ex : google.com")
            pbar.update(1)

            # Scan GOBUSTER
            pbar.set_description("Scan GoBuster en cours ")
            gobuster_fichier = 'resultats/gobuster-'+domaine+'.txt'
            with open(gobuster_fichier, 'w') as f:
                try : 
                    commande_gobuster = ["gobuster", "dir",'-u',ajouter_https_www(domaine), '-w','modules/wordlist.txt']
                    gobuster_lancement = subprocess.run(commande_gobuster, text=True, check=True, stdout=f)
                except:
                    print("Un problème avec le module Gobuster")
            pbar.update(1)

    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'exécution de la commande :", e.cmd)
    except OSError:
        print("Erreur lors de l'exécution de la commande : Commande introuvable")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

    print("Les résultats sont stockés dans ; \n")
    print('- resultats/dns-'+domaine+".txt")
    print('- resultats/subdomains-'+domaine+".txt")
    print('- resultats/gobuster-'+domaine+".txt")

    while True:
        print("\nVoulez-vous lire les résultats en console ?")
        print("Choisissez parmi les options suivantes:\n")
        print("1 - Scan DNS")
        print("2 - Scan des sous domaines")
        print("3 - Scan gobuster")
        print("4 - Quitter")
        option = input("Votre choix (1/2/3/4): ")
            
        if option == "1":
            os.system('clear')
            print("Voici le rapport concernant le scan DNS\n")
            with open(dns_fichier,'r+') as f:
                data_dns = f.read()
                print(data_dns)
        elif option == "2":
            os.system('clear')
            print("Voici le rapport concernant le scan des sous-domaines\n")
            with open("resultats/subdomains.txt",'r+') as f:
                data_subdomains = f.read()
                print(data_subdomains)
        elif option == "3":
            os.system('clear')
            print("Voici le rapport concernant le scan GoBuster\n")
            with open(gobuster_fichier,'r+') as f:
                data_gobuster = f.read()
                print(data_gobuster)
        elif option == "4":
            print("Au revoir")
            break
        else:
            print("Option invalide. Veuillez choisir parmi les options proposées.")


def redteam():
        #PRESENTATION FAIRE DROOPSCAN POUR MONTRER LES ENUMRATIONS
        try:
            with tqdm(total=2, desc="REDTEAM") as pbar:
                # Scan CMS
                pbar.set_description("Vérification CMS")
                cms_fichier = 'resultats/cms-'+domaine+'.txt'
                with open('resultats/cms-'+domaine+".txt", 'w') as f:
                    try:
                        commande_cms = ["droopescan", "scan",'--url',ajouter_https_www(domaine)]
                        cms_lancement = subprocess.run(commande_cms, text=True, check=True, stdout=f)
                    except:
                        print("Un problème avec le CMS checker")
                pbar.update(1)

            with tqdm(total=2, desc="REDTEAM") as pbar:
                # Scan NMAP
                pbar.set_description("Scan Réseau")
                try:
                    nmap_fichier = 'resultats/scan_nmap-'+domaine+'.txt'
                    commande_nmap = ["nmap", "--script=exploit",'-sV','-sC',domaine,'-o','resultats/scan_nmap-'+domaine+'.txt']
                    nnmap_lancement = subprocess.run(commande_nmap, text=True, check=True,stdout=subprocess.DEVNULL)

                except:
                        print("Un problème avec Nmap")
                pbar.update(1)

        except subprocess.CalledProcessError as e:
            print("Erreur lors de l'exécution de la commande :", e.cmd)
        except OSError:
            print("Erreur lors de l'exécution de la commande : Commande introuvable")
        except Exception as e:
            print("Une erreur s'est produite :", str(e))

        print("Les résultats sont stockés dans ; \n")
        print('- resultats/cms-'+domaine+".txt")
        print('- resultats/scan_nmap.txt-'+domaine+".txt")

        
        while True:
            print("\nVoulez-vous lire les résultats en console ?")
            print("Choisissez parmi les options suivantes:\n")
            print("1 - Scan WEB (CMS)")
            print("2 - Scan machine nmap, axé vulnérabilitées")
            print("4 - Quitter")
            option = input("Votre choix (1/2/3): ")
            
            if option == "1":
                os.system('clear')
                print("Voici le rapport concernant le scan CMS\n")
                with open(cms_fichier,'r+') as f:
                    data_cms = f.read()
                    print(data_cms)
            elif option == "2":
                os.system('clear')
                print("Voici le rapport concernant le scan NMAP\n")
                with open(nmap_fichier,'r+') as f:
                    data_nmap = f.read()
                    print(data_nmap)
            elif option == "3":
                print("Au revoir")
                break
            else:
                print("Option invalide. Veuillez choisir parmi les options proposées.")




demarrage()





