def insertionSort(list1):
    for j in range(1,len(list1)):
        key=list1[j]
        i=j-1
        while(key<list1[i] and i>=0):
            list1[i+1]=list1[i]
            i-=1
        list1[i+1]=key
    print(list1)
list1=list(map(int,input("Enter the list of elements:").strip().split()))
insertionSort(list1)
