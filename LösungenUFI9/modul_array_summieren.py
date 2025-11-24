def summe(liste):
    summe_liste=0
    for i in range(0,len(liste)):
        summe_liste += liste[i]
    return summe_liste



#--------Test-------------------
if __name__=="__main__":
    print(summe([1,5,6,4,8,9,7,3,5,4,885,2]))
