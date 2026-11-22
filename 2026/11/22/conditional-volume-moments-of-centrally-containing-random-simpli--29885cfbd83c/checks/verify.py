"""Reproduce exact and numerical checks of conditional spherical simplex volumes."""
from itertools import product
from math import factorial, gamma, pi, sqrt
import numpy as np
import sympy as sp

SEED=20261121
rng=np.random.default_rng(SEED)

def samples(d,n):
    z=rng.standard_normal((n,d+1,d))
    return z/np.linalg.norm(z,axis=2,keepdims=True)

def minors(x):
    d=x.shape[2]
    return np.stack([(-1)**i*np.linalg.det(np.delete(x,i,axis=1)) for i in range(d+1)],axis=1)

def constants(d):
    a=gamma(d/2)**d/(sqrt(pi)*gamma((d+1)/2)**(d-1))
    c=gamma(d/2)/(sqrt(pi)*gamma((d+1)/2))
    return (d+1)*a/factorial(d),(d+1)*(1+d*d*c*c)/(factorial(d)*d**d)

def near(a,b,tol=0.025):
    assert abs(a-b) <= tol*max(0.01,abs(b)),(a,b,tol)

# Symbolic rational identity and rigorously negative third centered moment.
p=sp.symbols('p',positive=True)
m1=p/12
m2=sp.Rational(13,162)
m3=7*p/1152+2/(81*p)
f=sp.factor(m3-3*m1*m2+2*m1**3)
assert sp.simplify(f-(12*p**4-145*p**2+256)/(10368*p))==0
upper=sp.Rational(22,7);lower=sp.Rational(223,71)
assert f.subs(p,upper)==-sp.Rational(1091,6519744)
assert sp.diff(f,p).subs(p,lower)>0
assert sp.diff(f,p,2).subs(p,lower)>0
assert sp.simplify((4*(3*p/64)+36*(p/32)+24*(2/(9*p)))/216-m3)==0
assert abs(float(m3.subs(p,sp.pi))-0.02695)<0.00002

for d in (2,3,4):
    x=samples(d,110000)
    cof=minors(x)
    abscof=np.abs(cof)
    accept=np.logical_or(np.all(cof>0,axis=1),np.all(cof<0,axis=1))
    near(float(accept.mean()),2**(-d),0.025)
    s=abscof.sum(axis=1)/factorial(d)
    predicted1,predicted2=constants(d)
    near(float(s.mean()),predicted1,0.014)
    near(float(np.mean(s*s)),predicted2,0.018)
    # Directly conditioned actual Euclidean simplex volume.
    v=np.abs(np.linalg.det(x[:,1:,:]-x[:,:1,:]))/factorial(d)
    near(float(np.max(np.abs(v[accept]-s[accept]))),0.,1e-8)
    near(float(v[accept].mean()),predicted1,0.026)
    near(float(np.mean(v[accept]**2)),predicted2,0.032)
    lamb=abscof[accept]/abscof[accept].sum(axis=1)[:,None]
    assert np.max(np.linalg.norm(np.einsum('ni,nij->nj',lamb,x[accept]),axis=1))<1e-10
    assert np.max(np.abs(lamb.sum(axis=1)-1))<1e-12
    # Exact sign-orbit counts and determinant invariance, on independently sampled frames.
    for row in x[:3]:
        base=np.abs(minors(row[None,:,:])[0])
        good=0
        for signs in product((-1.,1.), repeat=d+1):
            ss=np.asarray(signs)
            cc=minors((row*ss[:,None])[None,:,:])[0]
            good+=int(np.all(cc>0) or np.all(cc<0))
            assert np.max(np.abs(np.abs(cc)-base))<1e-12
        assert good==2

# Three distinct versus two-equal determinant correlations on sphere S^2.
x=samples(3,370000)
a=np.abs(minors(x))
qcube=float(np.mean(a[:,0]**3))
qtwo=float(np.mean(a[:,0]**2*a[:,1]))
qtri=float(np.mean(a[:,0]*a[:,1]*a[:,2]))
near(qcube,3*pi/64,.018)
near(qtwo,pi/32,.018)
near(qtri,2/(9*pi),.019)
near(float(np.mean((a.sum(axis=1)/6)**3)),float(m3.subs(p,sp.pi)),.014)
print('ALL_CHECKS_PASSED',{'single_cubic':qcube,'two_equal':qtwo,'three_distinct':qtri,'central_third':float(f.subs(p,sp.pi))})
