#!/usr/bin/env python3
"""Exact finite determinant tests and independent seeded sampling checks."""
import itertools, math, random

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def matching(labels):
    if not labels:
        yield ()
        return
    a=labels[0]
    for i in range(1,len(labels)):
        for rest in matching(labels[1:i]+labels[i+1:]):
            yield ((a,labels[i]),)+rest

MATCH=tuple(matching(tuple(range(6))))
assert len(MATCH)==15
TRI=tuple(itertools.combinations(range(6),3))
COMPL=tuple((t,tuple(i for i in range(6) if i not in t)) for t in TRI if 0 in t)
assert len(COMPL)==10

def six_defect(v):
    p={t:abs(det(*(v[i] for i in t))) for t in TRI}
    a=2*sum(p[t]*p[u] for t,u in COMPL)
    b=sum(abs(det(*(cross(v[i],v[j]) for i,j in m))) for m in MATCH)
    return a-b

def full_defect(v):
    n=len(v)
    triples=itertools.combinations(range(n),3)
    vol=sum(abs(det(*(v[i] for i in t))) for t in triples)
    pairs=tuple(cross(v[i],v[j]) for i,j in itertools.combinations(range(n),2))
    w=sum(abs(det(pairs[i],pairs[j],pairs[k])) for i,j,k in itertools.combinations(range(len(pairs)),3))
    return vol*vol-w

# Exact arithmetic for six- and seven-generator examples; compare both routes.
CASES=[
 [(2,1,0),(0,3,1),(1,0,2),(2,1,3),(-1,2,1),(1,-2,3)],
 [(1,2,3),(2,-1,1),(3,1,-2),(1,4,0),(-2,1,1),(1,-1,5),(3,2,-1)],
 [(1,0,0),(0,1,0),(0,0,1),(1,1,1),(-1,1,2),(2,-1,1),(1,2,-1)]
]
for vecs in CASES:
    n=len(vecs)
    res=full_defect(vecs)
    pieces=sum(six_defect([vecs[i] for i in s]) for s in itertools.combinations(range(n),6))
    assert res==pieces and res>=0,(res,pieces)
    print('integer n',n,'defect',res,'six-subsets',math.comb(n,6))
for n in (3,4,5):
    assert full_defect(CASES[1][:n])==0
print('exact finite determinant checks PASS')

# Monte Carlo probes are NOT proof; they check normalization of the analytic coefficient.
rng=random.Random(777221)
def sphere():
    z=2*rng.random()-1
    t=2*math.pi*rng.random()
    a=math.sqrt(1-z*z)
    return (a*math.cos(t),a*math.sin(t),z)
N=18000
s=ss=0.0
for k in range(N):
    value=six_defect([sphere() for _ in range(6)])
    s+=value;ss+=value*value
mean=s/N
se=math.sqrt(max(0.,ss/N-mean*mean)/N)
target=5*math.pi**2*(32-3*math.pi**2)/512
print('MC six-defect',mean,'standard error',se,'exact target',target)
assert abs(mean-target)<max(0.035,7*se)
print('ALL_CHECKS_PASSED')
