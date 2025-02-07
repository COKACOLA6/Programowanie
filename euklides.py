def NWD (a,b):
    while a!=b:
        if a > 0 and b > 0:
            if a>b:
                a= a-b
            else:
                b = b-a
        else:
            return None
    return a
    

a = int(input("podaj a:"))
b = int(input("Podaj b:"))
print("NWD",NWD(a,b))