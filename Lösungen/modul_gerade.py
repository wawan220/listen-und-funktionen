def count_even(list):
    even_count=0
    for i in range(0,len(list)):
        if list[i]%2==0:
            even_count+=1
    return even_count



#--------test--------

if __name__ == "__main__":
    print(count_even([1,2,5,4,6,8,9,3,12,18,66]))