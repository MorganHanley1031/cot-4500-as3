import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


def determinant_of_four(matrix):
    
    matrixA=np.copy(matrix)
    matrixA=np.delete(matrixA,0,axis=0)
    matrixA=np.delete(matrixA,0,axis=1)
    val=determinant_of_three(matrixA)*matrix[0][0]

    matrixB=np.copy(matrix)
    matrixB=np.delete(matrixB,0,axis=0)
    matrixB=np.delete(matrixB,1,axis=1)
    val2=determinant_of_three(matrixB)*matrix[0][1]
    
    matrixC=np.copy(matrix)
    matrixC=np.delete(matrixC,0,axis=0)
    matrixC=np.delete(matrixC,2,axis=1)
    val3=determinant_of_three(matrixC)*matrix[0][2]
    
    matrixD=np.copy(matrix)
    matrixD=np.delete(matrixD,0,axis=0)
    matrixD=np.delete(matrixD,3,axis=1)
    val4=determinant_of_three(matrixD)*matrix[0][3]
       
    return (val-val2+val3-val4)
    
def determinant_of_three(matrix):   
    
    val1= matrix[0][0]*(matrix[1][1]*matrix[2][2]- matrix[1][2]*matrix[2][1]) 
    val2= matrix[0][1]*(matrix[1][0]*matrix[2][2]- matrix[1][2]*matrix[2][0]) 
    val3= matrix[0][2]*(matrix[1][0]*matrix[2][1]- matrix[1][1]*matrix[2][0]) 
    return val1-val2+val3

def determinant_of_two(matrix):
    val= matrix[0][0]*matrix[1][0]- matrix[0][1]*matrix[0][1]
    return val


def  positive_definite_matrix_3x3 (matrix): 
    
    val1 = matrix[0][0]
    matrix_2x2=np.delete(matrix,2,axis=0)
    matrix_2x2=np.delete(matrix_2x2,2,axis=1)
    val2 = determinant_of_two(matrix_2x2)
    val3 = determinant_of_three(matrix)
    return (val1>=0 and val2>=0 and val3>=0)  
    
def findLU(matrix):
    matrix2=np.copy(matrix)
    size: int = len(matrix[:,])
    #print(size)
    matrixL: np.array = np.zeros((size,size))
    matrixU: np.array = np.zeros((size,size))
    #print(matrixL)
    k: int
    k2: int
    matrixU[0,:]=matrix[0,:]
    
    for i in range(0, size):
         for j in range(0,size):
             if i==j: 
                 matrixL[i,j]=1
                

    for i in range(size-1,-1,-1):
    
        for j in range(0,i):
            #print(j,i,matrix[i][j],matrix[size-1-i][size-1-i],matrix[size-1-i,:], matrix[i,:])
             
            #print(i,j,i-1,size-1-j,size,"fgh",matrix[i][j],matrix[size-1-i][size-1-i])
            
            #print(matrix[j][j],matrix[i,j],"g")           
            #print(matrix[j,:],j,matrix[i,:],i)
           
            k= matrix[i][j]/matrix[j][j]
            #print(matrix[j][j],matrix[i][j])
            matrix[i,:] =(matrix[j,:]*(0-k))+ matrix[i,:]
                        

            #print(matrix[i,:],k)
            matrixL[i,j]=k
       # matrixL[i,j]=k 

    print(matrixL)
    print("\n")
    matrix = np.array(matrix, dtype=np.double) 
    print(matrix)
    
    print("\n")

def value_check(matrix,spot):
    
    store=0
    for i,num in enumerate(matrix):
       store =store+abs(num)
    
    store= store-abs(matrix[spot])

    if abs(matrix[spot])>store:
        return True
    return False

def diagonally_dominate(matrix):
    size: int = len(matrix[:,])
    for i in range(0,size-1):
        for j in range(0,size-1): 
            if i==j:
                if (value_check(matrix[i,:],i)):
                    return False
    return True
    

if __name__ == "__main__":
      
    
    A = np.array([[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]])
    B2 = np.array([[9,0,5,2,1],[3,9,1,2,1],[0,1,7,2,3],[4,2,3,12,2],[3,2,4,0,8]])
    B3 = np.array([[2,2,1],[2,3,0],[1,0,2]])

    
    print(determinant_of_four(A),"\n")
    findLU(A)
    print (diagonally_dominate(B2),"\n")
    
    print(positive_definite_matrix_3x3(B3))