"""Independent finite diagnostics for the three-factor Hamming biharmonic kernel."""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def polys(q, u):
    return [1+3*(q-1)*u+3*(q-1)**2*u**4+(q-1)**3*u**9,
            1+(2*q-3)*u+(q-1)*(q-3)*u**4-(q-1)**2*u**9,
            1+(q-3)*u+(3-2*q)*u**4+(q-1)*u**9,
            1-3*u+3*u**4-u**9]

def lap(q):
    a = q*np.eye(q)-np.ones((q,q)); i=np.eye(q)
    return np.kron(np.kron(a,i),i)+np.kron(np.kron(i,a),i)+np.kron(np.kron(i,i),a)

count=0
for q in [2,3,4]:
    L=lap(q)
    r2=brentq(lambda u:polys(q,u)[2],0.5,0.999)
    r3=brentq(lambda u:polys(q,u)[3],0.1,0.5)
    assert r2>r3
    for u in [0.15,r3*0.9,(r2+r3)/2,(1+r2)/2,0.99]:
        t=-math.log(u)/(q*q)
        M=expm(-t*(L@L)); F=polys(q,u)
        for i in range(q**3):
            a=(i//(q*q),i//q%q,i%q)
            for j in range(q**3):
                b=(j//(q*q),j//q%q,j%q)
                k=sum(x!=y for x,y in zip(a,b))
                assert abs(M[i,j]-F[k]/q**3)<1e-10,(q,u,i,j,k,M[i,j],F[k]/q**3)
                count+=1
        value=1+2/q**3*(3*(q-1)**2*max(-F[2],0)+(q-1)**3*max(-F[3],0))
        assert abs(np.max(np.sum(np.abs(M),axis=1))-value)<1e-10
        assert abs(np.max(np.abs(M.sum(axis=1)-1)))<1e-10
print('PASS: exact spectral kernels, norms, stochasticity and ordered crossings;',count,'matrix entries')
