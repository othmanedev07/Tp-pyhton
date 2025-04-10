
notes={}

while True:
    try:
        taille=int(input("Taper combien d'éleves dans la class: "))
        if 1<=taille<=30:
            break
        else:
            print("Vous devez taper un nombre entre 1 et 30 :")
    except ValueError:
        print("Le nombre d'eleves doit etre un nombre entier positives")

for i in range(taille):
        while True:
            nom = input("Donnez le nom de l'élève: ").strip()
            #replace enleve les espaces et les tiré selon ce que tu as mis dans les double code
            if nom.replace(" ", "").replace("-", "").isalpha():
            #isalpha verfie si l'input entrée et un caractere non un chiffre
                break
            else:
                print("Vous devez entrer une chaine de caractéres")
            
        while True:
            try:
                note=int(input("Donnez la note de l'éleve: "))
                if 0<=note<=20:
                    notes[nom]=note
                    break
                else:
                    print("Vous devez entrer une note entre 0 et 20")
                
            
            except ValueError:
                print("Veuillez entrer une valeur positives")

print(notes)

def fonction_note_max(notes):
    max_n=max(notes.values())
    for keys  in notes.keys():
        if notes[keys] == max_n:
            return f"Le nom de la meilleure note de la classe est {keys} avec une note de {max_n}"
print(fonction_note_max(notes))


def fonction_note_min(notes):
    min_n=min(notes.values())
    for keys  in notes.keys():
        if notes[keys] == min_n:
            return f"Le nom de l'eleve qui a la note la plus mauvaise est {keys} avec une note de {min_n}"
print(fonction_note_min(notes))


def fonction_compter_scores(notes):
    dic_s={}
    dic_i={}
    for keys , values in notes.items():
        if values>10:
            dic_s[keys]=values

        elif values < 10:
            dic_i[keys] = values 
        
    if not dic_i:
        print("Aucun eleves a eu  moins de 10")
     

    return dic_s , dic_i

superieur , inferieur = fonction_compter_scores(notes)

print("Les nom d'eleves qui ont une note superieur a 10",superieur)
if inferieur:
    print("Les nom d'eleves qui ont une note inferieur a 10",inferieur)


def fonction_moyenne_classe(notes):
    for values in notes.values():
        moy= sum(notes.values()) / len(notes)
        
    return moy

moyenne=fonction_moyenne_classe(notes)
print('La moyenne géneral de la classe est: ',moyenne)


def ajouter_point(notes):
    ajoutez={}

    for keys,values in notes.items():
        nouvelle_note=values+2

        if nouvelle_note > 20:
            nouvelle_note = 20
        
        ajoutez[keys]=nouvelle_note

    return ajoutez

ajoutez=ajouter_point(notes)
print("Les nouvelles notes ajouter récament",ajoutez)

def  trier_scores(notes):
    note_c={}
    note_d={}

    for keys, value in sorted(notes.items(), key=lambda item: item[1]):
            note_c[keys]=value
    for keys, value in sorted(notes.items(), key=lambda item: item[1] , reverse=True):
            note_d[keys]=value

    return note_c , note_d
    
croissant,decroissant=trier_scores(notes)
print("Les notes par ordre croissant",decroissant)
print("Les notes par ordre décroissant",croissant)

def fonction_eleves_superieurs(notes, seuil):
    superieur=[]
    for keys,values in notes.items():
        if values>seuil:
            superieur.append(keys)
            
    if not superieur:
        print("Aucun éleves n'a dépasser le seuil")
        
    return superieur
    
seuil=18
res=fonction_eleves_superieurs(notes, seuil)
if res:
    print("Les éleves qui ont dépasser le seuil sont",res)

        


    