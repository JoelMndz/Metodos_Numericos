import numpy as np

class Gauss():
	
	def set_datos(self, matrix, vector, m, n):
		self.matrix=np.array(matrix)
		self.vector=np.array(vector)
		self.x=np.zeros((int(m)))
		m=int(m)
		n=int(n)
		for k in range(0,m):
			for r in range(k+1,m):
				factor=(self.matrix[r,k]/self.matrix[k,k])
				self.vector[r]=self.vector[r]-(factor*self.vector[k])
				for c in range(0,n):
					self.matrix[r,c]=self.matrix[r,c]-(factor*self.matrix[k,c])


		#sustitución hacia atrás
		self.x[m-1]=self.vector[m-1]/self.matrix[m-1,m-1]
		for r in range(m-2,-1,-1):
			suma=0
			for c in range(0,n):
				suma=suma+self.matrix[r,c]*self.x[c]
			self.x[r]=(self.vector[r]-suma)/self.matrix[r,r]

	def get_matriz(self):
		return self.matrix

	def get_vector(self):
		return self.vector

	def get_x(self):
		return self.x