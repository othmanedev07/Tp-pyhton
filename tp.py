temperatures={}

while True:
    try:
        n=int(input("Donner un nombre jour: "))
        if 1< n <7:

            break
    except ValueError:
        print(" Il faut donnez un nombre entier covenable : ")
  
for i in range(n):
    while True:
        nom_j=input("Donnez le nom du jour: ")
        Jours=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
        if nom_j.lower() in  Jours:
            break
    while True:
        try:
             tem=float(input("Quelle est la température du jour: "))
             if -100<tem<100:
                temperatures[nom_j]=tem
             break
        except ValueError:
            print("Une valeur float")

    
for keys ,value in temperatures.items():
    print(f'{keys};{value}')

def max_t(tem):
    max_T=max(tem.values())
    for key in tem.keys():
        if tem[key]==max_T:
            return f"{key}:{max_T}" 
print("max")
print("La temperature maximal est ",max_t(temperatures))

def min_t(tem):
    min_t=min(tem.values())
    for key in tem.keys():
        if tem[key]==min_t:
            return f"{key}:{min_t}" 
print("min")
print("La temperature minimal est ",min_t(temperatures))

def compter_temperatures(temperatures):
        dict_p={}
        dict_n={}

        for keys ,value in temperatures.items():
            if value<0:
                dict_n[keys]=value
            else:
                dict_p[keys]=value

        return dict_n , dict_p
 

negatives,positives  = compter_temperatures(temperatures)
print("Températures positives  :", positives)
print("Températures négatives :", negatives)

def temperature_moyenne(temperatures):
    try:
        temperatureM=[]
        for keys, value in temperatures.items():
            if 10 < value < 15:
                temperatureM.append(value)

        moyenne = sum(temperatureM) / len(temperatureM)
        return f"La température moyenne entre 10 et 15°C est : {moyenne:.2f}°C"

    except ZeroDivisionError:
        print("La division avec 0 est impossible ")
     
resultat = temperature_moyenne(temperatures)
print(resultat)
        
def max_t(tem):
    max_temp = max(tem.values())  # Cherche la température la plus haute
    for jour in tem:
        if tem[jour] == max_temp:
            return jour  


def min_t(tem):
    min_temp = min(tem.values()) 
    for jour in tem:
        if tem[jour] == min_temp:
            return jour  
        
print("Le jour le plus chaud est :", max_t(temperatures))
print("Le jour le plus froid est :", min_t(temperatures))


def convertir_fahrenheit(temperatures):
    fahrenheit={}
    for keys, value in temperatures.items():
        f=(value*9/5)+32
        fahrenheit[keys]=f
    return fahrenheit

res=convertir_fahrenheit(temperatures)
print(res)

def trier_temperatures(temperatures):
    croissant={}
    decroissant={}
    for keys, value in sorted(temperatures.items(), key=lambda item: item[1]):
                croissant[keys]=value
    for keys, value in sorted(temperatures.items(), key=lambda item: item[1] , reverse=True):
                decroissant[keys]=value

    return decroissant , croissant
    
croissant,decroissant=trier_temperatures(temperatures)
print("Les températures par ordre croissant",croissant)
print("Les températures par ordre décroissant",decroissant)

def jours_superieurs(temperatures,seuil):
        jours=[]
        for keys, value in temperatures.items():
            if value>seuil:
                 jours.append(keys)
        return jours
            
seuil=30
resultat=jours_superieurs(temperatures,seuil)
print("C'est le jour qui a pu dépasser le seuil",resultat)