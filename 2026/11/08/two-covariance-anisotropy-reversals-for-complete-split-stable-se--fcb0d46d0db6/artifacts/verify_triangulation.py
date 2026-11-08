from fractions import Fraction as F
from itertools import product
from math import factorial
from scipy.spatial import Delaunay
import numpy as np
import sympy as s
for p,q in [(2,2),(2,3),(3,2),(3,3)]:
    V=np.array([tuple(x)+(0,)*p for x in product([0,1],repeat=q)]+[(0,)*q+tuple(int(i==j) for i in range(p)) for j in range(p)],dtype=int)
    simplices=Delaunay(V,qhull_options='QJ').simplices
    dim=p+q;tot=F(0); M=[F(0) for i in range(dim)];MM=[[F(0) for j in range(dim)] for i in range(dim)]
    n_simp=0
    for ids in simplices:
        v=V[ids]
        det=abs(int(s.Matrix((v[1:]-v[0]).T.tolist()).det()))
        if not det:continue
        wt=F(det,factorial(dim));tot+=wt;n_simp+=1
        S=[sum(int(w[i]) for w in v) for i in range(dim)]
        mu=[F(S[i],dim+1) for i in range(dim)]
        for i in range(dim):
           M[i]+=wt*mu[i]
           for j in range(dim):
             MM[i][j]+=wt*F(S[i]*S[j]+sum(int(w[i]*w[j]) for w in v),(dim+1)*(dim+2))
    M=[x/tot for x in M]
    C=[[MM[i][j]/tot-M[i]*M[j] for j in range(dim)] for i in range(dim)]
    D=dim+1
    a=F((q+1)*(q+2),12*D*(D+1));b=F(1,D*(D+1))
    var=F(p*(q+1),D*D*(D+1))
    for i in range(q):
       for j in range(q):assert C[i][j]==(a if i==j else 0)+var/4
    for i in range(p):
       for j in range(p):assert C[q+i][q+j]==(b if i==j else 0)+(var-b*p)/p**2
    for i in range(q):
       for j in range(p):assert C[i][q+j]==-var/(2*p)
    print(p,q,'volume',tot,'simplices',n_simp,'moments OK')
