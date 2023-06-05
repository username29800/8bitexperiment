# start loop
while True:
    for i in range(0, len(a)):
        if a[i] > 255:
            a[i] = -1*a[i]
    print (a)
    break
