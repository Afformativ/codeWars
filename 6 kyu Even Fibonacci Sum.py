def even_fib(m):
    a=[0,1]
    count=0
    while True:
        a.append(a[len(a)-2]+a[len(a)-1])
        if a[len(a)-1]>=m:
            a.pop()
            break
    for i in range(len(a)):
        if a[i]%2==0:
            count+=a[i]
    return count
