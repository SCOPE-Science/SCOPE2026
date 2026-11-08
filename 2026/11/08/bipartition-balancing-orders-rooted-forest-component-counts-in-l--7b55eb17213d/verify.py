#!/usr/bin/env python3
"""Exact checks for the bipartition-balancing rooted-forest theorem."""
from fractions import Fraction
from math import comb

checks = 0

def require(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def mul(A, B):
    C = [0] * (len(A) + len(B) - 1)
    for i, x in enumerate(A):
        for j, y in enumerate(B):
            C[i+j] += x*y
    return C

def coefficients(a, b):
    n = a+b
    c = [0, 1]
    for v in ([n] + [a]*(b-1) + [b]*(a-1)):
        c = mul(c, [v, 1])
    return c

def rooted_forest_coefficients(a,b):
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    out=[0]*(n+1)
    for mask in range(1<<len(edges)):
        parent=list(range(n))
        size=[1]*n
        components=n
        acyclic=True
        for k,(u,v) in enumerate(edges):
            if not (mask>>k)&1:
                continue
            ru=u
            while parent[ru]!=ru: ru=parent[ru]
            rv=v
            while parent[rv]!=rv: rv=parent[rv]
            if ru==rv:
                acyclic=False
                break
            parent[rv]=ru
            size[ru]+=size[rv]
            components-=1
        if acyclic:
            weight=1
            for i in range(n):
                if parent[i]==i:weight*=size[i]
            out[components]+=weight
    return out

def mass(a,b,q):
    c=coefficients(a,b)
    d=[Fraction(c[k])*q**k for k in range(len(c))]
    z=sum(d)
    return [v/z for v in d]

def bernoulli_mass(a,b,q):
    n=a+b
    probs=[Fraction(1)]+[q/(q+n)]+[q/(q+a)]*(b-1)+[q/(q+b)]*(a-1)
    d=[Fraction(1)]
    for p in probs:
        d=mul(d,[1-p,p])
    return d

for n in range(2,9):
    for a in range(1,n):
        b=n-a
        require(coefficients(a,b)==rooted_forest_coefficients(a,b), ('forest count',a,b))

for n in range(4,32):
    for a in range(1,n//2):
        b=n-a
        for q in map(Fraction, (Fraction(1,3), Fraction(1),Fraction(3,2),Fraction(7),Fraction(100))):
            P,Q=mass(a,b,q),mass(a+1,b-1,q)
            require(P==bernoulli_mass(a,b,q),('Bernoulli factor',a,b,q))
            require(Q==bernoulli_mass(a+1,b-1,q),('Bernoulli factor next',a,b,q))
            for k in range(1,n):
                require(P[k+1]*Q[k] >= P[k]*Q[k+1],('LR ordering',a,b,q,k))
            for k in range(2,n+1):
                require(sum(P[k:])>sum(Q[k:]),('strict upper tail',a,b,q,k))
            gap = sum(k*P[k] for k in range(n+1))-sum(k*Q[k] for k in range(n+1))
            formula=q*(b-a-1)*(n+2*q)*(n+q-1)/((a+q)*(b+q)*(a+q+1)*(b+q-1))
            require(gap==formula,('mean gap',a,b,q))

print(f'VERIFY_OK {checks} exact rational checks')
