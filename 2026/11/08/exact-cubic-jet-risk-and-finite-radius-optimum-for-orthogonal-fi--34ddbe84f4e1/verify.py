#!/usr/bin/env python3
"""Exact arithmetic checks for a finite-difference moment identity.
Public verification script. Only Python's standard library is needed.
Checks are finite consistency tests; the universal proof is mathematical.
"""
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from collections import defaultdict
from random import Random
from math import factorial

NASSERT=0

def check(a,b,context=''):
    global NASSERT
    NASSERT+=1
    if a!=b: raise AssertionError((context,a,b))

def tensor(d,rng,kind='random'):
    a={}
    for trip in combinations_with_replacement(range(d),3):
        a[trip]=F(rng.randrange(-3,4)) if kind=='random' else F(0)
    if kind=='radial':
        v=[F(rng.randrange(-3,4)) for _ in range(d)]
        if not any(v):v[0]=F(1)
        for trip in a:
            i,j,k=trip
            a[trip]=2*(v[i]*(j==k)+v[j]*(i==k)+v[k]*(i==j))
    if kind=='harmonic':
        v=[F(rng.randrange(-3,4)) for _ in range(d)]
        # Harmonic planar polynomial x0^3 -3x0*x1^2.
        a[(0,0,0)]=F(6)
        a[(0,1,1)]=F(-6)
    return lambda i,j,k:a[tuple(sorted((i,j,k)))]

def data(d,T):
    t=[sum((T(i,j,j) for j in range(d)),F(0)) for i in range(d)]
    H=lambda i,j,k:T(i,j,k)-(t[i]*(j==k)+t[j]*(i==k)+t[k]*(i==j))/F(d+2)
    ht=[sum((H(i,j,j) for j in range(d)),F(0)) for i in range(d)]
    hn=sum((H(i,j,k)**2 for i,j,k in product(range(d),repeat=3)),F(0))
    tn=sum((z*z for z in t),F(0))
    normT=sum((T(i,j,k)**2 for i,j,k in product(range(d),repeat=3)),F(0))
    for x in ht:check(x,F(0),'harmonic trace')
    check(normT,hn+F(3,d+2)*tn,'orthogonal tensor decomposition')
    return t,H,tn,hn

def monomial(d,exp):
    if any(e%2 for e in exp):return F(0)
    m=sum(exp)//2
    num=1
    for e in exp:
        for a in range(1,e,2):num*=a
    den=1
    for z in range(m):den*=d+2*z
    return F(num,den)

def poly_q(d,b,T,s):
    q=defaultdict(F)
    for i in range(d):
        e=[0]*d;e[i]=1;q[tuple(e)]+=b[i]
    for i,j,k in product(range(d),repeat=3):
        e=[0]*d
        for a in (i,j,k):e[a]+=1
        q[tuple(e)]+=s*T(i,j,k)/6
    return {e:c for e,c in q.items() if c}

def expect(d,p):return sum((c*monomial(d,e) for e,c in p.items()),F(0))

def direct(d,k,b,T,s):
    q=poly_q(d,b,T,s)
    mean=[]
    for i in range(d):
        p={tuple(e[z]+(z==i) for z in range(d)):c for e,c in q.items()}
        mean.append(d*expect(d,p))
    q2=defaultdict(F)
    for e,c in q.items():
        for f,v in q.items():q2[tuple(e[i]+f[i] for i in range(d))]+=c*v
    eq2=expect(d,q2)
    e_norm2=F(d*d,k)*eq2
    variance=e_norm2-sum((z*z for z in mean),F(0))
    risk=e_norm2-2*sum((x*y for x,y in zip(mean,b)),F(0))+sum((x*x for x in b),F(0))
    return mean,variance,risk

def closed(d,k,b,t,tn,hn,s):
    w=[b[i]+s*t[i]/F(2*(d+2)) for i in range(d)]
    wn=sum((x*x for x in w),F(0))
    var=F(d-k,k)*wn+s*s*F(d,6*k*(d+2)*(d+4))*hn
    risk=var+s*s*tn/F(4*(d+2)**2)
    return w,var,risk

def eval_f(d,x,b,T):
    return sum((b[i]*x[i] for i in range(d)),F(0))+sum((T(i,j,k)*x[i]*x[j]*x[k] for i,j,k in product(range(d),repeat=3)),F(0))/6

def oriented_check(d,k,b,T,s,columns):
    # For exact integer h, evaluate the actual 2k black-box function values.
    h=F(int(s**F(1,2))) # used only s=1,4
    grad=[F(0) for _ in range(d)]
    for u in columns[:k]:
        fp=eval_f(d,[h*y for y in u],b,T)
        fm=eval_f(d,[-h*y for y in u],b,T)
        deriv=(fp-fm)/(2*h)
        for i in range(d):grad[i]+=F(d,k)*u[i]*deriv
    t,H,tn,hn=data(d,T)
    w=[b[i]+s*t[i]/F(2*(d+2)) for i in range(d)]
    rhs=[F(0) for _ in range(d)]
    for u in columns[:k]:
        cubic=sum((H(i,j,m)*u[i]*u[j]*u[m] for i,j,m in product(range(d),repeat=3)),F(0))
        deriv=sum((w[i]*u[i] for i in range(d)),F(0))+s*cubic/6
        for i in range(d):rhs[i]+=F(d,k)*u[i]*deriv
    for a,z in zip(grad,rhs):check(a,z,'actual stencil vs harmonic representation')

rng=Random(13579)
for d in range(2,6):
    for rep in range(8):
        kind=('random','radial','harmonic','random')[rep%4]
        T=tensor(d,rng,kind)
        t,H,tn,hn=data(d,T)
        b=[F(rng.randrange(-3,4)) for _ in range(d)]
        for k in range(1,d+1):
            for s in (F(0),F(1,3),F(1),F(7,4)):
                m,v,r=direct(d,k,b,T,s)
                m2,v2,r2=closed(d,k,b,t,tn,hn,s)
                check(m,m2,'mean')
                check(v,v2,'variance')
                check(r,r2,'risk')

# The exact radial convex example, with a positive optimal finite radius.
for d in range(2,12):
    v=[F(1)]+[F(0)]*(d-1)
    T=lambda i,j,k:F(2)*(v[i]*(j==k)+v[j]*(i==k)+v[k]*(i==j))
    t,H,tn,hn=data(d,T)
    check(hn,F(0),'radial harmonic cancellation')
    b=[-z for z in v]
    for k in range(1,d):
        s=F(d-k,d)
        _,_,r0=closed(d,k,b,t,tn,hn,F(0))
        _,_,rstar=closed(d,k,b,t,tn,hn,s)
        check(r0,F(d-k,k),'radial base risk')
        check(rstar,F(d-k,d),'radial optimal risk')
        # Exact strict risk gap by completing the square.
        for ds in [F(-1,5),F(1,5),F(1)]:
            if s+ds>=0:
                _,_,risk=closed(d,k,b,t,tn,hn,s+ds)
                check(risk-rstar,F(d,k)*ds*ds,'sharp quadratic minimum')

# Selected rational orthonormal frames and direct function evaluations.
for kind in ('random','radial','harmonic'):
    T=tensor(3,rng,kind)
    b=[F(1),F(-2),F(3)]
    U=[[F(3,5),F(4,5),F(0)],[-F(4,5),F(3,5),F(0)],[F(0),F(0),F(1)]]
    for k in (1,2,3):
        for s in (F(1),F(4)):
            oriented_check(3,k,b,T,s,U)

print('PASS:',NASSERT,'exact rational assertions; moments, tensor traces, sharp radius, and direct stencil values')
