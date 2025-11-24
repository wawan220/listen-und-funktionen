
def search_for_index(liste, suche):
    for i in range(0,len(liste)):
        if liste[i] == suche:
            return i
    
    return -1

            
#------------Test---------------        
if __name__ == "__main__":
    liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(search_for_index(liste, int(input("gebeZahl: "))))