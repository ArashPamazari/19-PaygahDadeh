def Check (araye):
    for i in range(len(araye)//2):
        if araye[i] != araye[-i-1]:
            return False
    return True

araye = input("enter number & press space: ")
araye = araye.split()
araye = [int(x) for x in araye] 

if Check(araye):
    print("True")
else:
    print("Wrong")
