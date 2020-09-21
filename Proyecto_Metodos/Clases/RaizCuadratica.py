from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class RaizCuadratica():
	
	def set_variables(self, a, b, c):
		
		self.__a=float(a)
		self.__b=float(b)
		self.__c=float(c)
				
	def get_calcular(self):
		self.det=(self.__b**2)-(4*self.__a*self.__c)
		if self.det<=0:
			x1=round((-self.__b/(2*self.__a)),2)
			return x1
		else:
			x1=round(((-self.__b+sqrt(self.det))/(2*self.__a)),2)
			x2=round(((-self.__b-sqrt(self.det))/(2*self.__a)),2)
			return x1,x2

	def get_graficar(self):
		m=np.linspace(-10,10)
		f=self.__a*m**2+self.__b*m+self.__c
		plt.plot(m,f)
		plt.plot(m,f*0)
		plt.grid()
		plt.show()
		
			