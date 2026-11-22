"""Independent binary-rank checker for all omitted-gate subsets and all single gates.
Run: python3 VERIFY_BINARY.py (standard library only).
"""
from itertools import combinations
D=list(combinations(range(6),2))
# Independent line-generation via all perfect-matching masks, sorted lexically.
ALL=[]
for ab in D:
    free=set(range(6))-set(ab)
    for cd in combinations(sorted(free),2):
        ef=tuple(sorted(free-set(cd)))
        part=tuple(sorted((ab,cd,ef)))
        if part not in ALL:ALL.append(part)
ALL=sorted(ALL)
assert len(ALL)==15
W=[sum(1<<j for j,p in enumerate(ALL) if e in p) for e in D]

def gf2rank(bits):
    piv={}
    for initial in bits:
        v=initial
        while v:
            k=v.bit_length()-1
            if k not in piv:
                piv[k]=v
                break
            v^=piv[k]
    return len(piv)

assert gf2rank(W)==10
F=[(D.index((2,3)),ALL.index(((0,1),(2,3),(4,5)))),
   (D.index((0,1)),ALL.index(((0,1),(2,5),(3,4)))),
   (D.index((1,2)),ALL.index(((0,3),(1,2),(4,5)))),
   (D.index((1,5)),ALL.index(((0,2),(1,5),(3,4)))),
   (D.index((1,3)),ALL.index(((0,4),(1,3),(2,5))))]
assert len({i for i,j in F})==len({j for i,j in F})==5
for mask in range(32):
    rows=W[:]
    for k,(i,j) in enumerate(F):
        if mask>>k&1:
            assert rows[i]>>j&1
            rows[i]^=1<<j
    assert gf2rank(rows)==10+mask.bit_count(),mask
single_edges=0
for i in range(15):
    for j in range(15):
        if W[i]>>j&1:
            rows=W[:]
            rows[i]^=1<<j
            assert gf2rank(rows)==11,(i,j)
            single_edges+=1
assert single_edges==45
print('PASS: independent representation; baseline rank 10; all 32 subsets; all 45 single-edge fault ranks are 11.')
