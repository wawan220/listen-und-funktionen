def summe(liste):
    summe =0
    for i in range(0, len(liste)):
        summe+=liste[i]
    return summe

#--------test--------

if __name__=="__main__":
    print(summe([1,2,5,4,8,9,6,3,7,51,12]))