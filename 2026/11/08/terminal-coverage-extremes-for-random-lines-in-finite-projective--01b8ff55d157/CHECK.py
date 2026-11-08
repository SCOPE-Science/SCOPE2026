from itertools import combinations,product
from fractions import Fraction
from math import comb

def projective(q):
    def norm(v):
        k=next(i for i,x in enumerate(v) if x%q)
        inv=pow(v[k],-1,q)
        return tuple((x*inv)%q for x in v)
    pts=sorted({norm(v) for v in product(range(q),repeat=3) if any(v)})
    lines=sorted({norm(v) for v in product(range(q),repeat=3) if any(v)})
    incid=[{i for i,p in enumerate(pts) if sum(a*b for a,b in zip(d,p))%q==0} for d in lines]
    return pts,incid

checks=0
for q in (2,3,5):
    points,lines=projective(q); n=q*q+q+1; k=q+1
    assert len(points)==len(lines)==n
    for line in lines: assert len(line)==k; checks+=1
    for i in range(n):
        assert sum(i in L for L in lines)==k; checks+=1
    for i,j in combinations(range(n),2):
        assert sum(i in L and j in L for L in lines)==1
        checks+=1
        p=Fraction(n-k,n)
        both=Fraction(n-2*k+1,n)
        assert both<p*p;checks+=1
    for r in range(1,min(n,4)+1):
        for subset in combinations(range(n),r):
            count=sum(any(i in L for i in subset) for L in lines)
            assert r*k-comb(r,2) <= count <=r*k
            # independent check: pair union exactly 2k-1
            if r==2: assert count==2*k-1
            checks+=1
    print('q',q,'n',n,'checks',checks)
print('passed',checks)
# Verify exact multi-time joint survival by independent direct path enumeration.
for q in (2,3):
    pts,blocks=projective(q); v=len(pts)
    labels=(0,1,2)
    limits=(1,2,3)
    count=0
    from itertools import product as _product
    for draw_indices in _product(range(v),repeat=3):
        if all(all(i not in blocks[draw_indices[t]] for t in range(limits[a])) for a,i in enumerate(labels)):
            count+=1
    prob=Fraction(count,v**3)
    prod=Fraction(1)
    for t in range(3):
        active={labels[a] for a in range(3) if limits[a]>t}
        hits=sum(bool(active.intersection(L)) for L in blocks)
        prod*=Fraction(v-hits,v)
    assert prob==prod
    checks+=1
# Exact q=2 expected cover time by inclusion-exclusion, independently computed.
q=2
points,blocks=projective(q)
v=len(points)
E=Fraction(0)
for mask in range(1,1<<v):
    subset={i for i in range(v) if mask>>i&1}
    hits=sum(bool(subset.intersection(L)) for L in blocks)
    E+=Fraction((-1)**(len(subset)+1)*v,hits)
assert E==Fraction(163,30),E
checks+=1
print('all checks passed:',checks,'q2 exact expected cover time:',E)
