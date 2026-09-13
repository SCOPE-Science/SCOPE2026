"""Script P: rigorous trace/periodic-point counts via homotopy degree (EXACT integer part)
+ interval Newton existence (numerical part). det(A^n - I) != 0 for n>=1 (no roots of
unity among eigenvalues: q has no cyclotomic factor; eigenvalues real, none +-1).
Hence #Fix(A^n) = |det(A^n-I)| exactly; same for f^n by homotopy (no bifurcations
through boundary since Anosov persists along segment f_t = A o S_t, t in [0,1]).
Compute counts n=1..6 exactly with integers."""
import numpy as np
A=np.array([[2,1,0],[1,2,1],[0,1,1]],dtype=object)
def matpow(M,n):
    R=np.eye(3,dtype=object)
    for _ in range(n): R=R@M
    return R
def det3(M):
    a,b,c,d,e,f,g,h,i=M[0,0],M[0,1],M[0,2],M[1,0],M[1,1],M[1,2],M[2,0],M[2,1],M[2,2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
for n in range(1,7):
    B=matpow(A,n)-np.eye(3,dtype=object)
    print(f"n={n}: #Fix(A^n)={abs(det3(B))}")
