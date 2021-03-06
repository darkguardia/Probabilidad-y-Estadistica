import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def ej1():
	datos = {0:18, 1:37, 2:42, 3:30, 4:13, 5:7, 6:2, 7:1}
	mean = E(datos)
	var = V(datos)/150
	print("a) un estimador insesgado es X barra. su valor es:", "%.3f"%mean)
	error = math.sqrt(var)
	print("b) desvio del estimador:", "%.3f"%error) 
	print("   error estandar estimado:", "%.3f"%error) 

def ej2():

	X = [5.9, 7.2, 7.3, 6.3, 8.1, 6.8, 7.0, 7.6, 6.8, 6.5, 7.0, 6.3, 7.9, 9.0, 8.2, 8.7, 7.8, 9.7, 7.4, 7.7]
	Y = [6.1, 5.8, 7.8, 7.1, 7.2, 9.2, 6.6, 8.3, 7.0, 8.3, 7.8, 8.1, 7.4, 8.5, 8.9, 9.8, 9.7, 14.1, 12.6, 11.2]

	e1 = E(X)
	e2 = E(Y)
	d1 = math.sqrt(V(X)/20)
	d2 = math.sqrt(V(Y)/20)
	print("a) e1 =", "%.3f"%e1)
	print("   e2 =", "%.3f"%e2)
	print("   d1 =", "%.3f"%d1)
	print("   d2 =", "%.3f"%d2)

	diff = e1 - e2
	print("b) E(X-Y) es un estimador insesgado.")
	print("   E(X-Y) =", "%.3f"%diff) 

	error = d1 + d2
	varb = error**2
	print("c) V(X-Y) =", "%.3f"%varb)
	print("    error =", "%.3f"%error)

	print("d)", "%.3f"%(d1/d2))

def ej3():
	X1, fda1, e1, v1, d1 = binomial_dist(200, 127/200)
	X2, fda2, e2, v2, d2 = binomial_dist(200, 176/200)
	prob = (E(X1) - E(X2))/200
	var = V(X1)/200**2 + V(X2)/200**2
	error = math.sqrt(var)
	print("c)valor estimado:", "%.3f"%prob)
	print("d) error estandar estimado:", error) 

def ej6():
	print("a) E(X) = integrate x*f(x) dx from -inf to inf")
	print("        = integrate θx**(θ+1) + x**(θ+1) dx from 0 to 1")
	print("        = θ/(θ+2) + 1/(θ+2) ")
	print("----------------------------")
	print("     Xb = E(X)")
	print("     Xb = (θ+1)/(θ+2)")
	print("  θ + 1 = Xb * (θ+2)")
	print("  θ + 1 = Xb*θ + 2Xb")
	print("θ- Xb*θ = 2Xb - 1")
	print("      θ = (2Xb - 1)/(1 - Xb)")
	
	Y = [0.92, 0.79, 0.9, 0.65, 0.86, 0.47, 0.73, 0.97, 0.94, 0.77] 
	e = E(Y)
	est = (2*e - 1)/(1-e)
	print("b)", "%.3f"%est)

def ej7():
	X = [0.83, 0.88, 0.88, 1.04, 1.09, 1.12, 1.29, 1.31, 1.48, 1.49, 1.59, 1.62, 1.65, 1.71, 1.71, 1.76, 1.83]
	e = E(X)
	v = V(X, est=True)
	d = math.sqrt(v)
	print("a)", "%.3f"%e)
	f, fda = normal_dist(e, v)
	print("b) la mediana de una distribución normal es igual su promedio")
	per90 = 1.37
	while integrate.quad(f, -math.inf, per90)[0] < 0.9:
		per90 += 0.01
	print("c) percentil 90 =", "%.3f"%per90)
	print("d)", "%.3f"%integrate.quad(f, -math.inf, 1.5)[0])
	print("e)", "%.3f"%d)


def ej8():
	X = [3.11, 0.64, 2.55, 2.2, 5.44, 3.42, 10.39, 8.93, 17.82, 1.30]
	print("El estimador de MV de λ es 1/Xb")
	lam = 1/E(X)
	print("b) λ =", "%.3f"%lam)
	
def ej9():
	X = [392, 376, 401, 367, 389, 362, 409, 415, 358, 375]
	e = E(X)
	v = V(X, est=True)
	d = math.sqrt(v)
	f, fda = normal_dist(e, v)

	print("a) E(X) =", "%.3f"%e)
	print("  error =", "%.3f"%d)
	per95 = e
	while integrate.quad(f, -math.inf, per95)[0] < 0.9:
		per95 += 0.01
	print("b) percentil 95 =", "%.3f"%per95)
	print("c)", "%.3f"%integrate.quad(f, -math.inf, 400)[0])
