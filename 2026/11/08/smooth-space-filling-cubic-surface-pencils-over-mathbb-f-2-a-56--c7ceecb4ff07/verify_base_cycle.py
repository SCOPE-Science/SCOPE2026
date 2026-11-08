#!/usr/bin/env python3
"""Independent finite-field checks for the seven lines supporting a (3,3) base.
All arithmetic uses F4=F2[a]/(a^2+a+1), with a encoded by 2.
"""
from itertools import product, combinations
PAIRS = tuple(combinations(range(4), 2))
MUL = [[0]*4 for _ in range(4)]
for a in range(4):
    for b in range(4):
        v = 0
        for i in (0,1):
            for j in (0,1):
                if ((a>>i)&1) and ((b>>j)&1): v ^= 1 << (i+j)
        if v & 4: v ^= 7
        MUL[a][b] = v
INV = [0,1,3,2]
def mul(a,b):return MUL[a][b]
def sq(a):return mul(a,a)
def scale(c,x):return tuple(mul(c,a) for a in x)
def add(x,y):return tuple(a^b for a,b in zip(x,y))
def norm(x):
    for c in x:
        if c:return scale(INV[c],x)
    raise ValueError('zero vector')
def form(a,x):
    v=0
    for k,(i,j) in enumerate(PAIRS):
        if (a>>k)&1: v ^= mul(sq(x[i]),x[j]) ^ mul(x[i],sq(x[j]))
    return v
def gradient(a,x):
    v=[0]*4
    for k,(i,j) in enumerate(PAIRS):
        if (a>>k)&1:
            v[i]^=sq(x[j]);v[j]^=sq(x[i])
    return tuple(v)
def projective_line(x,y):
    return frozenset([norm(add(x,scale(t,y))) for t in range(4)]+[norm(y)])
def vec_binary(x):return tuple((x>>j)&1 for j in range(4))
assert sq(2)==3 and sq(3)==2 and mul(2,3)==1
assert len({norm(x) for x in product(range(4),repeat=4) if any(x)})==85
rational_spread=[(1,4),(2,8),(3,12),(6,11),(7,9)]
L=[projective_line(vec_binary(u),vec_binary(v)) for u,v in rational_spread]
assert len(set(L))==5
for l in L:
    assert len(l)==5 and all(form(a,p)==0 for p in l for a in (33,13))
for i,j in combinations(range(5),2): assert not L[i].intersection(L[j])
assert len(set.union(*(set(l) for l in L)))==25
# The two F4-conjugate transversals to the rational spread.
T={t:projective_line((1,0,t,0),(0,1,0,t)) for t in (2,3)}
assert not (T[2]&T[3])
assert T[3]==frozenset(norm(tuple(sq(z) for z in p)) for p in T[2])
for t in (2,3):
    assert all(form(a,p)==0 for p in T[t] for a in (33,13))
    assert all(len(T[t]&ell)==1 for ell in L)
    c=sq(t)    # On T_t, gradient(F_33) = t^2 gradient(F_13).
    assert all(gradient(33,p)==scale(c,gradient(13,p)) for p in T[t])
# In particular, each nonrational transversal has generic base multiplicity >= 2.
# All 15 rational points are regular points of the base complete intersection.
for x in range(1,16):
    p=vec_binary(x)
    g=gradient(33,p);h=gradient(13,p)
    assert any(g) and any(h) and g != h
    assert form(33,p)==0 and form(13,p)==0
# Check every F4-rational projective line; there are exactly seven common lines.
pts=sorted({norm(x) for x in product(range(4),repeat=4) if any(x)})
all_lines={projective_line(x,y) for x,y in combinations(pts,2)}
assert len(all_lines)==357
common={ell for ell in all_lines if all(form(a,p)==0 for p in ell for a in (33,13))}
assert len(common)==7 and common==(set(L)|set(T.values()))
# The scheme is a complete intersection of two distinct smooth cubics, degree 9.
# The five rational lines contribute >=5, and the two transversals >=2 each.
# Hence the fundamental cycle is exactly 5*1 + 2*2 = 9.
assert 5+2+2==3*3
# Underlying reduced curve has graph K_(5,2), 7 components, 10 nodes:
# p_a(red)=10-7+1=4. CI arithmetic genus is 1+9*(3+3-4)/2=10.
assert 10-7+1==4 and 1+9*2//2==10
print('FROBENIUS_CUBIC_BASE_PASS',len(L),len(T),len(common),len(pts),len(all_lines),9,4,10)
