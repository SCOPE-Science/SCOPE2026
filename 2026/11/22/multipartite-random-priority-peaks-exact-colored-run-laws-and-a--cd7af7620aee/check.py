"""Exact finite checks for random-priority peak counts on multipartite graphs.
This is standalone standard-library code, no downloaded data required.
"""
from itertools import product, permutations
from fractions import Fraction
from collections import Counter
from math import factorial

def survive(counts,ell):
    M=sum(counts)
    if ell<1 or ell>M: return Fraction(0)
    def fall(m,j):
        out=1
        for i in range(j): out*=m-i
        return out
    return Fraction(sum(fall(m,ell) for m in counts if m>=ell),fall(M,ell))

def color_law(counts):
    M=sum(counts)
    if not M: return {0:Fraction(1)}
    return {j:survive(counts,j)-survive(counts,j+1) for j in range(1,M+1)}

def convolution(a,b):
    out=Counter()
    for x,px in a.items():
        for y,py in b.items(): out[x+y]+=px*py
    return out

def predicted(parts, colors):
    k=max(colors)+1
    counts=[[0]*len(set(parts)) for _ in range(k)]
    for i,(p,c) in enumerate(zip(parts,colors)):
        counts[c][p]+=1
    ans={0:Fraction(1)}
    for cell in counts: ans=convolution(ans,color_law(cell))
    return ans

def observed(parts, colors):
    n=len(parts)
    ans=Counter()
    for order in permutations(range(n)):
        rank={v:j for j,v in enumerate(order)}
        S=sum(all(rank[u]<rank[v] for u in range(n) if parts[u]!=parts[v] and colors[u]==colors[v]) for v in range(n))
        ans[S]+=Fraction(1,factorial(n))
    return ans

checks=0
for parts in [(0,1), (0,0,1), (0,1,2), (0,0,1,1), (0,0,1,1,2), (0,0,0,1,1,2)]:
    for k in (1,2,3):
        for cs in product(range(k),repeat=len(parts)):
            assert predicted(parts,cs)==observed(parts,cs), (parts,cs)
            checks+=1
print('exact full-law cases:',checks)
for counts in [(2,3),(4,2,1),(3,1,2),(0,4,0),(2,0,0)]:
    M=sum(counts)
    if not M: continue
    mean=sum(j*p for j,p in color_law(counts).items())
    formula=sum((Fraction(a,M-a+1) for a in counts),Fraction(0))
    assert mean==formula
    checks+=1
for n,part_n,k in [(40,[20,20],2),(120,[40,40,40],3),(500,[200,300],5)]:
    expectation=sum(Fraction(m*k, n-m+1)*(1-Fraction(k-1,k)**(n-m+1)) for m in part_n)
    assert 0<expectation<n
    checks+=1
# Compare the finite exact expectation by averaging predicted laws over all colorings,
# not reusing the binomial-identity derivation.
for parts in [(0,1,2), (0,0,1,2), (0,0,1,1,2)]:
    n=len(parts)
    for k in (1,2,3):
        actual=Fraction(0)
        for colors in product(range(k),repeat=n):
            law=predicted(parts,colors)
            actual+=sum(Fraction(t)*p for t,p in law.items())/k**n
        count=[parts.count(i) for i in range(max(parts)+1)]
        formula=sum(Fraction(m*k,n-m+1)*(1-Fraction(k-1,k)**(n-m+1)) for m in count)
        assert actual==formula,(parts,k,actual,formula)
        checks+=1
print('total assertions/cases:',checks)
