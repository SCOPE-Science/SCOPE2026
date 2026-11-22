#!/usr/bin/env python3
"""Exact finite certificate for the ternary fixed-point Parikh-hole threshold."""
from math import gcd

def subst(s):
    return ''.join(c+c+str((int(c)+1)%3) for c in s)

def hull(points):
    p=sorted(points)
    def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for q in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],q)<=0:lo.pop()
        lo.append(q)
    for q in p[::-1]:
        while len(hi)>=2 and cross(hi[-2],hi[-1],q)<=0:hi.pop()
        hi.append(q)
    return lo[:-1]+hi[:-1]

def area_bound(poly):
    twice=0;bound=0
    for a,b in zip(poly,poly[1:]+poly[:1]):
        twice+=a[0]*b[1]-a[1]*b[0]
        bound+=gcd(abs(a[0]-b[0]),abs(a[1]-b[1]))
    return abs(twice),bound

def on_or_inside(q,poly):
    return all((b[0]-a[0])*(q[1]-a[1])-(b[1]-a[1])*(q[0]-a[0])>=0 for a,b in zip(poly,poly[1:]+poly[:1]))

def factor_parikh(blocks):
    L=len(blocks[0]); S=set()
    for a in blocks:
        for b in blocks:
            z=a+b;v=[z[:L].count(str(j)) for j in range(3)]
            for t in range(L+1):
                S.add(tuple(v))
                if t<L:
                    v[int(z[t])]-=1;v[int(z[t+L])]+=1
    return S

B=['0','1','2']
expected_counts=[3,10,37,115]
expected_holes=[0,0,0,21]
for m in range(4):
    N=len(B[0]); S=factor_parikh(B)
    P=hull([(a,b) for a,b,c in S]); twice,bound=area_bound(P)
    lattice=(twice+bound)//2+1
    holes={ (a,b,N-a-b) for a in range(N+1) for b in range(N-a+1) if on_or_inside((a,b),P) and (a,b,N-a-b) not in S}
    # Independent scan of a long one-sided fixed-point prefix, enough to contain every possible adjacent pair of blocks.
    Z='0'
    while len(Z)<N*500:Z=subst(Z)
    direct=set()
    v=[Z[:N].count(str(i)) for i in range(3)]
    for t in range(len(Z)-N+1):
        direct.add(tuple(v))
        if t<len(Z)-N:
            v[int(Z[t])]-=1;v[int(Z[t+N])]+=1
    assert direct==S, ('direct scan',m)
    assert len(S)==expected_counts[m] and len(holes)==expected_holes[m],m
    if m==3:
        assert len(P)==9 and lattice==136
        roots={(3,13,11),(3,15,9),(4,15,8),(5,7,15),(5,10,12),(6,6,15),(6,10,11)}
        cyc=lambda t:{t,(t[1],t[2],t[0]),(t[2],t[0],t[1])}
        assert holes==set().union(*(cyc(t) for t in roots))
        assert sum(1 for x in S if x[0]==15)==3
    print(f'm={m}, length={N}, Parikh vectors={len(S)}, hull lattice points={lattice}, holes={len(holes)}, vertices={len(P)}')
    B=[subst(s) for s in B]
print('PASS: all assertions and two independent enumerations agree.')
