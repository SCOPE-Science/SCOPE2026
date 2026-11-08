#!/usr/bin/env python3
"""Exact Fourier-autocorrelation identities for the seven-site hexagonal aperture.

No external libraries. The general analytic inequality is proved in RESULT.md;
this checks its Laurent-polynomial reductions and finite equality examples.
"""
from collections import defaultdict, Counter
from itertools import product
from math import pi, cos, sin

N=4
Z=(0,)*N

def const(v): return {Z:v} if v else {}
def var(j,sign=1):
    p=[0]*N;p[j]=sign
    return {tuple(p):1}
def add(*a):
    z=defaultdict(int)
    for p in a:
        for e,v in p.items():z[e]+=v
    return {e:v for e,v in z.items() if v}
def neg(a):return {e:-v for e,v in a.items()}
def scale(a,k):return {e:k*v for e,v in a.items() if k*v}
def mul(a,b):
    z=defaultdict(int)
    for x,v in a.items():
        for y,w in b.items():z[tuple(i+j for i,j in zip(x,y))]+=v*w
    return {e:v for e,v in z.items() if v}
def conj(a):return {tuple(-i for i in e):v for e,v in a.items()}
def sq(a):return mul(a,conj(a))
O=const(1)
U,V,W,T=[var(i) for i in range(4)]
x,y,z=conj(U),conj(V),mul(conj(W),conj(T))
s=add(x,y,z)
e2=add(mul(x,y),mul(x,z),mul(y,z))
S=[(0,0),(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1)]
c=[O,O,O,U,V,W,T]
D=defaultdict(list)
for i,a in enumerate(S):
    for j,b in enumerate(S):
        D[(a[0]-b[0],a[1]-b[1])].append((i,j))
assert len(D)==19
assert Counter(len(v) for k,v in D.items() if k!=(0,0))=={1:6,2:6,4:6}
C={d:add(*(mul(c[i],conj(c[j])) for i,j in ij)) for d,ij in D.items()}
positive=[d for d in D if d>(0,0)]
assert Counter(len(D[d]) for d in positive)=={1:3,2:3,4:3}
R=sq(s)
small=add(*(sq(C[d]) for d in positive if len(D[d])==2))
large=add(*(sq(C[d]) for d in positive if len(D[d])==4))
assert small==add(const(3),R), 'two-pair correlation identity'
A=[add(O,x),add(O,y),add(x,y)]
B=[add(O,mul(z,conj(y))),add(O,mul(z,conj(x))),add(O,z)]
Tmix=add(*(mul(conj(a),b) for a,b in zip(A,B)))
expected_mix=scale(mul(add(s,e2),mul(conj(x),conj(y))),2)
assert Tmix==expected_mix,'mixed term identity'
K=add(*(add(sq(a),sq(b)) for a,b in zip(A,B)))
assert K==add(R,const(9),s,conj(s)),'norm identity'
assert large==add(K,mul(W,Tmix),mul(conj(W),conj(Tmix))),'four-pair identity'
Moment=add(*(sq(v) for v in C.values()))
assert Moment==add(const(61),scale(R,2),scale(large,2))

def numeric(coeff):
    out=0
    for ij in D.values():
        a=sum(coeff[i]*coeff[j].conjugate() for i,j in ij)
        out+=abs(a)**2
    return out

minima=[(-1,-1,1,1),(-1,1,-1,1),(1,-1,-1,1)]
seen=[]
for signs in product((-1,1),repeat=4):
    v=numeric([1,1,1,*signs])
    assert abs(v-round(v))<1e-9
    if round(v)==63:seen.append(signs)
assert sorted(seen)==sorted(minima)
assert numeric([1]*7)==175
for q in (2,3,4,5,6):
    roots=[complex(cos(2*pi*k/q),sin(2*pi*k/q)) for k in range(q)]
    eq=[]
    for idx in product(range(q),repeat=4):
        cs=[1+0j,1+0j,1+0j,*[roots[k] for k in idx]]
        v=numeric(cs)
        assert 63-1e-7<=v<=175+1e-7
        if abs(v-63)<1e-7:eq.append(idx)
    if q%2==0:assert len(eq)==3, (q,eq)
    else:assert not eq,(q,eq)

# Additional numeric checks are observational only; proof holds for all phases.
print('HEXAGON_SEVEN_L4_PASS shifts=19 single=3 double=3 quadruple=3 binary_minimizers=3')
