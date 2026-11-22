"""Independent combinatorial incidence and pair-event consistency checks."""
from collections import Counter
from itertools import combinations
from math import comb

# Derive Clebsch graph directly from even five-bit words, independent of first script.
E=[x for x in range(32) if x.bit_count()%2==0]
N={v:{w for w in E if (v^w).bit_count()==4} for v in E}
assert all(len(N[v])==5 for v in E)
assert all(len(N[u]&N[v])==(0 if v in N[u] else 2)
           for u in E for v in E if u!=v)
faces={k:set() for k in range(6)}
for nhood in N.values():
    for k in range(6):faces[k].update(combinations(sorted(nhood),k))
f=[len(faces[k]) for k in range(6)]
assert f==[1,16,80,160,80,16],f
print('Clebsch neighborhood face counts (including empty):',f)
assert 2*sum(f)==706

# General geometry: closed distance-two balls in Q_d and antipodal contradictions.
for d in range(5,11):
    v=1<<d; allbits=(1<<d)-1; m=comb(d,2)
    B=[{x} | {x^(1<<i)^(1<<j) for i,j in combinations(range(d),2)}
       for x in range(v)]
    overlap=Counter()
    for u in range(v):
        for w in range(u+1,v):
            r=(u^w).bit_count()
            a=len(B[u]&B[w]); overlap[(r,a)]+=1
            assert a==((2*d-2) if r==2 else (6 if r==4 else 0)), (d,r,a)
    if d>=7:
        for u in range(v):
            for w in range(u+1,v):
                if (u^w).bit_count()==2:
                    union=B[u]|B[w]
                    assert all((x^allbits) not in union for x in union)
    print(f'd={d}: size={m+1}; all two-center ball intersections verified')

# d=6: each parity's closed distance-two balls are exactly antipodal transversals.
d=6; full=63
E=[x for x in range(64) if x.bit_count()%2==0]
B=[{v}|{v^(1<<i)^(1<<j) for i,j in combinations(range(d),2)} for v in E]
assert all(len(t)==16 and all((x^full) not in t for x in t) for t in B)
assert len({frozenset(t) for t in B})==32
print('d=6: exactly 32 distinct obstructing antipodal transversals per parity')
