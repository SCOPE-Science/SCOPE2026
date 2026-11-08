"""Finite exact certificate for the ordinary three-cut complex of the Frucht graph.

Run with Python 3 standard library: python3 verify_frucht_cut.py
The Alexander dual is collapsed by explicit, checked elementary simplicial pairs.
Mod-two boundary ranks of the original complex provide an independent check.
"""
from itertools import combinations
from collections import Counter

N=12
EDGES=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),
       (3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),
       (7,11),(8,9),(8,11),(10,11))
A=[0]*N
for i,j in EDGES:
    assert 0<=i<j<N
    A[i] |= 1<<j; A[j] |= 1<<i
assert all(x.bit_count()==3 for x in A) and len(EDGES)==18
FULL=(1<<N)-1

def connected3(bits):
    v=[i for i in range(N) if bits>>i & 1]
    assert len(v)==3
    e=sum(bool((A[x]>>y)&1) for x,y in combinations(v,2))
    return e>=2

def bit_subsets(s,k):
    v=[i for i in range(N) if s>>i&1]
    for comb in combinations(v,k):
        yield sum(1<<i for i in comb)

triples=[s for s in range(1<<N) if s.bit_count()==3]
conn={s for s in triples if connected3(s)}
disc=set(triples)-conn
triangles=[s for s in triples if all((A[x]>>y)&1 for x,y in combinations([i for i in range(N) if s>>i&1],2))]
assert len(triangles)==3
quad=[s for s in range(1<<N) if s.bit_count()==4 and all(t in conn for t in bit_subsets(s,3))]
assert quad==[sum(1<<i for i in (2,3,8,9))]
dual=set()
for s in range(1<<N):
    if all(t in conn for t in bit_subsets(s,3)):
        dual.add(s)
assert max(s.bit_count() for s in dual)==4
assert {k:sum(s.bit_count()==k for s in dual) for k in range(5)}=={0:1,1:12,2:66,3:30,4:1}
print('graph: 12 vertices; 18 edges; cubic; 3 triangles')
print('Alexander dual f-vector by simplex cardinality: (1,12,66,30,1)')
# A second face predicate for the original three-cut complex.
cut=set()
for s in range(1<<N):
    if any(t in disc for t in bit_subsets(FULL^s,3)):
        cut.add(s)
assert cut == {s for s in range(1<<N) if (FULL^s) not in dual}
assert max(s.bit_count() for s in cut)==9
assert all(s in cut for s in range(1<<N) if s.bit_count()<=7)
assert len([s for s in cut if s.bit_count()==9])==len(disc)
print('ordinary cut facets:',len(disc),'(all cardinality nine)')
print('ordinary cut f-vector by cardinality:',tuple(sum(s.bit_count()==k for s in cut) for k in range(10)))

# Perform and VERIFY each elementary collapse; no unstated solver dependency.
active=set(dual)
trace=[]
for high_size in [4,3]:
    while any(s.bit_count()==high_size for s in active):
        hi=sorted(s for s in active if s.bit_count()==high_size)
        parents=Counter(t for s in hi for t in bit_subsets(s,high_size-1))
        chosen=None
        for s in hi:
            for t in bit_subsets(s,high_size-1):
                if parents[t]==1 and t in active:
                    chosen=(t,s);break
            if chosen:break
        assert chosen is not None, ('not collapsible at dimension',high_size)
        lo,up=chosen
        assert lo in active and up in active and lo.bit_count()+1==up.bit_count()
        # Explicitly verify lo is contained in exactly one maximal remaining face.
        containers=[s for s in active if s!=lo and s&lo==lo]
        assert containers==[up],(lo,up,containers)
        active.remove(lo);active.remove(up)
        trace.append((lo,up))
assert len(trace)==30
assert {s.bit_count() for s in active}=={0,1,2}
assert sum(s.bit_count()==1 for s in active)==12
assert sum(s.bit_count()==2 for s in active)==37
# Connected residual graph, hence first Betti = edges - vertices + 1 = 25.
rem=[s for s in active if s.bit_count()==1]
seen={rem[0]};changed=True
while changed:
    changed=False
    for e in [s for s in active if s.bit_count()==2]:
        if any(e&v for v in seen):
            for v in rem:
                if e&v and v not in seen:seen.add(v);changed=True
assert len(seen)==N
beta=len([s for s in active if s.bit_count()==2])-N+1
print('checked free-face collapse pairs:',len(trace))
print('collapse sequence (lower_face, upper_face), vertex indices:')
for lo,up in trace:
    lower=tuple(i for i in range(N) if lo>>i&1)
    upper=tuple(i for i in range(N) if up>>i&1)
    print(lower,upper)
print('remaining connected graph: 12 vertices, 37 edges; first Betti:',beta)
assert beta==26

# Independently compute reduced homology over F2 for the original complex.
f={k:sorted(s for s in cut if s.bit_count()==k) for k in range(10)}
def rank(cols,rows):
    d={b:i for i,b in enumerate(rows)};piv={}
    for s in cols:
        v=0
        for b in bit_subsets(s,s.bit_count()-1):v^=1<<d[b]
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)
r={k:rank(f[k],f[k-1]) for k in range(1,10)}
betti={k-1:len(f[k])-r.get(k,0)-r.get(k+1,0) for k in range(1,10)}
assert betti=={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:26}
assert beta==betti[8]
print('cut mod-two reduced Betti by degree:',betti)
print('cut mod-two boundary ranks by input cardinality:',r)
print('PASS: full free-face certificate and independent mod-two chain computation')
