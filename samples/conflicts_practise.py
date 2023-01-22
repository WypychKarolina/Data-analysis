#!/usr/bin/python3
import math
import sys
def trojmian(a,b,c):
    lista=[]
    if a==0 and b==0 and c==0:
        x="Istnieje nieskończenie wiele rozwiązań"
    elif a==0:
        x="Istnieje 1 pierwiastek:",-c/b,"."
    else:
        delta=b**2-4*a*c
        if delta<0:
            x="Równanie nie ma rozwiązań"
        elif delta==0:
            x="Istnieje jeden pierwiastek podwojny:",-b/a,"."
        else:
            x1=(-b-math.sqrt(delta))/2*a
            lista.append(x1)
            x2=(-b+math.sqrt(delta))/2*a
            lista.append(x2)
            x="Istnieją 2 pierwiastki:",lista,"."
            
    return(x)

if __name__ == "__main__":
      print(trojmian(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])))
