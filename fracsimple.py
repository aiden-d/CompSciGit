n = int(input("Enter numerator?: "))
d = int(input("Enter denominator?: "))
i = 2
if (n>d): small = d
if (n<d): small = n
if (n==d):
    print("1")
    quit()

while(i <= small):
    if (d/i == int(d/i) and n/i == int(n/i)):
        d = d/i
        n = n/i
        i=1
        if (n>d): small = d
        if (n<d): small = n
    i = i+1
    


n = int(n)
d = int(d)

if (d == 1):
    print(n)   
else: 
    print(n, "/",d)