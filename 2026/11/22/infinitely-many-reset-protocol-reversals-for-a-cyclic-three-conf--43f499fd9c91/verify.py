"""Reproducible tests of the cyclic-gate first-arrival formula (Python 3, numpy/scipy)."""
import cmath
import math
import numpy as np
from scipy.linalg import expm, sqrtm
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

checks = 0

def formulas(D, gamma, r, a):
    kappa = gamma * (1 - cmath.exp(2j * math.pi / 3))
    k = cmath.sqrt((r + kappa)/D)
    k0 = math.sqrt(r/D)
    TJ = (math.exp(k0*a)*(1+2*k0*(1/k).real)-1)/r
    delta = 2*k0*(cmath.exp(-(k-k0)*a)/(kappa*k)).real
    return TJ+delta, TJ, delta, k, kappa

def independent_matrix(D, gamma, r, a):
    Q=np.array([[-gamma,gamma,0],[0,-gamma,gamma],[gamma,0,-gamma]],float)
    pi=np.ones(3)/3
    K=np.asarray(sqrtm((r*np.eye(3)-Q)/D),float)
    E=expm(-K*a)
    # Position-only reset: m(x)=h+e^(-Kx)c; Neumann closed phases.
    A=np.vstack([K[[1,2],:], pi@E]); rhs=np.array([0.,0.,-1/r]); c=np.linalg.solve(A,rhs)
    z=np.ones(3)+r*E@c
    hzero=np.linalg.lstsq(np.vstack([Q,pi]),np.r_[-z,0],rcond=None)[0]
    h=hzero+(-c[0]-hzero[0])
    TP=pi@(h+E@c)
    # Joint complete reset: no-reset first-arrival transform.
    d=np.linalg.solve(np.vstack([K[[1,2],:],np.array([1.,0.,0.])]),np.array([0.,0.,1.]))
    p=pi@E@d
    TJ=(1-p)/(r*p)
    return TP,TJ

def finite_difference(D,gamma,r,a,delta=0.04,L=20):
    N=round(L/delta); dx=L/N; jreset=round(a/dx)
    assert abs(jreset*dx-a)<1e-8
    out=[]
    for joint in (False,True):
        n=3*(N+1); A=lil_matrix((n,n)); y=np.ones(n)
        for j in range(N+1):
            for s in range(3):
                i=3*j+s
                if j==0 and s==0:
                    A[i,i]=1; y[i]=0; continue
                A[i,i]+=-gamma-r
                A[i,3*j+(s+1)%3]+=gamma
                if j==0:
                    A[i,i]+=-2*D/dx**2
                    A[i,3*(j+1)+s]+=2*D/dx**2
                elif j==N:
                    A[i,i]+=-2*D/dx**2
                    A[i,3*(j-1)+s]+=2*D/dx**2
                else:
                    A[i,i]+=-2*D/dx**2
                    A[i,3*(j-1)+s]+=D/dx**2
                    A[i,3*(j+1)+s]+=D/dx**2
                if joint:
                    for t in range(3):A[i,3*jreset+t]+=r/3
                else:
                    A[i,3*jreset+s]+=r
        x=spsolve(A.tocsr(),-y)
        out.append(np.mean(x[3*jreset:3*jreset+3]))
    return out

for D in (0.4,1.,2.5):
 for gamma in (.3,1.,4.):
  for r in (.25,1.,3.):
   for a in (.01,.25,.8,1.4,2.8):
    T_P,T_J,delta,k,kappa = formulas(D,gamma,r,a)
    P2,J2=independent_matrix(D,gamma,r,a)
    assert math.isclose(T_P,P2,rel_tol=8e-9,abs_tol=1e-7),(D,gamma,r,a,T_P,P2)
    checks+=1
    assert math.isclose(T_J,J2,rel_tol=8e-9,abs_tol=1e-7)
    checks+=1
    assert math.isclose(T_P-T_J,delta,rel_tol=1e-5,abs_tol=1e-7)
    checks+=1
    assert T_J>0 and T_P>0
    checks+=1
    phase=cmath.phase(1/(kappa*k))
    assert math.pi/6 < phase < math.pi/4
    checks+=1
    v=-k.imag
    assert v>0 and k.real>math.sqrt(r/D)
    checks+=1
    root=(math.pi/2-phase)/v
    assert root>0 and abs(formulas(D,gamma,r,root)[2])<1e-12
    checks+=1
    assert formulas(D,gamma,r,root+.05/v)[2]<0
    checks+=1
    assert formulas(D,gamma,r,root+1.05*math.pi/v)[2]>0
    checks+=1
for a in (1.,5.):
 P,J=finite_difference(1.,1.,1.,a)
 PP,JJ,_,_,_=formulas(1.,1.,1.,a)
 print('FD D=gamma=r=1 distance',a,':',P,J,'exact',PP,JJ,'errors',P-PP,J-JJ)
 assert abs(P-PP) < .4
 assert abs(J-JJ) < .4
 checks+=2
 assert math.copysign(1,P-J)==math.copysign(1,PP-JJ)
 checks+=1
print('PASS',checks,'checks')
