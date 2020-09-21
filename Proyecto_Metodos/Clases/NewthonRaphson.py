from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class NewthonRaphson():
	__error=0.0001

	def set_ecuacion(self, funcion):
		eval(funcion)
		self.__funcion=funcion
	
	def set_xi(self, xi):
		self.__xi=float(xi)

	def set_rango(self, p1,p2):
		self.__p1=float(p1)
		self.__p2=float(p2)
	
	def get_resultado(self):
		fun= lambda x: eval(self.__funcion)
		d_fun= lambda x: eval(str(sp.diff(self.__funcion)))
		while True:
			xn=self.__xi-fun(self.__xi)/d_fun(self.__xi)
			ep=np.abs(xn-self.__xi)
			self.__xi=xn
			if self.__error > ep:
				return self.__xi
				break

	
	def get_grafica_inicial(self):
		fun= lambda x: eval(self.__funcion)
		m=np.linspace(self.__p1, self.__p2)
		plt.plot(m,fun(m),label="Funcion")
		plt.plot(m,fun(m)*0)
		plt.grid()
		plt.legend()
		plt.show()
			
	def get_grafica_resultado(self):
		fun= lambda x: eval(self.__funcion)
		m=np.linspace(self.__p1, self.__p2)
		plt.plot(m,fun(m),label="Funcion")
		plt.plot(m,fun(m)*0)
		plt.plot(self.__xi,0, 'or', label='Raíz')
		plt.grid()
		plt.legend()
		plt.show()

