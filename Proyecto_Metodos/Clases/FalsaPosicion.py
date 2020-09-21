import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class FalsaPosicion():
	__error=0.0001

	def set_ecuacion(self, funcion):
		eval(funcion)
		self.__funcion=funcion
	
	def set_x0_delta(self, x0, delta):
		self.__x0=float(x0)
		self.__d=float(delta)

	def set_rango(self, p1,p2):
		self.__p1=float(p1)
		self.__p2=float(p2)
	
	def get_resultado(self):
		fun= lambda x: eval(self.__funcion)
		
		if fun(self.__x0) >= 0:
			while True:
				xn=self.__x0+self.__d
				if fun(xn) < 0:
					self.__d=self.__d/10
				if abs(self.__x0-xn)<self.__error:
					return (self.__x0+xn)/2
					break
				self.__x0=self.__x0+self.__d               
		if fun(self.__x0) < 0:
			while True:
				xn=self.__x0+self.__d
				if fun(xn) > 0:
					self.__d=self.__d/10
				if abs(self.__x0-xn)<self.__error:
					return (self.__x0+xn)/2
					break
				self.__x0=self.__x0+self.__d 
	
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
		plt.plot(self.get_resultado(),0, 'or', label='Raíz')
		plt.grid()
		plt.legend()
		plt.show()

# x**3-30*x**2+2552