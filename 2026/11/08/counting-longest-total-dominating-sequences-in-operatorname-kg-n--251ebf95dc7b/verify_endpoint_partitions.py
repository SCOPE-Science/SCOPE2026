"""Different certificate: restricted-growth partitions of 12 oriented endpoints.
Every unordered six-edge sequence is represented by precisely 2**6
oriented endpoint lists; no pair-birth bookkeeping is required.
"""
from collections import Counter
from math import factorial

COEFF={4:720,5:33120,6:257040,7:655200,8:624960,9:181440}
HIST={4:1920,5:17664,6:22848,7:8320,8:992,9:32}
counts=Counter()
visits=Counter()

def legal(ordered_edges, e):
    if not ordered_edges:return True
    involved={x for a,b in ordered_edges for x in (a,b)}
    possible=[{x} for x in involved if x not in e]
    possible += [{x,y} for x in involved for y in involved if x<y and x not in e and y not in e]
    return any(all(a in S or b in S for a,b in ordered_edges) for S in possible)

def has_two_cover(edges):
    involved=sorted({x for e in edges for x in e})
    for a in involved:
        if all(a in e for e in edges): return True
        for b in involved:
            if a<b and all(a in e or b in e for e in edges): return True
    return False

def walk(partial,t):
    k=len(partial)
    visits[k]+=1
    if k==6:
        assert not has_two_cover(partial)
        counts[t]+=1
        return
    # Independently enumerate the 12-position restricted-growth strings.
    for a in range(t+1):
        for b in range(max(t,a+1)+1):
            if b==a:continue
            # Ensure each new symbol has the next available number.
            if b>t+(a==t):continue
            e=tuple(sorted((a,b)))
            if e in partial:continue
            if legal(partial,e):walk(partial+(e,),max(t,a+1,b+1))
walk((),0)
assert dict(counts)==HIST, (dict(counts),HIST)
assert sum(counts.values())==51776
for t,n in HIST.items():
    assert n * factorial(t)//64 == COEFF[t]
print('PASS oriented-endpoint restricted-growth enumeration')
print('level counts:', sorted(visits.items()))
print('oriented pattern histogram:',sorted(counts.items()))
print('binomial coefficients:', sorted(COEFF.items()))
