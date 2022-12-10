def digital_root(n):
    count = 0
    while n > 9:
        for i in str(n):
            count += int(i)
        n = count
        count = 0
    return n
