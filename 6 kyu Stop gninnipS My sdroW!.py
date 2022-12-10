def spin_words(sentence):
    a=sentence.split()
    sentence1=[]
    for i in a:
        if len(i)>=5:
            sentence1.append(i[::-1])
        else:
            sentence1.append(i)
           
    return ' '.join(sentence1)
