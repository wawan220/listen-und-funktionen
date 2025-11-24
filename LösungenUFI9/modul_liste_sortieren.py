def sort_array(liste):
    #count=1
    for i in range(0 ,len(liste)):
        for j in range(0,len(liste)-i-1,1):
            temp1=liste[j]
            temp2=liste[j+1]
            if temp1>temp2:
                liste[j]=temp2
                liste[j+1]=temp1            
           # print(f"durchlauf: {count} \t{liste}")
           # count+=1
    return liste


#-----------Test--------------
if __name__=="__main__":
    print(sort_array([6,5,8,7,4,22,45,69,8,7,2,3,4,788,5,44,9]))