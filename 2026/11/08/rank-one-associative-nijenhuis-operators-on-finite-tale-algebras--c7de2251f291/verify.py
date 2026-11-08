#!/usr/bin/env python3
"""Exact small-field check of rank-one associative Nijenhuis maps.
No external dependencies; all tests use the defining basis-pair identity.
"""
import itertools
import math


def extension_mult(a, b, q, degree):
    if degree == 1:
        return [(a[0]*b[0])%q]
    # Quadratic polynomial theta^2+c1 theta+c0=0.
    assert degree == 2 and q in (2,3)
    c0,c1 = (1,1) if q==2 else (1,0)
    return [(a[0]*b[0]-c0*a[1]*b[1])%q,
            (a[0]*b[1]+a[1]*b[0]-c1*a[1]*b[1])%q]


def multiplication_table(q,degrees):
    d=sum(degrees)
    table=[[[0]*d for _ in range(d)] for _ in range(d)]
    s=0
    for deg in degrees:
        for i in range(deg):
            for j in range(deg):
                a=[int(k==i) for k in range(deg)]
                b=[int(k==j) for k in range(deg)]
                z=extension_mult(a,b,q,deg)
                for k in range(deg):table[s+i][s+j][s+k]=z[k]
        s+=deg
    return table


def prod(x,y,T,q):
    d=len(x)
    z=[0]*d
    for i,xi in enumerate(x):
        if xi:
            for j,yj in enumerate(y):
                if yj:
                    for k,t in enumerate(T[i][j]):z[k]=(z[k]+xi*yj*t)%q
    return z


def rank_one_maps(q,d):
    vectors=[v for v in itertools.product(range(q),repeat=d) if any(v)]
    for u in vectors:
        if next(x for x in u if x)==1:
            for phi in vectors:
                yield tuple(tuple((a*b)%q for a in u) for b in phi)


def nij(columns,T,q):
    d=len(columns)
    for i in range(d):
        for j in range(d):
            left=prod(columns[i],columns[j],T,q)
            u=prod(columns[i],tuple(int(k==j) for k in range(d)),T,q)
            v=prod(tuple(int(k==i) for k in range(d)),columns[j],T,q)
            xy=T[i][j]
            arg=[(u[k]+v[k]-sum(xy[t]*columns[t][k] for t in range(d)))%q for k in range(d)]
            rhs=[sum(arg[t]*columns[t][k] for t in range(d))%q for k in range(d)]
            if tuple(left)!=tuple(rhs):return False
    return True


def predicted(q,degrees):
    d=sum(degrees)
    offsets=[]
    s=0
    for deg in degrees:
        offsets.append(s);s+=deg
    singles=[i for i,deg in enumerate(degrees) if deg==1]
    canon=set()
    for mask in range(1,1<<len(degrees)):
        u=[0]*d
        for i,st in enumerate(offsets):
            if mask>>i & 1:u[st]=1
        for i in singles:
            if not (mask>>i & 1):continue
            for c in range(1,q):
                for j in [None]+[j for j in singles if not(mask>>j & 1)]:
                    cols=[]
                    for k in range(d):
                        coeff=(c if k==offsets[i] else (-c if j is not None and k==offsets[j] else 0))%q
                        cols.append(tuple((coeff*v)%q for v in u))
                    canon.add(tuple(cols))
    return canon


def counts(q,degrees):
    expected=predicted(q,degrees)
    T=multiplication_table(q,degrees)
    good={P for P in rank_one_maps(q,sum(degrees)) if nij(P,T,q)}
    assert good==expected, (q,degrees,len(good),len(expected),len(good-expected),len(expected-good))
    s=sum(deg==1 for deg in degrees)
    r=len(degrees)
    pred=(q-1)*s*2**(r-1)
    if s>=2:pred+=(q-1)*s*(s-1)*2**(r-2)
    assert len(good)==pred
    print('PASS q=%s factors=%s actual=%s predicted=%s' %(q,degrees,len(good),pred))


if __name__=='__main__':
    for q,degs in [(2,(1,)),(3,(1,)),(2,(2,)),(3,(2,)),
                   (2,(1,2)),(3,(1,2)),(2,(1,1)),(3,(1,1)),
                   (2,(1,1,2)),(2,(1,1,1)),(3,(1,1,1))]:
        counts(q,degs)
    print('VERIFY_OK')
