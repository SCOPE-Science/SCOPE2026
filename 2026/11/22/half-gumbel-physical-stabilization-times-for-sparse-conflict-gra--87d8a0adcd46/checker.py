"""Finite exact checks for the edge-clock stabilization identity.
Run: python checker.py. Finite tests support, but do not prove, the limit theorem.
"""
from itertools import permutations, product
from fractions import Fraction
from math import comb

checks=0

def check(cond,context):
    global checks
    if not cond:
        raise AssertionError(context)
    checks+=1


def edges_of(n,mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return [e for bit,e in enumerate(pairs) if mask>>bit & 1]


def independent(n,edges,selected):
    return all(not (selected>>u&1 and selected>>v&1) for u,v in edges)

for n in range(1,5):
    pcount=comb(n,2)
    for mask in range(1<<pcount):
        edges=edges_of(n,mask)
        for colors in product(range(3),repeat=n):
            H=[(u,v) for u,v in edges if colors[u]==colors[v]]
            for order in permutations(range(n)):
                current=list(colors)
                fired=set()
                for j in range(n+1):
                    actual=not any(current[u]==current[v] for u,v in edges)
                    theoretical=not any(u not in fired and v not in fired for u,v in H)
                    check(actual==theoretical,(n,mask,colors,order,j))
                    if j==n: break
                    v=order[j]
                    if any((u==v and current[u]==current[w]) or (w==v and current[u]==current[w]) for u,w in edges):
                        prohibited={current[w] for u,w in edges if u==v}
                        prohibited|={current[u] for u,w in edges if w==v}
                        current[v]=next(c for c in range(max(3,n+1)) if c not in prohibited)
                    fired.add(v)
print('pathwise scheduler checks:',checks)

# Exact rational CDF from independence-polynomial counts and explicit
# retained-set enumeration, for every simple labelled graph of order <= 5.
for n in range(1,6):
    for mask in range(1<<comb(n,2)):
        edges=edges_of(n,mask)
        for q in [Fraction(1,3),Fraction(1,2),Fraction(2,3)]:
            left=sum(q**s.bit_count()*(1-q)**(n-s.bit_count()) for s in range(1<<n) if independent(n,edges,s))
            counts=[sum(s.bit_count()==k and independent(n,edges,s) for s in range(1<<n)) for k in range(n+1)]
            right=(1-q)**n*sum(counts[k]*(q/(1-q))**k for k in range(n+1))
            check(left==right,(n,mask,q))

# Dependency-pair counts b1 and b2 for the Stein--Chen graph.
for n in range(2,6):
    for mask in range(1<<comb(n,2)):
        edges=edges_of(n,mask)
        m=len(edges)
        degrees=[sum(v in e for e in edges) for v in range(n)]
        D2=sum(d*(d-1) for d in degrees)
        adjacent_ordered=sum(bool(set(e)&set(f)) for e in edges for f in edges)
        distinct_adj=sum(bool(set(e)&set(f)) for i,e in enumerate(edges) for j,f in enumerate(edges) if i!=j)
        check(adjacent_ordered==m+D2,(n,mask,'b1'))
        check(distinct_adj==D2,(n,mask,'b2'))

# Boundary graph identities for star and complete graphs at q=2/5.
for n in range(2,12):
    q=Fraction(2,5)
    star=[(0,j) for j in range(1,n)]
    clique=edges_of(n,(1<<comb(n,2))-1)
    Fstar=sum(q**s.bit_count()*(1-q)**(n-s.bit_count()) for s in range(1<<n) if independent(n,star,s))
    Fclique=sum(q**s.bit_count()*(1-q)**(n-s.bit_count()) for s in range(1<<n) if independent(n,clique,s))
    check(Fstar==(1-q)+q*(1-q)**(n-1),(n,'star'))
    check(Fclique==(1-q)**n+n*q*(1-q)**(n-1),(n,'complete'))
print('ALL EXACT CHECKS PASSED:',checks)
