"""Exact checks of Euclidean radii for edge-diamond Minkowski sums.

Run with Python 3.10 or later. No third-party packages are required.
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import comb, isqrt

checks=0

def check(flag, context):
    global checks
    checks+=1
    if not flag: raise AssertionError(context)

def coverage_min_sq(n, edges, weights):
    vals=[]
    for mask in range(1,1<<n):
        k=mask.bit_count()
        w=sum((weight for (a,b),weight in zip(edges,weights) if (mask>>a)&1 or (mask>>b)&1), Fraction())
        vals.append((w*w/Fraction(k),mask))
    return min(v for v,m in vals),[m for v,m in vals if v==min(x for x,_ in vals)]

def cycle(n):
    return [(i,(i+1)%n) for i in range(n)]

def brute_outer_cycle(n):
    # Each edge chooses one signed coordinate endpoint of its cross-polytope.
    best=-1
    extrema=set()
    choices=[]
    for u,v in cycle(n):
        choices.append([(u,1),(u,-1),(v,1),(v,-1)])
    for picked in product(*choices):
        x=[0]*n
        for vertex,sgn in picked: x[vertex]+=sgn
        r2=sum(v*v for v in x)
        if r2>best:best=r2;extrema={tuple(x)}
        elif r2==best:extrema.add(tuple(x))
    return best,extrema

def expected_outer(n):
    return 2*n if n%2==0 else 2*n-1

def expected_extrema(n):
    if n%2==0:return 2*(1<<(n//2))
    return n*(1<<((n+3)//2))

# Enumerate independent support-mask minima, independently of support integrals.
for n in range(3,13):
    c,masks=coverage_min_sq(n,cycle(n),[Fraction(1)]*n)
    check(c==Fraction(n if n==3 else 4),('cycle inward',n,c))
    if n==3: check(set(masks)=={(1<<n)-1},('inward contact 3',masks))
    elif n==4: check(set(masks)=={(1<<n)-1}|{1<<j for j in range(n)},('inward contact 4',masks))
    else:check(set(masks)=={1<<j for j in range(n)},('inward contacts',n,masks))

# Exhaustively generate vertices for n<=8: verify radius and all farthest points.
for n in range(3,9):
    r2,points=brute_outer_cycle(n)
    check(r2==expected_outer(n),('outer radius',n,r2))
    check(len(points)==expected_extrema(n),('outer contacts',n,len(points)))
    for pt in points:
        check(sum(x*x for x in pt)==r2,('extremal norm',n,pt))

# A second independent optimizer for outer radius: enumerate target endpoint
# counts only, ignoring signs; arithmetic is integral.
for n in range(3,15):
    best=max(sum(sum(1 for ep,choice in enumerate(orientation) if choice==v) ** 2 for v in range(n))
             for orientation in product(*[(u,v) for u,v in cycle(n)])) if n<=11 else None
    if best is not None:check(best==expected_outer(n),('orientations',n,best))

# Exact support-function inequalities at a finite integer grid of normals.
# They are corroborative checks; the mathematical proof is all-dimensional.
for n in range(3,8):
    r2=Fraction(n if n==3 else 4)
    for u in product(range(-2,3),repeat=n):
        if not any(u):continue
        support=sum(max(abs(u[a]),abs(u[b])) for a,b in cycle(n))
        check(support*support>=r2*sum(t*t for t in u),('support bound',n,u))

# Weighted, noncycle graph instances: exact coverage bound and its
# sharpness at every winning indicator, on small graphs.
for n in range(2,6):
    all_edges=list(combinations(range(n),2))
    for mask in range(1,1<<len(all_edges)):
        edges=[e for j,e in enumerate(all_edges) if (mask>>j)&1]
        if any(not any(i in e for e in edges) for i in range(n)):continue
        weights=[Fraction(1+(j%3),1+(j%2)) for j in range(len(edges))]
        r2,ms=coverage_min_sq(n,edges,weights)
        for win in ms:
            cov=sum((w for w,e in zip(weights,edges) if any((win>>v)&1 for v in e)),Fraction())
            check(cov*cov==r2*win.bit_count(),('equality',n,win))
        for u in product(range(-1,2),repeat=n):
            if not any(u):continue
            h=sum(w*max(abs(u[a]),abs(u[b])) for (a,b),w in zip(edges,weights))
            check(h*h>=r2*sum(t*t for t in u),('weighted support',n,u))

print('PASS',checks,'exact integer/rational assertions')

# Mixed hyperedge families: compare unrestricted assignments/signs against
# maximum-over-orders formula for the circumball.
def general_outer_sq(n, sets, ws):
    best=Fraction(-1)
    for picks in product(*[[(i,s) for i in a for s in [-1,1]] for a in sets]):
        x=[Fraction() for _ in range(n)]
        for (i,s),w in zip(picks,ws): x[i]+=s*w
        best=max(best,sum(t*t for t in x))
    return best

def order_outer_sq(n, sets, ws):
    best=Fraction(-1)
    for perm in permutations(range(n)):
        loc={j:i for i,j in enumerate(perm)}
        x=[Fraction() for _ in range(n)]
        for a,w in zip(sets,ws):x[max(a,key=lambda j:loc[j])]+=w
        best=max(best,sum(t*t for t in x))
    return best
from itertools import permutations
from random import Random
rng=Random(1729)
for n in range(2,6):
    all_sets=[s for sz in range(1,min(n,3)+1) for s in combinations(range(n),sz)]
    for trial in range(36):
        sz=rng.randint(1,4)
        sets=[rng.choice(all_sets) for _ in range(sz)]
        ws=[Fraction(rng.randint(1,4),rng.randint(1,3)) for _ in sets]
        a=general_outer_sq(n,sets,ws)
        b=order_outer_sq(n,sets,ws)
        check(a==b,('weighted hypergraph',n,sets,ws,a,b))
print('PASS total',checks,'assertions including weighted hypergraph outer-radii')
