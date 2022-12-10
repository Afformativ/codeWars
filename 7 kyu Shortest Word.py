def find_short(s):
    k=s.split()
    min=len(k[len(k)-1])
    for i in k:
        if min>len(i):
            min=len(i)
    
        
    return min 
