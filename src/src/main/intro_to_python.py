def stringLoop(matrix):
   for i in matrix:
      matString=""
      for j in i:
         matString+=(" #"+str(j))
      print(matString)
   print("\n")   
   

if __name__== "__main__":
   import numpy as np

   matrix=np.eye((3))
   matrix=matrix.astype(int)
   stringLoop(matrix)

   matrix[matrix<1]=3
   stringLoop(matrix)   
      
   matrix=matrix[:,(0,1)]
   stringLoop(matrix)