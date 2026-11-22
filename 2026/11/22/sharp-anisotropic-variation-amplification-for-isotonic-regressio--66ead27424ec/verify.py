"""Exact finite-face verification for anisotropic diamond isotonic regression.

Only Python standard library is required. This verifies the finite algebraic
classification; the mathematical proof explains why it applies globally.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random

EDGES=((0,1),(0,2),(1,3),(2,3))

def partitions():
    result=set()
    for mask in range(1<<len(EDGES)):
        par=list(range(4))
        def root(i):
            while par[i]!=i: i=par[i]
            return i
        for j,(u,v) in enumerate(EDGES):
            if mask>>j&1:par[root(u)]=root(v)
        blocks=tuple(sorted(tuple(i for i in range(4) if root(i)==k)
                            for k in set(root(i) for i in range(4))))
        belong={v:j for j,b in enumerate(blocks) for v in b}
        adj={j:set() for j in range(len(blocks))}
        for u,v in EDGES:
            if belong[u]!=belong[v]:adj[belong[u]].add(belong[v])
        seen=set();active=set()
        def visit(v):
            if v in active:return False
            if v in seen:return True
            active.add(v)
            for w in adj[v]:
                if not visit(w):return False
            active.remove(v);seen.add(v)
            return True
        if all(visit(v) for v in adj):result.add(blocks)
    return sorted(result)

PARTS=partitions()
assert len(PARTS)==10,PARTS

def avg(B,x):
    y=[F(0)]*4
    for b in B:
        a=sum((x[i] for i in b),F(0))/len(b)
        for i in b:y[i]=a
    return tuple(y)

def vweights(x,w):return sum((q*abs(x[u]-x[v]) for (u,v),q in zip(EDGES,w)),F(0))

def coeff(x):
    # (coefficient of r, constant coefficient) for cycle edge weights (r,1,1,r)
    d=[abs(x[u]-x[v]) for u,v in EDGES]
    return (d[0]+d[3],d[1]+d[2])

def same_rational_function(n,d,nn,dd):
    a,b=n;c,e=d;A,B=nn;C,E=dd
    return (a*C==A*c and a*E+b*C==A*e+B*c and b*E==B*e)

EXPECTED={
 '1/(r+1)':((F(0),F(1)),(F(1),F(1))),
 '1/3':((F(0),F(1)),(F(0),F(3))),
 'r/(r+1)':((F(1),F(0)),(F(1),F(1))),
 '(r+1)/3':((F(1),F(1)),(F(0),F(3))),
 '1/2':((F(0),F(1)),(F(0),F(2))),
 '1':((F(0),F(1)),(F(0),F(1))),
 '(r+1)/2':((F(1),F(1)),(F(0),F(2))),
 '(r+1)/(3r)':((F(1),F(1)),(F(3),F(0))),
 '(r+1)/(2r)':((F(1),F(1)),(F(2),F(0)))
}
found=set();cases=0
for B in PARTS:
    for bits in product((F(0),F(1)), repeat=4):
        di=coeff(bits)
        if di==(0,0):continue
        co=coeff(avg(B,bits))
        if co==(0,0):continue
        names=[k for k,(n,d) in EXPECTED.items() if same_rational_function(co,di,n,d)]
        assert len(names)==1,(B,bits,co,di,names)
        found.add(names[0]);cases+=1
assert found==set(EXPECTED),(found,set(EXPECTED)-found)
print('DIAMOND_ALL_REALIZABLE_FACES_AND_BINARY_CUT_RATIOS_PASS',len(PARTS),cases,len(found))

# Each of the nine functions is <= (r+1)/2 for r>=1.
for r in [F(1),F(11,10),F(2),F(3),F(100)]:
    w=(r,F(1),F(1),r)
    gain=max(vweights(avg(B,bits),w)/vweights(bits,w)
             for B in PARTS for bits in product((F(0),F(1)),repeat=4)
             if vweights(bits,w)>0)
    assert gain==(r+1)/2,(r,gain)
print('ANISOTROPIC_ALL_FACES_EXACT_GAIN_PASS')

# Exact QP solution: minimization of residual over the possible active equality faces.
def project(x):
    candidates=[]
    for B in PARTS:
        z=avg(B,x)
        if all(z[u]<=z[v] for u,v in EDGES):
            cost=sum((q*q for q in (x[i]-z[i] for i in range(4))),F(0))
            candidates.append((cost,z))
    assert candidates
    return min(candidates,key=lambda h:h[0])[1]

# Full nonlinear sharp witnesses with strict positive active multiplier.
for r in [F(1,5),F(1,2),F(1),F(2),F(4),F(7,3)]:
    w=(r,F(1),F(1),r)
    if r>=1:
        x=(F(1),F(1),F(-1),F(2));delta=(F(0),F(0),F(1,4),F(1,4))
    else:
        # Relabel the two incomparable middle vertices.
        x=(F(1),F(-1),F(1),F(2));delta=(F(0),F(1,4),F(0),F(1,4))
    z=tuple(x[i]+delta[i] for i in range(4))
    px=project(x);pz=project(z)
    norm=vweights(tuple(pz[i]-px[i] for i in range(4)),w)/vweights(delta,w)
    sharp=(1+max(r,1/r))/2
    assert norm==sharp,(r,norm,sharp,px,pz)
print('NONLINEAR_STRICT_ACTIVE_CHAMBER_ATTAINMENT_PASS')

rng=Random(2037)
for k in range(2200):
    x=tuple(F(rng.randint(-12,12),rng.randint(1,7)) for _ in range(4))
    y=tuple(F(rng.randint(-12,12),rng.randint(1,7)) for _ in range(4))
    r=F(rng.randint(1,25),rng.randint(1,25));w=(r,F(1),F(1),r)
    dx=tuple(x[i]-y[i] for i in range(4));dv=vweights(dx,w)
    if not dv:continue
    px=project(x);py=project(y)
    dp=tuple(px[i]-py[i] for i in range(4))
    assert vweights(dp,w)<=dv*(1+max(r,1/r))/2,(x,y,r)
print('RANDOM_EXACT_RATIONAL_NONLINEAR_TESTS_PASS',2200)
print('ALL_DIAMOND_ISOTONIC_VARIATION_CERTIFICATES_PASS')
