"""Distribution-free exact checks for mutual minimum edge covariances on finite graphs.
Run: python VERIFY.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial
from random import Random

checks=0

def check(cond, message):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(message)

def derived(edges):
    edges = tuple(tuple(sorted(e)) for e in edges)
    ed = set(edges)
    stars={e:{f for f in edges if set(e)&set(f)} for e in edges}
    alpha={e:len(stars[e]) for e in edges}
    probs={e:F(1,alpha[e]) for e in edges}
    joint={}
    for e,f in combinations(edges,2):
        if set(e)&set(f):
            j=F(0)
        else:
            a,b=alpha[e],alpha[f]
            h=len(stars[e]&stars[f])
            j=F(a+b,a*b*(a+b-h))
        joint[(e,f)]=j
    return probs,joint

def empirical(edges):
    edges=tuple(sorted(edges))
    m=len(edges)
    hits={e:0 for e in edges}
    pairs={(e,f):0 for e,f in combinations(edges,2)}
    for order in permutations(edges):
        rank={e:i for i,e in enumerate(order)}
        selected={e for e in edges if all(rank[e]<rank[f] for f in edges if f!=e and set(e)&set(f))}
        for e in selected:hits[e]+=1
        for e,f in combinations(sorted(selected),2):pairs[(e,f)]+=1
    total=factorial(m)
    return {e:F(n,total) for e,n in hits.items()}, {(e,f):F(n,total) for (e,f),n in pairs.items()}

# Every simple graph on up to four vertices; each graph with <=6 edges is enumerated over ALL orderings.
for n in range(2,5):
    possible=list(combinations(range(n),2))
    for mask in range(1<<len(possible)):
        es=tuple(possible[i] for i in range(len(possible)) if mask & (1<<i))
        probs,joint=derived(es)
        ep,ej=empirical(es)
        for e in es:check(probs[e]==ep[e],f'marginal {n} {mask} {e}')
        for p in joint:check(joint[p]==ej[p],f'joint {n} {mask} {p}: {joint[p]} {ej[p]}')

# Sparse five- and six-vertex graphs including triangles, four-cycles and mixed degree patterns.
rng=Random(31522)
for n,m,tries in [(5,6,70),(6,6,50),(6,7,30)]:
    possible=list(combinations(range(n),2))
    for z in range(tries):
        es=tuple(sorted(rng.sample(possible,m)))
        probs,joint=derived(es)
        ep,ej=empirical(es)
        for e in es:check(probs[e]==ep[e],f'marginal {n} {z} {e}')
        for p in joint:check(joint[p]==ej[p],f'joint {n} {z} {p}')

# Exact mean/variance equality for cycles and paths of all 5 <= n <= 50.
def moments(edges):
    ps,j=derived(edges)
    mean=sum(ps.values(),F(0))
    variance=sum((p*(1-p) for p in ps.values()),F(0))+2*sum((z-ps[e]*ps[f] for (e,f),z in j.items()),F(0))
    return mean,variance
for n in range(5,51):
    path=[(i,i+1) for i in range(n-1)]
    cycle=path+[(0,n-1)]
    for label,es in [('path',path),('cycle',cycle)]:
        a,b=moments(es)
        check(a==F(n,3),f'{label} mean n={n}: {a}')
        check(b==F(2*n,45),f'{label} variance n={n}: {b}')

# Global covariance sign and independence iff induced matching are exact algebraic consequences.
for n in range(2,9):
    possible=list(combinations(range(n),2))
    for trial in range(40):
        es=tuple(sorted(e for e in possible if rng.randrange(2)))
        ps,j=derived(es)
        for (e,f),joint in j.items():
            cov=joint-ps[e]*ps[f]
            if set(e)&set(f): sign=-1
            else:
                h=sum(bool(set(g)&set(e)) and bool(set(g)&set(f)) for g in es)
                sign=1 if h else 0
            check((cov>0)-(cov<0)==sign, f'covariance sign n={n}, {e}, {f}')

print(f'VERIFY_OK {checks} assertions')

# Four-cycle variance formula for triangle-free regular host graphs.
def four_cycles(edges):
    vs=sorted(set(x for e in edges for x in e))
    ne={v:set() for v in vs}
    for u,v in edges:
        ne[u].add(v)
        ne[v].add(u)
    twice=0
    for u,v in combinations(vs,2):
        k=len(ne[u]&ne[v])
        twice+=k*(k-1)//2
    check(twice%2==0,'four-cycle parity')
    return twice//2

def regular_formula(edges):
    vs=sorted(set(x for e in edges for x in e))
    deg={v:0 for v in vs}
    for u,v in edges:
        deg[u]+=1;deg[v]+=1
    d=deg[vs[0]]
    check(d>=2 and all(x==d for x in deg.values()),'not regular')
    es=set(tuple(sorted(e)) for e in edges)
    for a,b,c in combinations(vs,3):
        check(not all(tuple(sorted(e)) in es for e in [(a,b),(b,c),(a,c)]),'triangle')
    m=len(es)
    q=four_cycles(es)
    return F(2*m*(d-1)**2,(2*d-1)**2*(4*d-3))+F(2*q,(d-1)*(2*d-1)**2*(4*d-3))

for d in range(2,9):
    es=[(i,d+j) for i in range(d) for j in range(d)]
    target=regular_formula(es)
    check(moments(es)[1]==target,'Kdd variance')
    check(moments(es)[1]==F(d*d*(d-1),2*(2*d-1)**2),'Kdd simplified variance')

petersen=[tuple(sorted((i,(i+1)%5))) for i in range(5)]+[tuple(sorted((5+i,5+(i+2)%5))) for i in range(5)]+[(i,5+i) for i in range(5)]
check(four_cycles(petersen)==0,'Petersen 4-cycles')
check(moments(petersen)[1]==regular_formula(petersen),'Petersen variance')

fano=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
heawood=[(v,7+j) for j,block in enumerate(fano) for v in block]
check(four_cycles(heawood)==0,'Heawood 4-cycles')
check(moments(heawood)[1]==regular_formula(heawood),'Heawood variance')

print(f'REGULAR_FORMULA_OK {checks} assertions total')
