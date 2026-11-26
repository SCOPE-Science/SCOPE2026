"""Exact six-symbol Ulam four-code census by directed-triple packing.
Run: python3 enumerate_triples.py
"""
from itertools import permutations, combinations
from collections import Counter, defaultdict

P=list(permutations(range(6)))
index={p:i for i,p in enumerate(P)}
assert len(P)==720
triples=list(permutations(range(6),3))
tridx={t:i for i,t in enumerate(triples)}
mask=[]
for p in P:
    bits=sum(1<<tridx[t] for t in combinations(p,3))
    assert bits.bit_count()==20
    mask.append(bits)
# Distinct permutations can coexist exactly when their directed three-subsequence sets are disjoint.
N=[i for i in range(1,720) if not(mask[i]&mask[0])]
adj={i:{j for j in N if i<j and not(mask[i]&mask[j])} for i in N}
normalized=[]
for i in N:
    for j in adj[i]:
        for k in adj[j]:
            if k in adj[i]:
                normalized.append((0,i,j,k))
assert len(normalized)==298, len(N)
assert all(not any(t not in cd and all((mask[t]&mask[i])==0 for i in cd) for t in N) for cd in normalized)
# Erdős–Szekeres implies pairwise exact Ulam distance four for these size-four codes.
assert all(any(tuple(P[i][a] for a in ix) == tuple(P[j][a] for a in iy) for ix in combinations(range(6),2) for iy in combinations(range(6),2)) for cd in normalized for i,j in combinations(cd,2))

def normalize(code,reversed_order=False):
    words=[tuple(reversed(P[i])) if reversed_order else P[i] for i in code]
    keys=[]
    for base in words:
        relabel={value:pos for pos,value in enumerate(base)}
        converted=sorted(''.join(str(relabel[a]) for a in p) for p in words)
        keys.append('|'.join(converted))
    return min(keys)

class_counts=Counter()
representatives={}
for code in normalized:
    key=min(normalize(code,False),normalize(code,True))
    class_counts[key]+=1
    representatives[key]=min(representatives.get(key,code),code)
hist=Counter(class_counts.values())
assert len(class_counts)==57 and hist==Counter({2:7,4:29,8:21}),hist
assert sum(180*m*n for m,n in hist.items()) == 53640
assert len(set(normalized))==298
print('INDEPENDENT_VERIFY_OK permutations=720 ordered_triples=120 admissible_neighbors=132 normalized=298 labeled=53640 classes=57')
print('orbits 360:7 720:29 1440:21')
for key in sorted(class_counts):print(class_counts[key],key)
