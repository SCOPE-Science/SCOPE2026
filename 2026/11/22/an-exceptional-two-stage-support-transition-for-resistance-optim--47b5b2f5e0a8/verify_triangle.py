"""Independent symbolic-spectrum and full-edge KKT checks for priced-triangle conductance design.

Run: python3 verify_triangle.py (requires sympy and numpy).
These finite checks supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction
from math import sqrt, isclose
import itertools
import numpy as np
import sympy as sp

checks=0

def candidate(m,r,B=1.0):
    n=m+3
    ra=Fraction((m+1)*(m+3),m*(m+2))
    if m==2 and r>=Fraction(45,23):
        ar,cr=0.0,0.0
        phase='bipartite'
    elif m==2 and r>=Fraction(9,5):
        X=sqrt((45/float(r)-15)/2)
        ar,cr=(X-2)/3,0.0
        phase='cross+triangle'
    elif m>=3 and r>=ra:
        u=sqrt(m*(m+1)*(m+3)/(m+2))
        ar,cr=0.0,(u-3)/m
        phase='cross+outside'
    else:
        X=sqrt(n*(3*(m+1)/float(r)-2*m))
        Y=sqrt(float(r))*X
        ar,cr=(X-m)/3,(Y-3)/m
        phase='all'
    denom=3*float(r)*ar+3*m+m*(m-1)*cr/2
    b=B/denom
    return (ar*b,b,cr*b,phase)

def lap(m,a,b,c):
    n=m+3
    L=np.zeros((n,n),dtype=float)
    edges=[]
    for i,j in itertools.combinations(range(n),2):
        typ='a' if i<3 and j<3 else ('c' if i>=3 else 'b')
        w={'a':a,'b':b,'c':c}[typ]
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
        edges.append((i,j,typ,w))
    return L,edges

# Independent exact full-matrix spectrum and inverse traces, using nonoptimal rational weights.
a0,b0,c0=sp.Rational(2,7),sp.Rational(3,5),sp.Rational(5,6)
for m in range(2,7):
    n=m+3
    L=sp.zeros(n)
    for i,j in itertools.combinations(range(n),2):
        w=a0 if j<3 else (c0 if i>=3 else b0)
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    X=3*a0+m*b0
    Y=m*c0+3*b0
    expected=sp.Symbol('x')*(sp.Symbol('x')-X)**2*(sp.Symbol('x')-Y)**(m-1)*(sp.Symbol('x')-n*b0)
    assert sp.expand(L.charpoly('x').as_expr()-expected)==0
    exact=sp.trace((L+sp.ones(n)/n).inv())-1
    assert sp.factor(exact-(2/X+(m-1)/Y+1/(n*b0)))==0
    checks+=2

# Exact symbolic thresholds and phase boundary identities, for many distinct sizes.
for m in range(2,60):
    n=m+3
    ra=Fraction((m+1)*n,m*(m+2))
    if m>=3:
        u2=Fraction(m*(m+1)*n,m+2)
        assert u2>9
        assert ra==u2/Fraction(m*m)
        assert Fraction(3*(m+4),2*n)>ra
        checks+=3
    else:
        assert Fraction(9,5)<Fraction(45,23)
        assert Fraction(45,Fraction(15+2*5))==Fraction(9,5)
        checks+=2

# Full, unrestricted edge-gradient KKT checks (all edges independently varied).
for m in [2,3,4,5,6,8,12]:
    ra=Fraction((m+1)*(m+3),m*(m+2))
    rr=[Fraction(1,20),Fraction(1,2),Fraction(1,1),Fraction(11,10),ra]
    if m==2:rr += [Fraction(9,5),Fraction(37,20),Fraction(45,23),Fraction(2,1),Fraction(5,1)]
    else:rr += [ra-Fraction(1,1000),ra+Fraction(1,1000),Fraction(3,1),Fraction(10,1)]
    for r in set(rr):
        if r<=0: continue
        a,b,c,phase=candidate(m,r)
        n=m+3
        assert min(a,b,c)>-1e-10
        assert b>0
        L,edges=lap(m,a,b,c)
        weighted=sum((float(r) if typ=='a' else 1)*w for _,_,typ,w in edges)
        assert abs(weighted-1)<1e-10
        ev=np.linalg.eigvalsh(L)
        assert ev[1]>1e-12
        positive=np.sort(ev[1:])
        X=3*a+m*b;Y=m*c+3*b
        expected=np.sort([X]*2+[Y]*(m-1)+[(m+3)*b])
        assert np.allclose(positive,expected,atol=1e-9,rtol=1e-9)
        Ainv=np.linalg.inv(L+np.ones((n,n))/n)
        K=n*(np.trace(Ainv)-1)
        assert isclose(K,n*(2/X+(m-1)/Y+1/((m+3)*b)),rel_tol=2e-9,abs_tol=2e-8)
        # KKT of K itself with positive b edges setting the multiplier; verify all edge types.
        grads=[]
        for i,j,typ,w in edges:
            diff=Ainv[:,i]-Ainv[:,j]
            grad=-n*float(diff@diff)
            grads.append((typ,w,grad, float(r) if typ=='a' else 1.0))
        lambdas=[-g/cost for typ,w,g,cost in grads if typ=='b']
        lam=sum(lambdas)/len(lambdas)
        for typ,w,grad,cost in grads:
            slack=grad+lam*cost
            assert slack>-2e-7, (m,r,phase,typ,slack)
            if w>1e-9:assert abs(slack)<2e-7, (m,r,phase,typ,slack)
            checks+=1
        checks+=6

print('PASS',checks,'exact symbolic / direct matrix / full-edge KKT checks')
