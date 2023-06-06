# initalize variables
a = [0, 0 ,0 ,0 ,0]
for i in range(0,len(a)):
    a[i] = int(input())
# start loop
while True:
    for i in range(0, len(a)):
        if a[i] > 255:
            a[i] = -1*a[i]
    print (a)
