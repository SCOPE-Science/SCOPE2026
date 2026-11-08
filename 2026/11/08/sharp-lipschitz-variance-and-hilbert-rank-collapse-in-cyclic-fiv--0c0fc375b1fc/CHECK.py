"""Exact finite certificate for the five-point cyclic metric variance theorem.

Run with Python 3.10+ and no third-party dependencies. All comparisons
for the scalar part are exact rational operations, valid for a continuum
of real parameters, not just a parameter grid.
"""
from itertools import product
from fractions import Fraction as Q
from collections import Counter, defaultdict

N=5

def d(i,j):
    assert i!=j
    return (1,0) if (i-j)%N in (1,4) else (0,1)

def edges_from_prufer(word):
    degree=[1]*N
    for k in word: degree[k]+=1
    edges=[]
    for k in word:
        i=next(i for i in range(N) if degree[i]==1)
        edges.append((i,k))
        degree[i]-=1
        degree[k]-=1
    u,v=[i for i in range(N) if degree[i]==1]
    return edges+[(u,v)]

def bound(a,b,c,d_,lo,hi):
    # a+b*t <= c+d_*t
    e=b-d_; f=c-a
    if e==0: return (lo,hi) if f>=0 else (None,None)
    k=Q(f,e)
    return (lo,min(hi,k)) if e>0 else (max(lo,k),hi)

def variance_poly(v):
    a=[Q(x) for x,y in v]
    b=[Q(y) for x,y in v]
    def cov(x,y):return sum(p*q for p,q in zip(x,y))/N-sum(x)*sum(y)/Q(N*N)
    return (cov(a,a),2*cov(a,b),cov(b,b))

def feasible_interval(v):
    lo,hi=Q(1),Q(2)
    for i in range(N):
        for j in range(i+1,N):
            a=v[i][0]-v[j][0]
            b=v[i][1]-v[j][1]
            c,dd=d(i,j)
            lo,hi=bound(a,b,c,dd,lo,hi)
            if lo is None or lo>hi: return None
            lo,hi=bound(-a,-b,c,dd,lo,hi)
            if lo is None or lo>hi: return None
    return lo,hi

def min_poly(poly,lo,hi):
    a,b,c=poly
    points=[lo,hi]
    if c>0:
        t=-b/(2*c)
        if lo<=t<=hi: points.append(t)
    return min(a+b*t+c*t*t for t in points)

def canon(v):
    variants=[]
    for sign in (-1,1):
        for shift in range(N):
            for orient in (-1,1):
                w=[v[(shift+orient*i)%N] for i in range(N)]
                variants.append(tuple((sign*(a-w[0][0]), sign*(b-w[0][1])) for a,b in w))
    return min(variants)

candidates={}
for word in product(range(N),repeat=N-2):
    ed=edges_from_prufer(word)
    for signs in product((-1,1),repeat=N-1):
        adj=[[] for _ in range(N)]
        for (u,v),sign in zip(ed,signs):
            a,b=d(u,v)
            adj[u].append((v,(sign*a,sign*b)))
            adj[v].append((u,(-sign*a,-sign*b)))
        vals=[None]*N
        vals[0]=(0,0)
        queue=[0]
        while queue:
            i=queue.pop()
            for j,(a,b) in adj[i]:
                if vals[j] is None:
                    vals[j]=(vals[i][0]+a,vals[i][1]+b)
                    queue.append(j)
        v=tuple(vals)
        if v in candidates: continue
        interval=feasible_interval(v)
        if interval is not None:
            candidates[v]=(interval, variance_poly(v))
assert len(candidates)==310
counts=Counter(interval for interval,q in candidates.values())
assert counts==Counter({(Q(1),Q(1)):180,(Q(1),Q(2)):70,(Q(2),Q(2)):60})

# Exact universal inequality over each candidate's full feasible parameter
# interval, not merely at sampled values.
SHARP=(Q(6,25),Q(-4,25),Q(4,25))
for v,((lo,hi),q) in candidates.items():
    delta=tuple(x-y for x,y in zip(SHARP,q))
    assert min_poly(delta,lo,hi)>=0,(v,lo,hi,q)

interior={v:q for v,((lo,hi),q) in candidates.items() if (lo,hi)==(Q(1),Q(2))}
assert len(interior)==70
orbits=defaultdict(list)
for v,q in interior.items(): orbits[canon(v)].append(q)
assert sorted(map(len,orbits.values()))==[10,10,10,20,20]
assert {(len(v),tuple(v[0])) for v in orbits.values()}=={
    (20,(Q(10,25),Q(-10,25),Q(6,25))),
    (20,(Q(14,25),Q(-14,25),Q(6,25))),
    (10,(Q(6,25),Q(-8,25),Q(6,25))),
    (10,(Q(6,25),Q(-4,25),Q(4,25))),
    (10,(Q(6,25),Q(0),Q(0)))
}

def actual_winners(t):
    vertices={}
    for v,((lo,hi),q) in candidates.items():
        if lo<=t<=hi:
            x=tuple(Q(a)+Q(b)*t for a,b in v)
            vertices[x]=q[0]+q[1]*t+q[2]*t*t
    m=max(vertices.values())
    return len(vertices),{x for x,y in vertices.items() if y==m},m

for t,nvertex,nwinning in [(Q(1),30,20),(Q(3,2),70,10),(Q(2),30,10)]:
    count,winning,m=actual_winners(t)
    assert count==nvertex and len(winning)==nwinning
    assert m==SHARP[0]+SHARP[1]*t+SHARP[2]*t*t
    if Q(1)<t<Q(2):
        basic=(Q(0),Q(1),t,Q(1),Q(0))
        rotations=set()
        for shift in range(N):
            for sign in (-1,1):
                w=[sign*basic[(i+shift)%N] for i in range(N)]
                rotations.add(tuple(a-w[0] for a in w))
        assert winning==rotations

print('PRUFER_SIGN_CASES_EXHAUSTIVE',N**(N-2)*2**(N-1))
print('ALL_FEASIBLE_AFFINE_VERTEX_FAMILIES',len(candidates))
print('INTERIOR_VERTEX_ORBIT_SIZES',sorted(map(len,orbits.values())))
print('ALL_CONTINUUM_SCALAR_VARIANCE_INEQUALITIES_EXACT')
print('ENDPOINT_AND_INTERIOR_OPTIMIZER_COUNTS_EXACT')
print('C5_SCALAR_CERTIFICATE_PASSED')
