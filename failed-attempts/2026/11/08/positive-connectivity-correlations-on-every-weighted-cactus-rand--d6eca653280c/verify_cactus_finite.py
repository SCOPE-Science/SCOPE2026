"""Exact, standalone checks for cycle connection inequalities and cactus random-cluster laws.
No external modules. The analytic proof is in RESULT.md; these finite tests are diagnostics.
"""
from fractions import Fraction as Q
from itertools import combinations, product

NASSERT=0

def check(statement, detail=''):
    global NASSERT
    NASSERT += 1
    if not statement:
        raise AssertionError(detail or 'check failed')

def connected(n, edges, selected, x, y):
    par=list(range(n))
    def root(a):
        while par[a]!=a:
            a=par[a]
        return a
    for i,(u,v) in enumerate(edges):
        if selected & (1<<i):
            a,b=root(u),root(v)
            par[a]=b
    return root(x)==root(y)

def moments(n, edges, q, weights):
    M=len(edges)
    events=list(combinations(range(n),2))
    probs=[]
    for mask in range(1<<M):
        par=list(range(n))
        def rt(a):
            while par[a]!=a:a=par[a]
            return a
        for j,(u,v) in enumerate(edges):
            if mask>>j&1: par[rt(u)]=rt(v)
        clusters=len(set(rt(i) for i in range(n)))
        w=q**clusters
        for i,z in enumerate(weights):
            if mask>>i&1:w*=z
        probs.append((w,{(u,v):rt(u)==rt(v) for u,v in events}))
    Z=sum(w for w,_ in probs)
    single={e:sum(w for w,F in probs if F[e]) for e in events}
    for e in events:
        for f in events:
            both=sum(w for w,F in probs if F[e] and F[f])
            check(Z*both >= single[e]*single[f],f'negative covariance {e} {f} q={q} weights={weights}')
    return Z

# Exact rational tests for all terminal-pair choices on cycles, positive q, heterogeneous edge weights.
for n in (3,4,5,6):
    E=[(i,(i+1)%n) for i in range(n)]
    for q in (Q(1,7),Q(1,2),Q(1),Q(3)):
        for scale in (0,1):
            weights=[Q((i+2)%5+1,(i*2+3)%7+1) if scale else Q(1) for i in range(n)]
            moments(n,E,q,weights)

# Two cycle blocks joined by a bridge; two cycles sharing one articulation vertex.
models=[(7,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,3)]),
        (5,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2)])]
for n,E in models:
    for q in (Q(1,11),Q(1,2),Q(1),Q(5)):
        for scale in (0,1,2):
            weights=[Q(1) if scale==0 else Q((i+3)*((i%3)+1),i+2) if scale==1 else Q(i+2,2*i+3) for i in range(len(E))]
            moments(n,E,q,weights)

# A proper graph which is not a cactus is intentionally not asserted here.
print('PASS:',NASSERT,'exact rational covariance assertions')
