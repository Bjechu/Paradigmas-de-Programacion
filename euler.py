#==============================================================================
# Algoritmo I
#==============================================================================
# Serie exponencial
# Factorización de x
# Negativos con función inversa
# Con el polinomio factorizado corre mejor (este programa es el ejemplo bueno)
# e**x = 1+x(1+(x/2)+(1+(x/3)+(1+(x/4)+...)))
#==============================================================================
n = 200     #Iteraciones
x = 1.0     #Valor de X
flag = False
if n<0:
    flag = True
    x = -x
s = 1.0
for i in range(n,0,-1):
    s *= x/float(i)
    s += 1.0
if flag == True:
    s = 1/s
print(s)
