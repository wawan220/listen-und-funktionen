def add_and_sort(liste, zahl):
    for i in range(0,len(liste)):
        if zahl<liste[i]:
            liste.insert(i,zahl)
            return liste
    liste.append(zahl)
    return liste
  



#--------test--------

if __name__=="__main__":
    print(add_and_sort([1,2,3,5,6,7,8,9],4))