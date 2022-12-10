def points(games):
    sum=0
    for i in range(len(games)):
        b=games[i]
        if b[0]>b[2]:
            sum+=3
        elif b[0]==b[2]:
            sum+=1
        else:
            sum+=0
    return sum
pass
