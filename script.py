import itertools
import string
import time

def brute_force_attack(target):
    # Définit les caractères possibles (lettres minuscules + chiffres)
    characters = string.ascii_lowercase + string.digits
    
    start_time = time.time()
    attempts = 0
    found = False
    
    print(f"Tentative de craquage pour : '{target}'...")
    
    # On teste des longueurs de 1 à 8 caractères
    for length in range(1, 9):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_str = "".join(guess)
            
            if guess_str == target:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"\n[+] Succès !")
                print(f"[+] Chaîne trouvée : {guess_str}")
                print(f"[+] Nombre de tentatives : {attempts}")
                print(f"[+] Temps écoulé : {elapsed_time:.4f} secondes")
                found = True
                break
        if found:
            break

# Demande la saisie à l'utilisateur
cible = input("Entrez la chaîne de caractères à trouver (max 8 caractères, minuscules/chiffres) : ")
if len(cible) > 8:
    print("La chaîne est trop longue (max 8).")
else:
    brute_force_attack(cible.lower())
