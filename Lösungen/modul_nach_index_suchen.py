def search_for_index(liste,zahl):
    index= -1
    for i in range(0,len(liste)):
        if liste[i]==zahl:
            index=i
    return index


#--------test--------

if __name__ == "__main__":
    print(search_for_index([1,5,6,4,8,9,7,121,11,15,45,658,22],22))