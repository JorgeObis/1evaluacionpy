def saludador():
    x=input ("Que haces a las?:  ")
    if (x>=6 and x<14):
        print "dormir"
    if(x>=14 and x<20):
        print "siestear "
    if((x>=20 and x<=24) or (x>=0 and x<6)):
        print "trasnochar"
saludador()
    
