#!/usr/bin/env python3
"""Reproduce finite probabilities and the four-vertex symbolic partition identity."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import prod
import sympy as sp

def falling(z, m):
    return prod(z-j for j in range(m))

@lru_cache(None)
def involutions(vertices):
    if not vertices:
        return ((),)
    a=vertices[0]
    answer=[((a,a),)+rest for rest in involutions(vertices[1:])]
    for b in vertices[1:]:
        answer.extend(((a,b),)+rest for rest in involutions(tuple(x for x in vertices[1:] if x!=b)))
    return tuple(answer)

@lru_cache(None)
def states(vertices):
    if not vertices:
        return (((),0,0,0),)
    a=vertices[0]
    ans=[(((a,a),)+rest, f+1,e,t) for rest,f,e,t in states(vertices[1:])]
    ans += [(((a,'E'),)+rest, f,e+1,t) for rest,f,e,t in states(vertices[1:])]
    for b in vertices[1:]:
        ans += [(((a,b),)+rest, f,e,t+1) for rest,f,e,t in states(tuple(x for x in vertices[1:] if x!=b))]
    return tuple(ans)

# Four marked locations are i,i+1,j,j+1. The other labels fall in three bins
# of sizes A=i-1, B=j-i-2, C=n-j-1. In every partial matching external
# partners in a bin are distinct and uniformly ordered. Every comparison
# whose two images share one bin has probability 1/2. Since the two
# comparisons use disjoint images, their conditional order events are
# independent even when all images fall in the same bin.
A,B,C,k=sp.symbols('A B C k',integer=True,nonnegative=True)
n=A+B+C+4
r=(n-k)/2
coefficient=defaultdict(lambda:sp.S.Zero)
for edges,f,e,t in states((1,2,3,4)):
    image={}; external=[]
    for a,b in edges:
        if b=='E':
            image[a]='E'; external.append(a)
        else:
            image[a]=b; image[b]=a
    for bins in product(range(3),repeat=e):
        placement=dict(zip(external,bins))
        def descent(a,b):
            x,y=image[a],image[b]
            if x=='E' and y=='E':
                return sp.Rational(1,2) if placement[a]==placement[b] else int(placement[a]>placement[b])
            if x=='E': return int((0,3,6)[placement[a]] > {1:1,2:2,3:4,4:5}[y])
            if y=='E': return int({1:1,2:2,3:4,4:5}[x] > (0,3,6)[placement[b]])
            return int(x>y)
        q=descent(1,2)*descent(3,4)
        if q:
            m=(bins.count(0),bins.count(1),bins.count(2))
            coefficient[(f,e,t)]+=q*falling(A,m[0])*falling(B,m[1])*falling(C,m[2])

v=A+B+C
expected={
    (0,0,2):2,
    (0,2,1):2*falling(v,2),
    (0,4,0):sp.Rational(1,4)*falling(v,4),
    (1,1,1):4*v,
    (1,3,0):falling(v,3),
    (2,0,1):1,
    (2,2,0):falling(v,2),
}
assert len(states((1,2,3,4)))==43
assert set(coefficient)==set(expected)
for t in expected:
    assert sp.expand(coefficient[t]-expected[t])==0,(t,coefficient[t])
print('PASS: 43 partial matching states, 7 nonzero weighted types, all interval sizes symbolic')

J=sp.S.Zero
for (f,e,t),count in coefficient.items():
    J+=count*falling(k,f)*2**(e+t)*falling(r,e+t)/falling(n,4+e)
J=sp.cancel(J)
P=(n**2-k**2)/(2*n*(n-1))
H=n**2*(n-2)-n**2*k+n*k**2-(2*n-3)*k**3
COV=(n-k)*H/(2*n**2*(n-3)*(n-2)*(n-1)**2)
assert sp.factor(J-P**2-COV)==0
print('PASS: symbolic probability and covariance identities')

cases=checks=0
for N in range(4,11):
    grouped=defaultdict(list)
    for pairs in involutions(tuple(range(1,N+1))):
        perm=list(range(N+1)); K=0
        for a,b in pairs:
            perm[a]=b; perm[b]=a; K+=a==b
        grouped[K].append(perm)
    for K,group in grouped.items():
        P0=Fraction(N*N-K*K,2*N*(N-1))
        H0=N*N*(N-2)-N*N*K+N*K*K-(2*N-3)*K**3
        C0=Fraction((N-K)*H0,2*N*N*(N-3)*(N-2)*(N-1)**2)
        D=[sum(p[i]>p[i+1] for p in group) for i in range(1,N)]
        for x in D:
            assert Fraction(x,len(group))==P0
            checks+=1
        for i in range(1,N):
            for j in range(i+2,N):
                jnt=Fraction(sum((p[i]>p[i+1])*(p[j]>p[j+1]) for p in group),len(group))
                assert jnt-P0**2==C0,(N,K,i,j,jnt-P0**2,C0)
                checks+=1
        cases+=1
print('PASS:',checks,'exact exhaustive checks across',cases,'nonempty fixed-point classes, N=4..10')

# Sign and asymptotic root coefficient check.
N,T,a,b,c=sp.symbols('N T a b c',positive=True)
# Writing N=T^3 and k=a*T^2+b*T+c, cancel successive high powers.
H_N=N**2*(N-2)-N**2*k+N*k**2-(2*N-3)*k**3
Q=sp.expand(H_N.subs({N:T**3,k:a*T**2+b*T+c}))
assert sp.factor(Q.coeff(T,9))==1-2*a**3
assert sp.factor(Q.coeff(T,8))==-a*(6*a*b+1)
assert sp.factor(Q.coeff(T,7))==-6*a*a*c-6*a*b*b-b+a*a
assert sp.simplify(Q.coeff(T,7).subs({b:-1/(6*a),c:sp.Rational(1,6)}))==0
print('PASS: cubic root expansion through constant term')
