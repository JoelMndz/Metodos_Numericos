import numpy as np

class GaussSeidel():
	def set_datos(self, matrix, vector, m, n):
		self.matrix=np.array(matrix)
		self.vector=np.array(vector)
		self.x=np.zeros((int(m)))
		self.comp=np.zeros((int(m)))
		tol=0.0001
		itera=20
		error=[]
		m=int(m)
		n=int(n)


				
		k=0
		while k < itera:
			suma=0
			k=k+1
			for r in range(0,m):
				suma=0
				for c in range(0,n):
					if (c != r):
						suma=suma+self.matrix[r,c]*self.x[c]               
				self.x[r]=(self.vector[r]-suma)/self.matrix[r,r]
			del error[:]
		
		# Comprobación
			for r in range(0,m):
				suma=0
				for c in range(0,n):
					suma=suma+self.matrix[r,c]*self.x[c]    
				self.comp[r]=suma 
				dif=abs(self.comp[r]-self.vector[r])
				error.append(dif)      
			if all(i<=tol for i in error) == True:
				break

	def get_raices(self):
		return self.x