def cout_even(liste):
    count_gerade=0
    for i in range(0,len(liste)):
        if liste[i]%2==0:
            count_gerade +=1
    return count_gerade


#--------Test------------
if __name__=="__main__":
    print(cout_even([0,1,5,8,7,9,6,4,3,2,5,1,8,9,544,12,6,5,4,2,8]))





#def cout_uneven(liste):
#    count_ungerade=0
#    for i in range(0,len(liste)):
#        if liste[i]%2!=0:
#            count_ungerade +=1
#    return count_ungerade