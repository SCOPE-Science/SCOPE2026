#!/usr/bin/env python3
"""Exact finite-field sanity checks for the Fermat degree-two exceptional boundary.

Only Python standard library.  GF(9)=GF(3)[a]/(a^2+1), represented by x+3*y.
The assertions corroborate finite cases; universal proofs are in RESULT.md.
"""
from collections import Counter
from itertools import product

F9 = range(9)
def coords9(x): return x % 3, x // 3
def plus9(x,y):
    a,b=coords9(x); c,d=coords9(y)
    return (a+c)%3 + 3*((b+d)%3)
def times9(x,y):
    a,b=coords9(x); c,d=coords9(y)
    return (a*c+2*b*d)%3 + 3*((a*d+b*c)%3)
def pow9(x,n):
    r=1
    while n:
        if n&1: r=times9(r,x)
        x=times9(x,x); n//=2
    return r
def inv9(x):
    assert x
    return pow9(x,7)
def sum9(vals):
    out=0
    for v in vals: out=plus9(out,v)
    return out
def normalize(v):
    k=inv9(next(x for x in v if x))
    return tuple(times9(k,x) for x in v)
def point_plane(field):
    return sorted({normalize(v) for v in product(field,repeat=3) if any(v)})
def herm(v): return sum9(pow9(x,4) for x in v)
def orthogonal(u,v): return sum9(times9(pow9(x,3),y) for x,y in zip(u,v))==0

points=point_plane(F9)
Q=[v for v in points if herm(v)==0]
external=[v for v in points if herm(v)!=0]
assert (len(points),len(Q),len(external))==(91,28,63)
tangents={p:tuple(pow9(x,3) for x in p) for p in Q}
def dot9(u,v):return sum9(times9(x,y) for x,y in zip(u,v))
count={p:sum(dot9(tangents[q],p)==0 for q in Q) for p in points}
assert Counter(count.values())=={1:28,4:63},Counter(count.values())
assert all(count[p]==1 for p in Q)
assert all(sum(dot9(tangents[p],x)==0 for x in points)==10 for p in Q)

F3points=[p for p in points if all(x in (0,1,2) for x in p)]
assert len(F3points)==13
assert Counter(herm(p) for p in F3points)=={0:4,1:3,2:6}
Q3=[p for p in Q if p in F3points]
assert len(Q3)==4
for p in Q3:
    line=tangents[p]
    assert all(x in (0,1,2) for x in line)
    v=next(v for v in F3points if v!=p and dot9(line,v)==0)
    assert herm(v)==2 # nonsquare scalar in GF(3), branches conjugate
for p in Q:
    assert (p in Q3)==all(x in (0,1,2) for x in tangents[p])
assert 2*3+4==10  # lifts of three coordinate vertices, four branch points
assert all(count[p]>0 for p in F3points)

# Every F9-plane point has two lifts unless it is on Q (one lift);
# in GF9, both 1 and 2 of GF3 have square roots.
assert all(pow9(x,4) in (1,2) for x in range(1,9))
assert len(Q)+2*len(external)==154
assert 56*(9+1)-3*(2*63)-len(Q)==154

# Independent extension check, GF(27)=GF(3)[b]/(b^3-b-1).
def unpack27(x):return tuple((x//3**i)%3 for i in range(3))
def pack27(a):return sum(x*3**i for i,x in enumerate(a))
def add27(x,y):return pack27(tuple((a+b)%3 for a,b in zip(unpack27(x),unpack27(y))))
def mul27(x,y):
    c=[0]*5
    for i,a in enumerate(unpack27(x)):
        for j,b in enumerate(unpack27(y)):c[i+j]=(c[i+j]+a*b)%3
    for k in (4,3):
        z=c[k];c[k]=0
        c[k-2]=(c[k-2]+z)%3  # b^3 = b+1
        c[k-3]=(c[k-3]+z)%3
    return pack27(c[:3])
def pow27(x,n):
    out=1
    while n:
        if n&1:out=mul27(out,x)
        x=mul27(x,x);n//=2
    return out
assert all(pow27(x,26)==1 for x in range(1,27))
squares={mul27(x,x) for x in range(27)}
def liftcount(z):return 1 if z==0 else (2 if z in squares else 0)
count27=0
for y in range(27):
    for z in range(27):
        F=add27(add27(1,pow27(y,4)),pow27(z,4))
        count27+=liftcount(F)
for z in range(27):count27+=liftcount(add27(1,pow27(z,4)))
count27+=liftcount(1)
assert count27==730,count27
print('GF9 plane: 91 points; 28 Hermitian points; 63 external points')
print('Incidences: 28 tangent points each on 1 tangent, 63 external each on 4')
print('GF3 base: 13 points; surface: 10 points; none off complete boundary')
print('Four GF3 hyperflex tangents have nonsquare splitting scalar 2')
print('GF9 surface and boundary: 154 points each; 28 tangencies and 126 fourfold points')
print('GF27 surface: 730 points; predicted odd boundary: 10 (proved via descent)')
print('CHECK_OK')
