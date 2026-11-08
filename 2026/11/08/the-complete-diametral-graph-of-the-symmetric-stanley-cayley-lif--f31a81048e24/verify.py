"""Finite exact-arithmetic replay for diametral geometry of symmetric Cayley lifts.
Theorem is proved in RESULT.md; this enumerator does not establish infinite quantifiers.
"""
from itertools import combinations, permutations
from math import factorial

def linear_extensions(elements, arcs):
    out=[]
    for p in permutations(sorted(elements)):
        pos={x:i for i,x in enumerate(p)}
        if all(pos[a]<pos[b] for a,b in arcs if a in elements and b in elements):
            out.append(p)
    return out

def upper_component_unions(d, arcs):
    unseen=set(range(d)); comps=[]
    adj=[set() for _ in range(d)]
    for a,b in arcs:
        adj[a].add(b);adj[b].add(a)
    while unseen:
        v=min(unseen);unseen.remove(v);stack=[v];comp={v}
        while stack:
            for w in adj[stack.pop()]:
                if w in unseen:
                    unseen.remove(w);comp.add(w);stack.append(w)
        comps.append(comp)
    return [frozenset(x for i,comp in enumerate(comps) if (mask>>i)&1 for x in comp)
            for mask in range(1<<len(comps))]

def sample_posets(d):
    pairs=list(combinations(range(d),2))
    for mask in range(1<<len(pairs)):
        arcs=[p for j,p in enumerate(pairs) if mask>>j&1]
        # Transitive naturally-labelled partial orders.
        if all((a,c) in arcs for a,b in arcs for x,c in arcs if b==x):
            yield arcs

def verify(d,arcs):
    universe=set(range(d)); ext=linear_extensions(universe,arcs);k=len(ext)
    lifted=[(frozenset(p[r:]),i) for i,p in enumerate(ext) for r in range(d+1)]
    assert len(set(lifted))==k*(d+1)
    actual=[];maxsq=-1
    for i in range(len(lifted)):
        for j in range(i+1,len(lifted)):
            (u,a),(v,b)=lifted[i],lifted[j]
            dist=len(u.symmetric_difference(v))+2*(a!=b)
            if dist>maxsq:
                maxsq=dist;actual=[(lifted[i],lifted[j])]
            elif dist==maxsq:
                actual.append((lifted[i],lifted[j]))
    unions=upper_component_unions(d,arcs)
    if k==1:
        assert maxsq==d and len(actual)==1
        return len(lifted)*(len(lifted)-1)//2
    assert maxsq==d+2
    a={I:len(linear_extensions(I,arcs))*len(linear_extensions(universe-set(I),arcs))
       for I in unions}
    count=k*(k-1)+sum(a[I]**2 for I in unions if I and len(I)<d)//2
    assert len(actual)==count,(d,arcs,len(actual),count)
    for (I,i),(J,j) in actual:
        assert I.isdisjoint(J) and len(I)+len(J)==d and i!=j
        assert I in a and J in a
    return len(lifted)*(len(lifted)-1)//2

assert sum(1 for _ in sample_posets(1))==1
assert sum(1 for _ in sample_posets(2))==2
assert sum(1 for _ in sample_posets(3))==7
assert sum(1 for _ in sample_posets(4))==40
assert sum(1 for _ in sample_posets(5))==357
N=0; checks=0
for d in range(1,6):
    for arcs in sample_posets(d):
        N+=1;checks+=verify(d,arcs)
for d in range(2,8):
    # Antichain test of the closed factorial formula.
    unions=upper_component_unions(d,[])
    e=factorial(d)
    ans=e*(e-1)+sum(factorial(len(I))**2*factorial(d-len(I))**2 for I in unions
                      if I and len(I)<d)//2
    assert ans==e*(e-1)+(e*e*sum(1/__import__('fractions').Fraction(factorial(d),factorial(j)*factorial(d-j))
                                          for j in range(1,d)))/2
print('SYMMETRIC_CAYLEY_DIAMETER_EXACT_OK',N,'posets',checks,'pairwise comparisons')
