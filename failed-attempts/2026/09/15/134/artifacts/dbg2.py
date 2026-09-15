import numpy as np
from minres import basis_P, ract, full_matrix, offs_of, lmult, dimF
# F1=P1+P1, gen_imgs: u=(a in P0 coords), w=(c in P0 coords)
P0=basis_P(0)
u=np.zeros(5); u[P0.index('a')]=1.0
w=np.zeros(5); w[P0.index('c')]=1.0
A=full_matrix([1,1],[0],[u,w])
print("A:\n",A)
print("rank:",np.linalg.matrix_rank(A))
uu,ss,vv=np.linalg.svd(A); K=vv[np.sum(ss>1e-8):]
print("K dim:",K.shape)
F=[1,1]
JK=np.array([ract(F,m)@v for m in ['a','b','c'] for v in K])
print("rank JK:",np.linalg.matrix_rank(JK,1e-8))
print("K rows:\n",np.round(K,3))
print("JK rows:\n",np.round(JK,3))
