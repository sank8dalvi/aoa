def insertionSort(list1):
    for j in range(1,len(list1)):
        key=list1[j]
        i=j-1
        while(key<list1[i] and i>=0):
            list1[i+1]=list1[i]
            i-=1
        list1[i+1]=key
    print(list1)
def selectionSort(list1):
    for i in range(len(list1)):
        j=i
        for k in range(i+1,len(list1)):
            if(list1[j]>list1[k]):
                j=k
        list1[i],list1[j] = list1[j],list1[i] 
    print(list1)
list1=list(map(int,input("Enter the list of elements:").strip().split()))
#insertionSort(list1)
#selectionSort(list1)
