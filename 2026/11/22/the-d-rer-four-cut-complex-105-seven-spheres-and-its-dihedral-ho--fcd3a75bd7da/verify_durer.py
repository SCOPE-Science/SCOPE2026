"""Exact, dependency-free verification for a four-cut-complex calculation.
Run: python3 verify_durer.py  (next to collapse_pairs.json).
All simplices and faces are indexed by vertices 0,...,11.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

N=12
V=tuple(range(N))
EDGES=set()
for i in range(6):
    EDGES.add(frozenset((i,(i+1)%6)))
    EDGES.add(frozenset((i,6+i)))
    EDGES.add(frozenset((6+i,6+(i+2)%6)))
assert len(EDGES)==18

def connected(s):
    s=frozenset(s)
    found={min(s)}
    while True:
        newer=found|{w for e in EDGES for v in e & found for w in e if w in s}
        if newer==found:break
        found=newer
    return found==s

disconnected4={t for t in itertools.combinations(V,4) if not connected(t)}
assert len(disconnected4)==429

def permitted(t):
    return all(sub not in disconnected4 for sub in itertools.combinations(t,4))

initial={tuple(t) for size in range(1,13) for t in itertools.combinations(V,size) if permitted(t)}
counts=Counter(map(len,initial))
assert [counts[k] for k in range(1,13)]==[12,66,220,66,6,0,0,0,0,0,0,0]
expected_five={tuple(sorted(((0+k)%6,(1+k)%6,(2+k)%6,6+k,6+(k+2)%6))) for k in range(6)}
assert {t for t in initial if len(t)==5}==expected_five
assert all(tuple(sorted(set(t)-{v})) in initial for t in initial for v in t if len(t)>1)

certificate_path=Path(__file__).with_name('collapse_pairs.json')
certificate=json.loads(certificate_path.read_text(encoding='utf-8'))
assert len(certificate)==66
live=set(initial)
for j,(a,b) in enumerate(certificate):
    a,b=tuple(a),tuple(b)
    assert tuple(sorted(a))==a and tuple(sorted(b))==b
    assert a in live and b in live and len(b)==len(a)+1
    assert set(a)<set(b) and len(b)>=4
    cofaces=[s for s in live if set(a)<set(s)]
    assert cofaces==[b], (j,a,b,cofaces)
    live.remove(a)
    live.remove(b)
assert len(live)==238
assert [sum(len(s)==k for s in live) for k in range(1,6)]==[12,66,160,0,0]
assert not any(len(t)>=4 for t in live)
# A full 2-skeleton is simply connected. Each checked pair is a simplicial
# elementary collapse. Consequently, the 2-dimensional residual complex
# has the homotopy type of 105 two-spheres, by Euler characteristic.
assert -1+12-66+160==105

# The 12 permutations below preserve edges. The only triangles of the graph
# are the two inner triangles. An automorphism therefore preserves the inner
# six vertices; its outer-vertex restriction is an automorphism of C6 and its
# spokes fix the inner permutation. Hence these 12 form the entire group.
def maps(k,reflection):
    return {i:(((-i if reflection else i)+k)%6) for i in range(6)} | {
        i+6:6+(((-i if reflection else i)+k)%6) for i in range(6)}

def perm_sign(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))

def trace_dual(g):
    ans=-1  # augmented 0-chain correction
    for s in initial:
        t=tuple(g[i] for i in s)
        if set(t)==set(s):ans+=(-1)**(len(s)-1)*perm_sign(t)
    return ans

traces=[]
for reflection in (False,True):
    line=[]
    for k in range(6):
        g=maps(k,reflection)
        assert len(set(g.values()))==12
        assert {frozenset(g[x] for x in e) for e in EDGES}==EDGES
        assert perm_sign(tuple(g[i] for i in V))==1
        line.append(trace_dual(g))
    traces.append(line)
assert traces==[[105,-1,3,5,3,-1],[-7,1,-7,1,-7,1]]
assert sum(sum(line) for line in traces)==96
assert sum(sum(line) for line in traces)//12==8

# The original complex contains the full 5-skeleton because the dual has
# no faces with six vertices (Alexander duality definition).
assert all(not permitted(t) for t in itertools.combinations(V,6))

print('graph: 12 vertices, 18 edges, exactly two inner triangles')
print('disconnected induced 4-sets:',len(disconnected4))
print('dual f-vector:',[counts[k] for k in range(1,6)])
print('elementary collapses:',len(certificate),'(6 four-to-three; 60 three-to-two)')
print('residual f-vector:',[sum(len(s)==k for s in live) for k in range(1,4)])
print('dual reduced Euler characteristic: 105')
print('r^k traces:',traces[0])
print('s r^k traces:',traces[1])
print('dimension of invariant rational homology:',8)
print('all exact checks passed')
