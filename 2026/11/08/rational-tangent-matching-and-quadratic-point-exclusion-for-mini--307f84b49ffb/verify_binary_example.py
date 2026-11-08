#!/usr/bin/env python3
"""Exact finite-field checks for a (3,4) space-filling complete intersection over F2.
Uses GF(4)=GF(2)[a]/(a^2+a+1); no dependencies beyond Python stdlib.
The source's geometric smoothness assertion is not verified by this finite check.
"""
from itertools import product, combinations

def m(a,b):
    v=0
    if b&1:v^=a
    if b&2:v^=a<<1
    if v&8:v^=12
    if v&4:v^=7
    return v

def p(a,n):
    s=1
    for _ in range(n):s=m(s,a)
    return s

def addvec(a,b):return tuple(x^y for x,y in zip(a,b))

def scale(a,c):return tuple(m(c,x) for x in a)

def normalize(a):
    inv={1:1,2:3,3:2}
    d=next(x for x in a if x)
    return scale(a,inv[d])

def projective(k):
    return sorted({normalize(v) for v in product(range(k),repeat=4) if any(v)})

def phi(v,i,j):return m(p(v[i],2),v[j])^m(v[i],p(v[j],2))

def g(v):return phi(v,0,1)^phi(v,2,3)

def f(v):
    x,y,z,w=v
    A=m(x^z,phi(v,0,2))
    B=m(y^z^w,phi(v,0,3))
    C=m(x^y^z^w,phi(v,1,2))
    D=m(z^w,phi(v,1,3))
    E=m(y,phi(v,2,3))
    return A^B^C^D^E

def gradient(v,func):
    x,y,z,w=v
    if func=='g':return (y,x,w,z)
    # At F2-rational points each Frobenius minor vanishes; only the
    # linear coefficient times the minor gradient survives.
    out=[0]*4
    terms=[(x^z,0,2),(y^z^w,0,3),(x^y^z^w,1,2),(z^w,1,3),(y,2,3)]
    for coefficient,i,j in terms:
        out[i]^=coefficient*v[j]
        out[j]^=coefficient*v[i]
    return tuple(out)

P=projective(2);P4=projective(4)
assert len(P)==15 and len(P4)==85
assert all(g(u)==0 and f(u)==0 for u in P)
lines=[]
for a,b in combinations(P,2):
    L=frozenset((a,b,addvec(a,b)))
    if L not in lines:lines.append(L)
assert len(lines)==35
iso=[]
for L in lines:
    a,b=list(L)[:2]
    nonrational=normalize(addvec(a,scale(b,2)))
    if g(nonrational)==0:iso.append(L)
assert len(iso)==15
fg2=[u for u in P4 if g(u)==0 and f(u)==0]
assert len(fg2)==15 and set(fg2)==set(P)
line_tangents={}
for u in P:
    dg=gradient(u,'g');df=gradient(u,'f')
    assert any(x for x in dg) and df!=dg and any(x for x in df)
    possible=[]
    for L in lines:
        if u not in L:continue
        w=next(x for x in L if x!=u)
        if all(sum(a*b for a,b in zip(d,w))%2==0 for d in (dg,df)):
            possible.append(L)
    assert len(possible)==1
    line_tangents[u]=possible[0]
assert len(set(line_tangents.values()))==15
assert set(line_tangents.values())==set(iso)
# each isotropic line has exactly one point where it is tangent
assert all(sum(line_tangents[u]==L for u in L)==1 for L in iso)
print('F2_LINE_SECTION_CHECK_PASS',len(P),'rational points,',len(lines),'rational lines,',len(iso),'isotropic lines')
print('F2_TANGENT_MATCHING_PASS',len(line_tangents),'distinct tangent lines, exactly all isotropic lines')
print('F4_NO_QUADRATIC_POINTS_PASS',len(fg2),'F4 points equal F2 points')
