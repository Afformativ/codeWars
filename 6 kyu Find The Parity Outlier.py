def find_outlier(a):
    for i in range(len(a)):
        if a[0]%2==0 and a[1]%2==0:
            if a[i]%2==1:
                return a[i]
        elif a[0]%2==1 and a[1]%2==1:
            if a[i]%2==0:
                return a[i]
        elif a[0]%2==1 and a[1]%2==0 and a[2]%2==1:
            return a[1]
        elif a[0]%2==0 and a[1]%2==1 and a[2]%2==1:
            return a[0]
        elif a[0]%2==1 and a[1]%2==0 and a[2]%2==0:
            return a[0]
        elif a[0]%2==0 and a[1]%2==1 and a[2]%2==0:
            return a[1]
