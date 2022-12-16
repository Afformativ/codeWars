def duplicate_count(text):
    text=text.upper()
    r=set(text)
    res=[]
    for i in r:
        counter=text.count(i)
        res.append(counter)
    ans=0
    for i in res:
        if i>1:
            ans+=1
    return ans
