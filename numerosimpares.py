def numerosimpares():
    suma=0
    n_impares=0
    numero=input("Dime un numero:")
    while numero>0:
        cifra=numero%10
        if cifra%2 ==0:
            n_impares=n_impares
        else:
            n_impares=n_impares+1
        numero=numero/10
    print "Tiene", n_impares, "cifras impares"
numerosimpares()
    
