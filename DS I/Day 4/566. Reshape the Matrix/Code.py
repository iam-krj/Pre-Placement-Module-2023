import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return mat if len(mat) * len (mat[0]) != r*c or len(mat) * len(mat[0])==1 else list(np.reshape(mat,(r,c)))
            
       
        