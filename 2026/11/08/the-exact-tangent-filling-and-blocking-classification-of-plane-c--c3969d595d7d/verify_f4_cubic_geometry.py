#!/usr/bin/env python3
"""Independent incidence and factorization classification for cubic forms over F_4.

Usage: python3 verify_f4_cubic_geometry.py candidate_masks.txt
The input is emitted by verify_f4_cubic_census.cpp. All arithmetic is exact.
"""
from itertools import combinations
from collections import Counter
import sys

M=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
def mul(a,b): return M[a][b]
def sq(a): return mul(a,a)
def normalize(v):
    u=next(t for t in v if t)
    inv=sq(u)   # in F_4^*, u^3=1
    return tuple(mul(inv,t) for t in v)

P=[(1,a,b) for a in range(4) for b in range(4)]+[(0,1,b) for b in range(4)]+[(0,0,1)]
assert len(P)==len(set(P))==21
I={p:i for i,p in enumerate(P)}
L=[sum(1<<i for i,(x,y,z) in enumerate(P)
       if mul(a,x)^mul(b,y)^mul(c,z)==0)
   for a,b,c in P]
assert len(set(L))==21 and all(l.bit_count()==5 for l in L)
E3=((3,0,0),(0,3,0),(0,0,3),(2,1,0),(2,0,1),
    (1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1))
E2=((2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1))
C3={e:i for i,e in enumerate(E3)}
def mon(p,e):
    r=1
    for t,k in zip(p,e):
        for _ in range(k):r=mul(r,t)
    return r
MON3=[[mon(p,e) for e in E3] for p in P]
MON2=[[mon(p,e) for e in E2] for p in P]

def coeffs(mask,k):
    return tuple(mask>>(2*i)&3 for i in range(k))
def maskof(c):
    c=normalize(c)
    return sum(v<<(2*i) for i,v in enumerate(c))
def pointmask(mask,kind=3):
    c=coeffs(mask,10 if kind==3 else 6)
    A=MON3 if kind==3 else MON2
    return sum(1<<i for i,row in enumerate(A)
               if not sum_gf4(mul(x,y) for x,y in zip(c,row)))
def sum_gf4(items):
    v=0
    for t in items:v^=t
    return v

# Every cubic with nonsingular rational points and either incidence property.
with open(sys.argv[1],encoding='ascii') as inp:
    cand={int(s.strip()) for s in inp if s.strip()}
assert len(cand)==6328

# Independent enumeration of small blocking configurations in PG(2,4).
small={}; unit=[]
for n in (7,8,9):
    good=[]
    for ss in combinations(range(21),n):
        b=sum(1<<i for i in ss)
        if all(0<(b&l).bit_count()<=3 for l in L):good.append(b)
    small[n]=len(good)
    if n==9:
        unit=[b for b in good if all((b&l).bit_count() in (1,3) for l in L)]
assert small=={7:360,8:0,9:280},small
assert len(unit)==280

# A conic is nonsingular iff its F_4-points are a 5-arc. In this degree
# any split/repeated conic has 9, 1, or 5 collinear F_4-points instead.
conics=[]
for raw in range(1,4**6):
    c=coeffs(raw,6)
    if next((a for a in c if a),0)!=1:continue
    b=pointmask(raw,2)
    if b.bit_count()==5 and all((b&line).bit_count()<=2 for line in L):
        conics.append((raw,b))
assert len(conics)==1008,len(conics)

def product(line,qmask):
    q=coeffs(qmask,6)
    ans=[0]*10
    for i,a in enumerate(line):
        for j,b in enumerate(q):
            exp=list(E2[j]);exp[i]+=1
            ans[C3[tuple(exp)]]^=mul(a,b)
    return maskof(ans)

products=set(); product_pointsets=set(); exterior_lines=Counter()
for q,b in conics:
    exterior=0
    for j,line in enumerate(L):
        if not (b&line):
            exterior+=1
            m=product(P[j],q)
            products.add(m)
            product_pointsets.add(pointmask(m))
    exterior_lines[exterior]+=1
assert exterior_lines=={6:1008},exterior_lines
assert len(products)==len(product_pointsets)==6048
assert products<=cand

hermitian=maskof((1,1,1,0,0,0,0,0,0,0))
H=pointmask(hermitian)
assert H.bit_count()==9 and H in unit and hermitian in cand
smooth_candidates=cand-products
assert len(smooth_candidates)==280
smooth_pointsets=[pointmask(m) for m in smooth_candidates]
assert len(set(smooth_pointsets))==280
assert set(smooth_pointsets)==set(unit)

# Check two full projective orbits by exact matrices, without using cubic
# coefficient substitution. A rationally smooth candidate is uniquely
# recovered from its rational point-set within each of these two classes.
def det(a,b,c):
    return (mul(a[0],mul(b[1],c[2])^mul(b[2],c[1]))
          ^ mul(a[1],mul(b[0],c[2])^mul(b[2],c[0]))
          ^ mul(a[2],mul(b[0],c[1])^mul(b[1],c[0])))

# Representative of an exterior line plus nonsingular conic.
LQ=product((0,0,1),maskof((1,2,1,1,0,0)))
assert LQ in products
Qpt=pointmask(LQ)
orbit_h=set();orbit_q=set();ng=0
for a in P:
    for b0 in P:
        for c0 in P:
            if not det(a,b0,c0):continue
            for u in (1,2,3):
                b=tuple(mul(u,t) for t in b0)
                for v in (1,2,3):
                    c=tuple(mul(v,t) for t in c0)
                    perm=[]
                    for x,y,z in P:
                        q=normalize(tuple(mul(x,a[j])^mul(y,b[j])^mul(z,c[j]) for j in range(3)))
                        perm.append(I[q])
                    orbit_h.add(sum(1<<perm[j] for j in range(21) if H>>j&1))
                    orbit_q.add(sum(1<<perm[j] for j in range(21) if Qpt>>j&1))
                    ng+=1
assert ng==60480,ng
assert orbit_h==set(unit)
assert orbit_q==product_pointsets
assert len(orbit_h)==280 and len(orbit_q)==6048
assert ng//len(orbit_h)==216 and ng//len(orbit_q)==10
print('F4_CUBIC_INDEPENDENT_GEOMETRY_PASS',ng,len(conics),len(products),len(orbit_h),len(orbit_q), flush=True)
