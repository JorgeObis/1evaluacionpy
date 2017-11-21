def suma_cifras():
    suma=0
    n_cifras=0
    numero=input("Dime un numero:")
    while numero>10:
        cifra=numero/10
        if cifra/2==0:
             n_cifras=n_cifras+1
        numero=numero/10
    print ("Tiene",n_pares, "cifras pares")
suma_cifras()
    
