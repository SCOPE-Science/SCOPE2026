import numpy as np
from finres import basis_P, actJ, offs_of, ARROWS, lmult
F=[0]; d=len(basis_P(0))
M=np.zeros((1,d)); M[0,0]=1.0
u,ss,vv=np.linalg.svd(M); K=vv[np.sum(ss>1e-8):].copy()
print("K0 shape:",K.shape)
JK=np.array([actJ(F,m)@v for m in ARROWS for v in K])
print("rank K0:",np.linalg.matrix_rank(K,1e-8),"rank JK0:",np.linalg.matrix_rank(JK,1e-8))
print("JK0 rows:")
print(np.round(JK,2))
