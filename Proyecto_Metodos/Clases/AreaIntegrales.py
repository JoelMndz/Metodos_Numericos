import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class AreaIntegrales():
	def set_ecuacion(self, funcion):
		eval(funcion)
		self.__funcion=funcion
	
	def set_datos(self, lim_s, lim_i):
		self.__lim_s=float(lim_s)
		self.__lim_i=float(lim_i)

	def set_rango(self, p1,p2):
		self.__p1=float(p1)
		self.__p2=float(p2)
	
	def get_resultado(self):
		fun= lambda x: eval(self.__funcion)
		m=np.zeros([15+1])
		h=(self.__lim_s-self.__lim_i)/15
		m[0]=self.__lim_i
		m[15]=self.__lim_s
		suma=0
		for i in range(1,15):
			m[i]=m[i-1]+h
			suma+=fun(m[i])
		self.__integral=round(((h/2)*(fun(m[0])+2*suma+fun(m[15]))),2)
		return self.__integral
	
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
		n=np.linspace(self.__lim_i, self.__lim_s)
		plt.plot(m,fun(m),label="Funcion")
		plt.plot(m,fun(m)*0)
		plt.fill_between(n,fun(n),color='c',label='Área')
		plt.grid()
		plt.legend()
		plt.show()