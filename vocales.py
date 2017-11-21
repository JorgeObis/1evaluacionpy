def vocales():
    palabra= raw_input("Dime una palabra:")
    vocales=0
    for cont in range(1,len(palabra),1):
        if palabra[cont]=="a" or palabra[cont]=="A" or palabra[cont]=="e" or palabra[cont]=="E":
            vocales=vocales+1
        print "La palabra",palabra,"tiene",cont,"letras"
    print "de las cuales",vocales,"son vocales y",cont(vocales),"son consonantes"
vocales()

