#!/usr/bin/env python3
"""Independent 27-line incidence and skew-six checks in two characteristics.

Each line is constructed parametrically, not by the point-multiplicity formula.
Run: python verify_line_geometry.py
"""
from itertools import combinations
from collections import Counter

MATCHINGS=(((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2)))
# Coefficients are powers of a primitive cube root omega in the base field.

def line_points(p, omega, char2, matching, i, j):
    ((a,b),(c,d))=MATCHINGS[matching]
    if char2:
        add=lambda x,y:x^y
        def mul(x,y):
            out=0
            while y:
                if y&1:out^=x
                y>>=1;x<<=1
                if x&4:x^=0b111
            return out
        neg=lambda x:x
        inv=lambda x:power(x,p-2)
    else:
        mul=lambda x,y:x*y%p
        neg=lambda x:-x%p
        inv=lambda x:pow(x,p-2,p)
    def power(x,n):
        out=1
        while n:
            if n&1:out=mul(out,x)
            x=mul(x,x);n>>=1
        return out
    u=power(omega,i);v=power(omega,j)
    pts=set()
    for s in range(p):
        for t in range(p):
            if not s and not t:continue
            x=[0]*4
            x[b]=s;x[a]=neg(mul(u,s))
            x[d]=t;x[c]=neg(mul(v,t))
            k=next(z for z in x if z)
            x=tuple(mul(z,inv(k)) for z in x)
            pts.add(x)
    assert len(pts)==p+1
    return pts

SKEW_SIX = ((0,0,0),(0,1,1),(0,2,2),(1,0,1),(1,1,2),(1,2,0))
for size,omega,char2 in ((7,2,False),(4,2,True)):
    lines = {(m,i,j):line_points(size,omega,char2,m,i,j)
             for m in range(3) for i in range(3) for j in range(3)}
    assert len(lines)==27 and len(set(frozenset(S) for S in lines.values()))==27
    frequencies=Counter()
    for pts in lines.values():
        for point in pts:frequencies[point]+=1
    counts=Counter(frequencies.values())
    target={3:45} if char2 else {2:81,3:18,1:0} # only incidence pts checked
    assert all(x<=3 for x in frequencies.values())
    if char2:
        assert counts=={3:45}
    else:
        assert counts=={3:18,2:81} # for q=7 there are no single-line pts
    meetings=sum(bool(a & b) for a,b in combinations(lines.values(),2))
    assert meetings==135
    assert all(not (lines[a] & lines[b]) for a,b in combinations(SKEW_SIX,2))
    print('OK GF(%d): %d lines; %d meeting pairs; geometric incidences %s; skew six verified'%
          (size,len(lines),meetings,dict(counts)))
print('Independent line-geometry checks: PASS')
