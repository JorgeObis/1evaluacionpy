def numerospares():
    suma=0
    n_pares=0
    numero=input("Dime un numero:")
    while numero>1:
        cifra=numero%10
        if cifra%2 ==0:
            n_pares=n_pares+1
        numero=numero/10
    print "Tiene", n_pares, "cifras pares"
    
numerospares()
    
