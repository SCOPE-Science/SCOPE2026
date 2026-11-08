"""Standalone checks for the near-full Gaussian indefinite Nystrom residual law.
Only standard Python plus sympy, mpmath and numpy are used.
Scientific proof is given in RESULT.md; these checks test algebra and distribution formulas.
"""
from fractions import Fraction
import math
import random
import sympy as sp
import mpmath as mp
import numpy as np

n_checks=0
rng=random.Random(50635)
for n in range(2,8):
    for trial in range(55):
        entries=[sp.Rational(rng.randint(1,7),rng.randint(1,6)) if i%2==0 else -sp.Rational(rng.randint(1,7),rng.randint(1,6)) for i in range(n)]
        A=sp.diag(*entries)
        X=sp.Matrix(n,n-1,[rng.randint(-3,3) for _ in range(n*(n-1))])
        if X.rank()!=n-1:continue
        W=X.T*A*X
        if W.det()==0:continue
        E=A-A*X*W.inv()*X.T*A
        # A null vector of the columns of X is a normal to the sketch subspace.
        null=X.T.nullspace()[0]
        q=(null.T*A.inv()*null)[0]
        RHS=null*null.T/q
        assert E==RHS
        assert E.rank()==1
        n_checks+=2

mp.mp.dps=65
for n in range(2,18):
    for r in range(1,n):
        s=n-r
        a=mp.mpf(2);b=mp.mpf(3)
        t0=a/(a+b)
        aa=mp.mpf(r)/2;bb=mp.mpf(s)/2
        beta=mp.beta(aa,bb)
        density=t0**(aa-1)*(1-t0)**(bb-1)/beta
        c=2*a*b/(a+b)*density
        for x in [mp.mpf(10000),mp.mpf(1000000)]:
            lo=(a-a*b/x)/(a+b)
            hi=(a+a*b/x)/(a+b)
            tail=mp.betainc(aa,bb,0,hi,regularized=True)-mp.betainc(aa,bb,0,lo,regularized=True)
            assert abs(tail*x/c-1)<mp.mpf('0.0004')
            n_checks+=1

# Two-dimensional arcsine simplification at equal magnitudes.
for x in [mp.mpf(3),mp.mpf(4),mp.mpf(10),mp.mpf(100)]:
    lo=(1-1/x)/2;hi=(1+1/x)/2
    cdf=mp.betainc(mp.mpf('0.5'),mp.mpf('0.5'),lo,hi,regularized=True)
    assert abs(cdf-2/mp.pi*mp.asin(1/x))<mp.mpf('1e-55')
    n_checks+=1

# In a concrete non-symmetric spectrum, the residual is rank one and the norm identity holds.
np_rng=np.random.default_rng(20261105)
for n,r,s,a,b in [(3,1,2,2.,1.),(5,2,3,3.,2.),(7,5,2,1.,4.)]:
    A=np.diag([a]*r+[-b]*s)
    for j in range(60):
        X=np_rng.standard_normal((n,n-1))
        W=X.T@A@X
        if abs(np.linalg.det(W))<1e-8:continue
        E=A-A@X@np.linalg.solve(W,X.T@A)
        u=np.linalg.svd(X.T,full_matrices=True)[2][-1]
        expected=np.outer(u,u)/(u@np.linalg.solve(A,u))
        assert np.allclose(E,expected,atol=1e-8,rtol=1e-8)
        assert abs(np.linalg.norm(E,'fro')-1/abs(u@np.linalg.solve(A,u)))<1e-7
        n_checks+=2


# Schur-update identity for every sketch size, across mixed-sign nonsingular spectra.
for n in range(3,8):
    A=sp.diag(*([sp.Integer(2)]*((n+1)//2)+[-sp.Integer(3)]*(n//2)))
    for s in range(2,n):
        for trial in range(12):
            X=sp.Matrix(n,s,[rng.randint(-2,2) for _ in range(n*s)])
            Y=X[:,:s-1]
            z=X[:,s-1]
            W=Y.T*A*Y
            if W.det()==0:continue
            B=A-A*Y*W.inv()*Y.T*A
            q=(z.T*B*z)[0]
            if q==0:continue
            Wfull=X.T*A*X
            assert Wfull.det()!=0
            Rfull=A-A*X*Wfull.inv()*X.T*A
            assert Rfull==B-(B*z)*(B*z).T/q
            n_checks+=1

# Two-eigenvalue exact Beta law of the n-minus-one-column residual:
# for dimension 3 and A = diag(1,-1,-1), T~Beta(1/2,1), tail constant 1/sqrt(2).
t0=mp.mpf('0.5')
c=2*1*1/(1+1)*t0**(mp.mpf('0.5')-1)*(1-t0)**(1-1)/mp.beta(mp.mpf('0.5'),1)
assert abs(c-1/mp.sqrt(2))<mp.mpf('1e-55')
n_checks+=1

print('PASS:',n_checks,'symbolic, high-precision distribution and numerical matrix checks')
print('n=2, a=b=1 exact survival: (2/pi) asin(1/x) for x>1')
print('for every nonsingular indefinite A and n>=2, moment threshold p=1 from coarea proof')
