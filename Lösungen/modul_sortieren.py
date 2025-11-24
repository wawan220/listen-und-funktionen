def sort_list(list):

    for i in range(0,len(list),1):
        for j in range(0, len(list) - i - 1, 1):
            temp1=list[j]
            temp2=list[j+1]
            if temp1>temp2:
                list[j]=temp2
                list[j+1]=temp1

    return list



#--------test--------

if __name__=="__main__":
    print(sort_list([1,5,9,8,7,3,4,6,8,5,2,31,15,24,22,1,]))