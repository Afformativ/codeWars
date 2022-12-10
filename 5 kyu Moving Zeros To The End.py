def move_zeros(lst):
    counter=0
    arr=[]
    for i in lst:
        if i !=0:
            counter+=1
            arr.append(i)
    b=[0]*(len(lst)-counter)
    res=arr+b
        
    return res
