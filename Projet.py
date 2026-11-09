from datetime import datetime

stock = {}
prix = {}
historique_ventes = []

chiffre_affaires = 0


# ENREGISTREMENT DES PRODUITS
print("===== ENREGISTREMENT DES PRODUITS =====")

nombre = int(input("Combien de produits voulez-vous enregistrer ? "))

for i in range(nombre):
    produit = input(f"\nNom du produit {i + 1} : ").strip()

    quantite = int(input("Quantité disponible : "))
    prix_unitaire = float(input("Prix de vente unitaire : "))

    stock[produit] = quantite
    prix[produit] = prix_unitaire


# MENU PRINCIPAL
while True:

    print("\n===== GESTION DE STOCK =====")
    print("1. Enregistrer une vente")
    print("2. Afficher le stock")
    print("3. Ajouter un produit")
    print("4. Réapprovisionner un produit")
    print("5. Historique des ventes")
    print("6. Chiffre d'affaires total")
    print("7. Chiffre d'affaires par produit")
    print("8. Quitter")

    choix = input("\nVotre choix : ")


    # ENREGISTRER UNE VENTE
    if choix == "1":

        produit = input("Produit vendu : ").strip()

        if produit in stock:

            quantite = int(input("Quantité vendue : "))

            if quantite <= 0:
                print("Quantité invalide.")

            elif quantite <= stock[produit]:

                stock[produit] -= quantite

                montant = quantite * prix[produit]
                chiffre_affaires += montant

                date_vente = datetime.now().strftime("%d/%m/%Y")
                heure_vente = datetime.now().strftime("%H:%M:%S")

                vente = {
                    "produit": produit,
                    "quantite": quantite,
                    "prix_unitaire": prix[produit],
                    "montant": montant,
                    "date": date_vente,
                    "heure": heure_vente
                }

                historique_ventes.append(vente)

                print("\nVENTE ENREGISTRÉE !")
                print("Produit :", produit)
                print("Quantité vendue :", quantite)
                print("Prix unitaire :", prix[produit], "FCFA")
                print("Montant :", montant, "FCFA")
                print("Stock restant :", stock[produit])
                print("Date :", date_vente)
                print("Heure :", heure_vente)

            else:
                print("Stock insuffisant !")
                print("Stock disponible :", stock[produit])

        else:
            print("Produit introuvable.")


    # AFFICHER LE STOCK
    elif choix == "2":

        print("\n===== STOCK DISPONIBLE =====")

        for produit, quantite in stock.items():
            print(
                produit,
                "| Quantité :", quantite,
                "| Prix :", prix[produit], "FCFA"
            )


    # AJOUTER UN PRODUIT
    elif choix == "3":

        produit = input("Nom du nouveau produit : ").strip()

        if produit in stock:
            print("Ce produit existe déjà.")

        else:
            quantite = int(input("Quantité initiale : "))
            prix_unitaire = float(input("Prix unitaire : "))

            if quantite >= 0 and prix_unitaire >= 0:
                stock[produit] = quantite
                prix[produit] = prix_unitaire

                print("Produit ajouté avec succès !")
            else:
                print("Valeurs invalides.")


    # RÉAPPROVISIONNEMENT
    elif choix == "4":

        produit = input("Produit à réapprovisionner : ").strip()

        if produit in stock:

            quantite = int(input("Quantité à ajouter : "))

            if quantite > 0:
                stock[produit] += quantite

                print("Réapprovisionnement effectué !")
                print("Nouveau stock :", stock[produit])

            else:
                print("Quantité invalide.")

        else:
            print("Produit introuvable.")


    # HISTORIQUE DES VENTES
    elif choix == "5":

        print("\n===== HISTORIQUE DES VENTES =====")

        if not historique_ventes:
            print("Aucune vente enregistrée.")

        else:
            for vente in historique_ventes:

                print("-------------------------")
                print("Produit :", vente["produit"])
                print("Quantité :", vente["quantite"])
                print("Prix unitaire :", vente["prix_unitaire"], "FCFA")
                print("Montant :", vente["montant"], "FCFA")
                print("Date :", vente["date"])
                print("Heure :", vente["heure"])


    # CHIFFRE D'AFFAIRES TOTAL
    elif choix == "6":

        print("\n===== CHIFFRE D'AFFAIRES TOTAL =====")
        print(f"Chiffre d'affaires : {chiffre_affaires:,.2f} FCFA")


    # CHIFFRE D'AFFAIRES PAR PRODUIT
    elif choix == "7":

        print("\n===== CHIFFRE D'AFFAIRES PAR PRODUIT =====")

        ca_produits = {}

        for vente in historique_ventes:

            produit = vente["produit"]

            if produit not in ca_produits:
                ca_produits[produit] = 0

            ca_produits[produit] += vente["montant"]

        for produit, montant in ca_produits.items():
            print(f"{produit} : {montant:,.2f} FCFA")


    # QUITTER
    elif choix == "8":

        print("\nMerci d'avoir utilisé notre logiciel !")
        print(f"Chiffre d'affaires final : {chiffre_affaires:,.2f} FCFA")
        break

    else:
        print("Choix invalide.")
          
