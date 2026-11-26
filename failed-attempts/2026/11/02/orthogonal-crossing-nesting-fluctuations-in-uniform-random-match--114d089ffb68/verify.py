#!/usr/bin/env python3
"""Exact reproducibility checks for crossing and nesting counts in uniform matchings.

Standard Python only. Run: python3 verify.py
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, factorial

checks = 0

def equal(actual, expected, label):
    global checks
    assert actual == expected, f"{label}: actual={actual}, expected={expected}"
    checks += 1

# Formal polynomial arithmetic on a,b,c for Dirichlet(1,1,1).
def add(*polys):
    out = {}
    for p in polys:
        for k,v in p.items(): out[k] = out.get(k,0)+v
    return {k:v for k,v in out.items() if v}

def mul(x,y):
    out={}
    for i,u in x.items():
        for j,v in y.items():
            ij=tuple(a+b for a,b in zip(i,j))
            out[ij]=out.get(ij,0)+u*v
    return out

def power(x,n):
    r={(0,0,0):1}
    for _ in range(n):r=mul(r,x)
    return r

def average(p):
    return sum((Q(2*v*factorial(i)*factorial(j)*factorial(k),factorial(i+j+k+2))
                for (i,j,k),v in p.items()),Q(0))

A={(1,0,0):1};B={(0,1,0):1};C={(0,0,1):1}
pX={ (1,1,0):2,(0,1,1):2 }
pN={ (0,2,0):1,(1,0,1):2 }
pAlign=add(power(A,2),power(C,2))
equal(average(pX),Q(1,3),'crossing one-chord projection mean')
equal(average(pN),Q(1,3),'nesting one-chord projection mean')
equal(average(pAlign),Q(1,3),'alignment projection mean')
equal(average(power(pX,2)),Q(2,15),'crossing projection square')
equal(average(power(pN,2)),Q(2,15),'nesting projection square')
equal(average(mul(pX,pN)),Q(1,9),'mixed projection product')
equal(average(mul(pX,pN))-Q(1,9),Q(0),'projection orthogonality')
equal(average(power(pX,2))-Q(1,9),Q(1,45),'projection crossing variance')
equal(average(power(pN,2))-Q(1,9),Q(1,45),'projection nesting variance')

def matchings(seq):
    seq=tuple(seq)
    if not seq:
        yield ()
        return
    a=seq[0]
    for k in range(1,len(seq)):
        b=seq[k]
        for rest in matchings(seq[1:k]+seq[k+1:]):
            yield ((a,b),)+rest

def kind(one,two):
    a,b=one;c,d=two
    if a>c:a,b,c,d=c,d,a,b
    if a<c<b<d:return 'X'
    if a<c<d<b:return 'N'
    return 'A'

def counts(edges):
    x=t=0
    for i in range(len(edges)):
        for j in range(i+1,len(edges)):
            k=kind(edges[i],edges[j])
            x+=k=='X';t+=k=='N'
    return x,t

for n in range(1,8):
    z=sx=sn=sxx=snn=sxn=0
    for mt in matchings(range(2*n)):
        x,y=counts(mt)
        z+=1;sx+=x;sn+=y;sxx+=x*x;snn+=y*y;sxn+=x*y
    expected_total=factorial(2*n)//(2**n*factorial(n))
    equal(z,expected_total,f'matching cardinality n={n}')
    ex=Q(n*(n-1),6)
    vx=Q(n*(n-1)*(n+3),45)
    cv=Q(-n*(n-1),18)
    equal(Q(sx,z),ex,f'crossing mean n={n}')
    equal(Q(sn,z),ex,f'nesting mean n={n}')
    equal(Q(sxx,z)-Q(sx,z)**2,vx,f'crossing variance n={n}')
    equal(Q(snn,z)-Q(sn,z)**2,vx,f'nesting variance n={n}')
    equal(Q(sxn,z)-Q(sx,z)*Q(sn,z),cv,f'mixed covariance n={n}')

# For labeled chords, each matching is uniformly assigned all n! chord labels.
for n in (3,4):
    total=px=pn=both=0
    for mt in matchings(range(2*n)):
        for e in permutations(mt):
            a=(kind(e[0],e[1])=='X')
            b=(kind(e[0],e[2])=='N')
            total+=1;px+=a;pn+=b;both+=a and b
    equal(Q(px,total),Q(1,3),f'X[0,1] marginal n={n}')
    equal(Q(pn,total),Q(1,3),f'N[0,2] marginal n={n}')
    equal(Q(both,total),Q(1,9),f'independence of overlapping labeled pairs n={n}')

n=4;total=both=0
for mt in matchings(range(2*n)):
    for e in permutations(mt):
        total+=1
        both+=kind(e[0],e[1])=='X' and kind(e[2],e[3])=='N'
equal(Q(both,total),Q(1,9),'independence of disjoint labeled pairs')

# Algebraic checks of the covariance, correlation, and Hoeffding variance split.
for n in range(2,200):
    m=comb(n,2)
    v=Q(m*2,9)+Q(n*(n-1)*(n-2),45)
    equal(v,Q(n*(n-1)*(n+3),45),f'variance count identity n={n}')
    equal(Q(-m,9)/v,Q(-5,2*(n+3)),f'correlation identity n={n}')
    equal(Q(n*(n-1)**2,45)+Q(m*8,45),v,f'Hoeffding decomposition n={n}')

print(f'PASS: {checks} exact assertions, matchings exhaustively enumerated through n=7.')
