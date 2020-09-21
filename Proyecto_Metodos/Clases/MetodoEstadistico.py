import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class MetodoEstadistico():
	
	def set_datos(self, eje_x, eje_y):
		self._x=eje_x.split(',')
		self._y=eje_y.split(',')
		# if len(_x)!=len(_y):
		# 	raise ValueError
		for i in range(len(self._x)):
			self._x[i]=float(self._x[i].strip())
		for i in range(len(self._y)):
			self._y[i]=float(self._y[i].strip())
		n=0
		x_2=0
		x_3=0
		x_4=0
		xy=0
		x_2y=0
		y_=0
		x_=0

		for i in range(len(self._x)):
			n+=1
			x_2+=self._x[i]**2
			x_3+=self._x[i]**3
			x_4+=self._x[i]**4
			xy+=self._x[i]*self._y[i]
			x_2y+=self._x[i]**2*self._y[i]
			y_+=self._y[i]
			x_+=self._x[i]
			
		# Ingreso los valores de la ecuación en la matriz  
		self.a=np.array([[n,x_,x_2],[x_,x_2,x_3],[x_2,x_3,x_4]])
		self.b=np.array([y_,xy,x_2y])
		# resulvemos la ecuacion
		resultado=np.linalg.solve(self.a,self.b)
		# Resultados esperados
		self.x1=round(resultado[0],2)
		self.x2=round(resultado[1],2)
		self.x3=round(resultado[2],2)

		self._a=np.array([[n,x_],[x_,x_2]])
		self._b=np.array([y_,xy])
		# resulvemos la ecuacion
		_resultado=np.linalg.solve(self._a,self._b)
		# Resultados esperados
		self._x1=round(_resultado[0],2)
		self._x2=round(_resultado[1],2)

	def set_rango(self, p1,p2):
		self.__p1=float(p1)
		self.__p2=float(p2)
	
	def set_aproximacion(self, aproximacion):
		if aproximacion=='x':
			self.__aprox=eval(aproximacion)
		else:
			self.__aprox=float(aproximacion)

	def get_aprox_lin(self):
		funcion=lambda x: self._x2*x + self._x1
		return funcion(self.__aprox)

	def get_aprox_cuad(self):
		funcion=lambda x: self.x3*x**2 + self.x2*x + self.x1
		return funcion(self.__aprox)

	def get_grafica_lineal(self):
		funcion=lambda x: self._x2*x + self._x1
		m=np.linspace(self.__p1, self.__p2)
		plt.plot(self._x,self._y,'o',label='Datos',color='red')
		plt.plot(m,funcion(m),label='Función lineal')
		plt.plot(m,funcion(m)*0)
		plt.grid()
		plt.legend()
		plt.show()

	def get_grafica_cuadratica(self):
		funcion=lambda x: self.x3*x**2 + self.x2*x + self.x1
		m=np.linspace(self.__p1, self.__p2)
		plt.plot(self._x,self._y,'o',label='Datos',color='red')
		plt.plot(m,funcion(m),label='Función cuadrática')
		plt.plot(m,funcion(m)*0)
		plt.grid()
		plt.legend()
		plt.show()
		
