"""Finite reproducibility checks of balanced-multipartite PQ outer ellipsoid.
Run: OPENBLAS_NUM_THREADS=1 python checks/check_pq_lowner.py
Dependencies: Python 3, NumPy, SymPy.
"""
from itertools import product
from math import sqrt
import numpy as np
import sympy as sp

r,s,p=sp.symbols('r s p', positive=True)
F=r*(r-1)/(r-2+r*p)+r*(s-1)/(1+p)-(r*s-1)/(1-p)
poly=r*(r*s-1)*p**2+(r*r*s-2*r*s+1)*p-(r-1)
assert sp.factor(F-(2*poly/((p-1)*(p+1)*(p*r+r-2))))==0
q=1/(1+(r-1)*s)
assert sp.simplify(F.subs(p,q)-2*(s-2)*(s-1)*(r*s-s+1)/(s*(r-1)*(r*s-2*s+2)*(r*s-s+2))) == 0
assert sp.factor(poly.subs(s,2).subs(p,1/(2*r-1)))==0
qD=2*(r-1)**2/(r-2+r*p)+2*r*(s-1)/(1+p)
qO=(r-2)*(r-1)/(r-2+r*p)+r*(s-1)/(1+p)+(r*s-1)/(1-p)
assert sp.factor(qD-qO-F)==0
print('SYMBOLIC_IDENTITIES_PASS')

checks=0
for R,S in product(range(3,8),range(2,7)):
    N=R*S; k=(R-1)*S; d=2*(N-1)
    # The analytic root is a positive mixture weight.
    a=R*(R*S-1); b=R*R*S-2*R*S+1
    P=2*(R-1)/(b+sqrt(b*b+4*a*(R-1)))
    assert 0<P<1
    I=np.eye(N); J=np.ones((N,N))/N; H=I-J
    A=np.array([[float(i//S!=j//S) for j in range(N)] for i in range(N)])
    C12=(P*H+(1-P)*(A/k-J))/N
    C=np.block([[H/N,C12],[C12,H/N]])
    # From the actual uniformly weighted vertices, directly reconstruct the mean and covariance.
    vertices=[]; weights=[]
    for i in range(N):
        for j in range(N):
            if i==j or i//S!=j//S:
                z=np.r_[I[i],I[j]]
                vertices.append(z)
                weights.append(P/N if i==j else (1-P)/(N*k))
    V=np.array(vertices); W=np.array(weights)
    assert abs(W.sum()-1)<1e-12
    mean=W@V
    assert np.max(abs(mean-1/N)) < 1e-12
    Y=V-mean
    C_actual=Y.T@(W[:,None]*Y)
    assert np.max(abs(C-C_actual))<2e-12
    # Pseudoinverse only removes the two constant block directions.
    Ci=np.linalg.pinv(C, rcond=1e-9)
    lev=np.einsum('ni,ij,nj->n',Y,Ci,Y)
    assert np.max(abs(lev-d))<2e-8, (R,S,np.min(lev),np.max(lev),d)
    ev=np.linalg.eigvalsh(C)
    ev=ev[ev>1e-9]
    pred=sorted(([ (R-2+R*P)/(N*(R-1))]*(R-1)
                +[(1+P)/N]*(R*(S-1))
                +[R*(1-P)/(N*(R-1))]*(R-1)
                +[(1-P)/N]*(R*(S-1))))
    assert len(ev)==d and np.max(abs(ev-pred))<1e-12
    ball2=2*(1-1/N)
    assert np.max(abs((Y**2).sum(axis=1)-ball2))<1e-12
    ratio=(R*(R-2+R*P)*(1-P)/(R-1)**2)**((R-1)/2)*(1-P*P)**(R*(S-1)/2)
    volratio=np.prod((d*ev/ball2)**0.5)
    assert abs(ratio-volratio)<1e-8
    if S==2:
        assert abs(P-1/(2*R-1))<1e-12
    else:
        assert P>1/(1+(R-1)*S)
    checks+=1
    print('FINITE_PASS',R,S,'mass',round(P,10),'volume_ratio',round(ratio,10))
print('BALANCED_MULTIPARTITE_PQ_LOEWNER_PASS cases=',checks)
