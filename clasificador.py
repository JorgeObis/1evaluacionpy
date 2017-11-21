def saludador():
    x=input ("que hora es")  
    if x>=0 and x<=13:
      print " buenos dias"
    else:
     if x>13 and x<=20:
        print " buenas tardes"
     else:
        print " buenas noches"
saludador()
