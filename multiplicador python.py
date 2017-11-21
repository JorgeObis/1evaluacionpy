def multiplicador():
    n=input("Dime que tabla quieres que escriba: ")
    print "TABLA DEL",n
    for cont in range(1,10000,1):
        print n,"x",cont,"=",n*cont
multiplicador()

            


