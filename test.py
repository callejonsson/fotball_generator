import random

match = ['Andreas', 'Olle', 'Sebbe-biceps', 'Carl', 'Orhan', 'Bertil', 'Hej', 'Daniel', 'Jonas']
match2 = []

matches_done = 0
lengh = len(match)



while matches_done < lengh-1: 
    if len(match) == 0:
        break
    else:    
        matches_done += 1
        rand = random.choice(match)
        match2.append(rand)
        match.remove(rand)
        if len(match) > 0:
            rand2 = random.choice(match)
            match2.append(rand2)
            match.remove(rand2)
            print(rand + " vs " + rand2)
        else:
            rand2 = random.choice(match2) 
            print(rand + " vs " + rand2)



#print("Ange namn for en spelare: ")
#print("Om de inte finns fler spelare. Skriv NEJ")










