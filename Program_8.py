a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
c = int(input("Enter Third Number"))
d = int(input("Enter Fourth Number"))
if a > b:
    if a > c:
        if a > d:
            print(a, "is Greater")

else:
    if b > c:
        if b > d:
            print(b, "is Greater")

    else:
        if c > d:
            print(c, "is Greater")
        else:
            print(d, "is Greater")
