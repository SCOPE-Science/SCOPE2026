#!/usr/bin/env python3
"""Exact polynomial reconstruction of the characteristic-seven plane-quartic Hasse matrix."""
from collections import defaultdict
P=7
# For each monomial: (exponents of X=x^2,Y=y^2,Z=z^2,a,b)
terms=[(2,0,0,0,0),(0,2,0,0,0),(0,0,2,0,0),
       (1,1,0,1,0),(1,0,1,0,1),(0,1,1,0,1)]
F={(0,0,0,0,0):1}
for step in range(6):
    G=defaultdict(int)
    for e,c in F.items():
        for t in terms:
            key=tuple(e[i]+t[i] for i in range(5))
            G[key]=(G[key]+c)%P
    F={k:v for k,v in G.items() if v}

def extract(xyz):
    return {(e[3],e[4]):c for e,c in F.items() if e[:3]==xyz}

def norm(d):
    return {k:(v%P) for k,v in d.items() if v%P}
def mul(u,v):
    w=defaultdict(int)
    for (i,j),c in u.items():
        for (r,s),d in v.items():w[(i+r,j+s)]+=c*d
    return norm(w)
def add(u,v):
    w=defaultdict(int,u)
    for e,c in v.items():w[e]+=c
    return norm(w)
def scale(u,c):return norm({k:v*c for k,v in u.items()})
A={(2,0):1,(0,0):-4};B={(0,2):1,(0,0):-4}
C={(1,1):2,(0,1):-4};D={(0,2):2,(1,0):-4}
lambda_h=mul(C,add(mul(C,C),scale(mul(A,B),6)))
mu_h=mul(D,add(mul(D,D),scale(mul(B,B),6)))
assert extract((6,3,3))==lambda_h, (extract((6,3,3)),lambda_h)
assert extract((3,6,3))==lambda_h
assert extract((3,3,6))==mu_h
# All other Hasse entries vanish: parity of x,y,z exponents in F^6.
# The nine target triples for basis x,y,z are (p(1+e_i)-1-e_j)/2;
# for i!=j one coordinate is half-integral, thus impossible.
print('PASS direct F^6 coefficients; Hasse matrix diagonal (lambda,lambda,mu).')
print('lambda coefficients:',sorted(lambda_h.items()))
print('mu coefficients:',sorted(mu_h.items()))
