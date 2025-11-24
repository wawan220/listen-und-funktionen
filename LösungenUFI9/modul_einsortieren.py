def sort_in(liste, zahl):
    for i in range(0,len(liste)):
        if zahl<liste[i]:
            liste.insert(i,zahl)
            return liste
    liste.append(zahl)
    return liste

#----------Test--------------
if __name__ == "__main__":
    print(sort_in([0,1,2,3,5,6,7,8,9], int(input("gebe zahl: "))))