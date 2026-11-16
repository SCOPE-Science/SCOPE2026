"""Exact formulas and independent Gram reconstruction for quartic S^3 latitude traces.

Requires Python 3, SymPy and NumPy. No stored data or network access is used.
This script checks finite symbolic identities and representative exact-rational
latitude Gram matrices; the infinite/global theorem uses the inequalities
proved in RESULT.md, not these numerical tests.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from functools import lru_cache
import sympy as s
import numpy as np

u=s.symbols('u')
lam=[(16*u*u-12*u+1)**2,
     s.Rational(8,3)*u*(1-u)*(8*u-3)**2,
     s.Rational(8,7)*(1-u)**2*(8*u-1)**2,
     s.Rational(128,7)*u*(1-u)**3,
     s.Rational(128,63)*(1-u)**4]
C=[s.gegenbauer(4-m,m+1,s.symbols('t')) for m in range(5)]

def rising(q,n):
    v=s.S.One
    for j in range(n):v*=q+j
    return v

# Independent polynomial moment route for all five spherical branches.
t=s.symbols('t')
for m in range(5):
    cm=s.expand(C[m]*C[m])
    norm=sum(coeff*rising(s.Rational(1,2),mon[0]//2)
             *rising(s.Rational(3,2),m)/rising(s.Integer(2),mon[0]//2+m)
             for mon,coeff in s.Poly(cm,t).terms())
    formula=s.factor((1-u)**m*cm.subs(t,s.sqrt(u))/norm)
    assert s.factor(formula-lam[m])==0,(m,formula)
assert s.expand(sum((2*m+1)*lam[m] for m in range(5)))==25

p=640*u**3-576*u**2+114*u-3
assert p.subs(u,s.Rational(6,25))>0 and p.subs(u,s.Rational(1,4))<0
assert 1920*s.Rational(1,4)**2-1152*s.Rational(6,25)+114<0
assert s.simplify(lam[1]-lam[2]+s.Rational(8,21)*(u-1)*p)==0
# Scalar rational partition certificate for global optimum.
assert lam[3].subs(u,s.Rational(1,32))<s.Rational(11,20)
assert lam[0].subs(u,s.Rational(1,32))<s.Rational(11,20)
assert lam[2].subs(u,s.Rational(6,25))>s.Rational(11,20)
assert lam[4].subs(u,s.Rational(7,25))<s.Rational(11,20)
assert lam[0].subs(u,s.Rational(6,25))>lam[1].subs(u,s.Rational(6,25))
assert s.Rational(324,175)>lam[1].subs(u,s.Rational(6,25))
assert s.Rational(9,14)>lam[1].subs(u,s.Rational(6,25))

# Construct every homogeneous harmonic quartic directly as kernel of Laplacian
# on the 35-dimensional monomial degree-four space. This is independent of
# the separated Gegenbauer bases above.
def exps(d,k):
    return [tuple(sum(int(q==j) for q in inds) for j in range(d))
            for inds in combinations_with_replacement(range(d),k)]
A=exps(4,4);B=exps(4,2);idx={b:j for j,b in enumerate(B)}
D=s.zeros(len(B),len(A))
for i,a in enumerate(A):
    for j,v in enumerate(a):
        if v>=2:
            b=list(a);b[j]-=2;D[idx[tuple(b)],i]+=v*(v-1)
vecs=D.nullspace()
assert len(A)==35 and D.rank()==10 and len(vecs)==25
vecs=[{A[k]:F(int(x.p),int(x.q)) for k,x in enumerate(vec) if x}
      for vec in vecs]

def poch_half(k):
    ans=F(1)
    for j in range(k):ans*=F(2*j+1,2)
    return ans

def poch_integer(a,k):
    ans=F(1)
    for j in range(k):ans*=F(a+j)
    return ans

@lru_cache(None)
def sphere_moment(ex):
    if any(e%2 for e in ex):return F(0)
    ans=F(1)
    for e in ex:ans*=poch_half(e//2)
    return ans/poch_integer(2,sum(ex)//2)

@lru_cache(None)
def sphere3_moment(ex):
    if any(e%2 for e in ex):return F(0)
    ans=F(1)
    for e in ex:ans*=poch_half(e//2)
    den=F(1)
    for j in range(sum(ex)//2):den*=F(3+2*j,2)
    return ans/den

basis=[list(v.items()) for v in vecs]

def inner(i,j,mode,uu=F(0)):
    acc=F(0)
    for a,ca in basis[i]:
        for b,cb in basis[j]:
            ex=tuple(a[k]+b[k] for k in range(4))
            if mode=='sphere':q=sphere_moment(ex)
            else:
                trans=ex[:3]
                if ex[3]%2:continue
                q=uu**(ex[3]//2)*(1-uu)**(sum(trans)//2)*sphere3_moment(trans)
            acc+=ca*cb*q
    return acc

H=np.array([[float(inner(i,j,'sphere')) for j in range(25)] for i in range(25)])
chol=np.linalg.cholesky(H)
for uu in [F(1,32),F(1,8),F(6,25),F(1,4),F(1,2),F(7,10)]:
    M=np.array([[float(inner(i,j,'latitude',uu)) for j in range(25)] for i in range(25)])
    Bm=np.linalg.solve(chol,M)
    Bm=np.linalg.solve(chol,Bm.T).T
    actual=np.linalg.eigvalsh((Bm+Bm.T)*0.5)
    predicted=sorted([float(L.subs(u,s.Rational(uu.numerator,uu.denominator)))
                      for m,L in enumerate(lam) for _ in range(2*m+1)])
    err=max(abs(x-y) for x,y in zip(actual,predicted))
    assert err<1e-8,(uu,err)
    print('latitude u=',uu,'spectral error=',f'{err:.2e}',
          'min=',f'{min(actual):.12f}')

root=s.nroots(p,maxsteps=200,n=50)
tau=next(s.re(z) for z in root if abs(float(s.im(z)))<1e-20 and s.Rational(6,25)<s.re(z)<s.Rational(1,4))
h=s.N(lam[1].subs(u,tau),40)
assert abs(float(lam[1].subs(u,tau)-lam[2].subs(u,tau)))<1e-35
print('tau=',tau)
print('h=',h)
print('branch values=',[s.N(L.subs(u,tau),18) for L in lam])
print('all symbolic identities, interval certificates and independent Gram tests passed')
