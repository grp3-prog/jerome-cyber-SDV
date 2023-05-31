#!/bin/bash

# Fonction pour vérifier si un programme est installé
program_is_installed() {
    type "$1" >/dev/null 2>&1
}

# Fonction pour mettre à jour la machine
update_machine() {
    echo "Mise à jour de la machine en cours..."
    apt-get update && apt-get upgrade -y
}

# Mise à jour de la machine
update_machine

# Vérification et installation de nmap
if ! program_is_installed "nmap"; then
    echo "nmap n'est pas installé. L'installation en cours..."
    apt-get install -y nmap
else
    echo "nmap est déjà installé."
fi

# Vérification et installation de gobuster
if ! program_is_installed "gobuster"; then
    echo "gobuster n'est pas installé. L'installation en cours..."
    apt-get install -y gobuster
else
    echo "gobuster est déjà installé."
fi

# Vérification et installation de dnsrecon
if ! program_is_installed "dnsrecon"; then
    echo "dnsrecon n'est pas installé. L'installation en cours..."
    apt-get install -y dnsrecon
else
    echo "dnsrecon est déjà installé."
fi

# Vérification de Python 3
if ! program_is_installed "python3"; then
    echo "python3 n'est pas installé. L'installation en cours..."
    apt-get install -y python3
else
    echo "python3 est déjà installé."
fi

# Vérification de pip pour Python 3
if ! program_is_installed "pip3"; then
    echo "python3-pip n'est pas installé. L'installation en cours..."
    apt-get install -y python3-pip
else
    echo "python3-pip est déjà installé."
fi

# Installation de droopescan avec pip
echo "Vérification et installation de droopescan..."
pip3 show droopescan >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "droopescan n'est pas installé. L'installation en cours..."
    pip3 install droopescan
else
    echo "droopescan est déjà installé."
fi

# Installation de aort avec pip
echo "Vérification et installation de aort..."
pip3 show aort >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "aort n'est pas installé. L'installation en cours..."
    pip3 install aort
else
    echo "aort est déjà installé."
fi
