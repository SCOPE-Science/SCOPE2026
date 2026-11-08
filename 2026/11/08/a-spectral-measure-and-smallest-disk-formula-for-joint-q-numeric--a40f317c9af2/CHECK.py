#!/usr/bin/env python3
"""Finite algebraic diagnostics for the complex coefficient-lifting lemma.
No infinite-dimensional or originality certification is implied.
"""
import random, cmath, math

rng = random.Random(261006)

def dot(x,y):
    return sum(a*b.conjugate() for a,b in zip(x,y))

def norm(x):
    return math.sqrt(sum(abs(a)**2 for a in x))

def lift(a):
    n=len(a)
    assert n>=2
    b=[abs(v) for v in a]
    assert sum(b)<=1+1e-10
    active=[i for i in range(n) if b[i]>1e-13]
    if len(active)<2:
        i=active[0] if active else 0
        j=(i+1)%n
        x=[0j]*n; y=[0j]*n
        x[i]=1+0j
        y[i]=a[i].conjugate() if active else 0j
        y[j]=math.sqrt(max(0.,1-abs(y[i])**2))
        return x,y
    B=sum(b[i] for i in active)
    r0=[b[i]/B for i in active]
    if 1-B**2<1e-13:
        r=r0
    else:
        # Move from the Cauchy-Schwarz minimizer to the simplex boundary.
        def vals(t):
            rr=[(1-t)*v for v in r0]
            rr[0]+=t
            return rr
        def fun(t):
            rr=vals(t)
            return sum(b[i]**2/rr[j] for j,i in enumerate(active))-1
        low,high=0.,1-1e-13
        assert fun(low)<1e-10 and fun(high)>0
        for _ in range(80):
            mid=(low+high)/2
            if fun(mid)>0:high=mid
            else:low=mid
        r=vals((low+high)/2)
    x=[0j]*n; y=[0j]*n
    for k,i in enumerate(active):
        x[i]=math.sqrt(r[k])
        y[i]=a[i].conjugate()/x[i]
    return x,y

count=0
for n in range(2,9):
    for _ in range(300):
        x=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
        y=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
        x=[z/norm(x) for z in x]
        y=[z/norm(y) for z in y]
        a=[u*v.conjugate() for u,v in zip(x,y)]
        u,v=lift(a)
        assert abs(norm(u)-1)<3e-8
        assert abs(norm(v)-1)<3e-8
        assert max(abs(u[i]*v[i].conjugate()-a[i]) for i in range(n))<3e-8
        assert abs(dot(u,v)-sum(a))<3e-8
        count+=1
for q in [0j,.2+.3j,-.5+.4j,.9+0j,1+0j]:
    for a in ([q,0j,0j],[0j,q,0j],[q/2,q/2,0j],[0j,0j,0j]):
        if abs(sum(a)-q)>1e-12:continue
        u,v=lift(a)
        assert abs(norm(u)-1)<3e-8
        assert abs(norm(v)-1)<3e-8
        assert abs(dot(u,v)-q)<3e-8
        count+=1
# Sample the exact finite-measure support inequality, using arbitrary feasible
# measures a and arbitrary centers z. This is not an optimization certificate.
for _ in range(1000):
    n=rng.randrange(2,8)
    c=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
    x=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
    y=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
    x=[u/norm(x) for u in x];y=[u/norm(y) for u in y]
    a=[u*v.conjugate() for u,v in zip(x,y)]
    q=sum(a)
    z=complex(rng.gauss(0,1),rng.gauss(0,1))
    lhs=(sum(a[i]*c[i] for i in range(n))).real
    rhs=(q*z).real+max(abs(w-z) for w in c)
    assert lhs<=rhs+1e-9
    count+=1
print('PASS',count,'diagnostic assertions')
