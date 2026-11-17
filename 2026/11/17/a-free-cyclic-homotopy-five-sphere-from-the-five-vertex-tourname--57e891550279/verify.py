"""Exact collapse and algebraic topology checks for the cyclic five-tournament NSC complex."""
from collections import Counter,deque
n=5
arcs=tuple((i,(i+d)%5) for i in range(n) for d in (1,2))
faces=set()
for bits in range(1<<len(arcs)):
    out=[set() for _ in range(n)]
    for j,(a,b) in enumerate(arcs):
        if bits>>j&1:out[a].add(b)
    ok=False
    for root in range(n):
        reached={root};queue=[root]
        while queue:
            for v in out[queue.pop()]-reached:
                reached.add(v);queue.append(v)
        if len(reached)<n:ok=True;break
    if ok:faces.add(bits)
assert 0 in faces and len(faces)==901
order=[8,2,5,9,7,1,6,0,4,3]
remaining=set(faces);match={}
for i in order:
    for f in sorted(list(remaining)):
        h=f|(1<<i)
        if f&(1<<i)==0 and f in remaining and h in remaining:
            remaining.remove(f);remaining.remove(h);match[f]=h
assert remaining=={189},remaining
assert 0 in match and match[0]==(1<<8)
# Change the reduced matching into an ordinary matching by leaving its (-1,0) pair unmatched.
match.pop(0)
vertices=sorted(faces-{0})
indegree={v:0 for v in vertices};adj={v:[] for v in vertices}
for h in vertices:
    for i in range(10):
        if h>>i&1:
            f=h^(1<<i)
            if not f:continue
            if match.get(f)==h:a,b=f,h
            else:a,b=h,f
            adj[a].append(b);indegree[b]+=1
q=deque(v for v,d in indegree.items() if d==0)
count=0
while q:
    v=q.popleft();count+=1
    for w in adj[v]:
        indegree[w]-=1
        if indegree[w]==0:q.append(w)
assert count==len(vertices),('gradient cycle',len(vertices)-count)
critical=set(vertices)-set(match)-set(match.values())
assert critical=={1<<8,189},critical
assert (189).bit_count()==6
# Check mod-two reduced chain ranks independently.
from itertools import combinations
simplices={j:[] for j in range(9)}
for f in vertices:simplices[f.bit_count()-1].append(f)
def grank(values):
    basis={}
    for v in values:
        while v:
            p=v.bit_length()-1
            if p not in basis:basis[p]=v;break
            v^=basis[p]
    return len(basis)
ranks={0:0}
for d in range(1,9):
    rowindex={f:i for i,f in enumerate(simplices[d-1])};cols=[]
    for f in simplices[d]:
        b=0
        for i in range(10):
            if f>>i&1:b^=1<<rowindex[f^(1<<i)]
        cols.append(b)
    ranks[d]=grank(cols)
betti={d:len(simplices[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(9)}
assert betti=={0:0,1:0,2:0,3:0,4:0,5:1,6:0,7:0,8:0},betti
# Lefschetz: any invariant arc subset for nontrivial rotation is union of two five-edge directed cycles,
# both strongly connected, so no nonempty invariant simplex. Thus top homology trace = +1.
for k in range(1,5):
    orbits=[];remaining_arcs=set(arcs)
    while remaining_arcs:
        a,b=next(iter(remaining_arcs));O={((a+j*k)%5,(b+j*k)%5) for j in range(5)}
        remaining_arcs-=O;orbits.append(O)
    assert len(orbits)==2 and all(len(o)==5 for o in orbits)
    assert all(not any(set(arcs[i] for i in range(10) if f>>i&1)==o for f in faces) for o in orbits)
print('TOURNAMENT5_NSC_DISCRETE_MORSE_PASS faces=901 reduced_pairs=450 critical_ordinary=(vertex8,face189_dim5) acyclic_hasse='+str(count)+' betti5=1 rotations=4')
