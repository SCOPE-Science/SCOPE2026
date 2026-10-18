from collections import deque, defaultdict
from itertools import combinations

D=4
N=D*(1<<(D-1))
ORDER=[21,26,9,5,12,1,15,23,28,0,22,2,6,8,19,10,14,16,20,24,17,27,11,30,25,3,13,29,18,7,31,4]

def edge_from_id(eid):
    i=eid//(1<<(D-1)); code=eid%(1<<(D-1))
    base=0; k=0
    for j in range(D):
        if j==i: continue
        if (code>>k)&1: base |= 1<<j
        k+=1
    return i,base,base|(1<<i)
EDGES=[edge_from_id(i) for i in range(N)]
assert len({tuple(sorted((a,b))) for _,a,b in EDGES})==N
# line graph adjacency
Ladj=[set() for _ in range(N)]
for a in range(N):
    ea=set(EDGES[a][1:])
    for b in range(a+1,N):
        if ea.intersection(EDGES[b][1:]):
            Ladj[a].add(b); Ladj[b].add(a)
assert all(len(x)==6 for x in Ladj), [len(x) for x in Ladj]
# all-pairs line distances
DIST=[]
for s in range(N):
    d=[-1]*N;d[s]=0;q=deque([s])
    while q:
        u=q.popleft()
        for v in Ladj[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    DIST.append(d)
assert max(map(max,DIST))==4
# scale2 proximity graph
Adj=[set() for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if DIST[i][j]<=2:
            Adj[i].add(j);Adj[j].add(i)
assert sum(map(len,Adj))//2==336
# enumerate every nonempty clique via increasing recursion
F=[]
def rec(prefix,cands):
    for idx,v in enumerate(cands):
        m=prefix | (1<<v); F.append(m)
        new=[w for w in cands[idx+1:] if w in Adj[v]]
        rec(m,new)
rec(0,list(range(N)))
assert len(F)==len(set(F))
Fset=set(F)
fv=defaultdict(int)
for m in F:fv[m.bit_count()-1]+=1
print('FACE_VECTOR', [fv[i] for i in range(max(fv)+1)])
assert [fv[i] for i in range(8)]==[32,336,1568,3672,4512,2848,832,96]
# repeated vertex matching
active=set(Fset); pairs=[]; pairmap={}
for v in ORDER:
    bit=1<<v
    lows=[m for m in active if not (m&bit) and (m|bit) in active]
    for lo in lows:
        hi=lo|bit
        assert lo in active and hi in active
        active.remove(lo);active.remove(hi)
        pairs.append((lo,hi));pairmap[lo]=hi;pairmap[hi]=lo
crit=defaultdict(int)
for m in active:crit[m.bit_count()-1]+=1
print('MATCHED_PAIRS',len(pairs),'CRITICAL',dict(sorted(crit.items())))
assert len(pairs)==6943
assert dict(crit)=={0:1,3:1,5:8}
# Hasse covers and acyclicity. For every high face, remove one vertex.
indeg={m:0 for m in Fset}; out=defaultdict(list); covers=0
for hi in F:
    if hi.bit_count()==1: continue
    bits=[i for i in range(N) if (hi>>i)&1]
    for v in bits:
        lo=hi^(1<<v)
        assert lo in Fset
        covers+=1
        if pairmap.get(lo)==hi:
            u,w=lo,hi
        else:
            u,w=hi,lo
        out[u].append(w);indeg[w]+=1
print('HASSE_COVERS',covers)
# topo sort
q=deque([m for m,d in indeg.items() if d==0]);seen=0
while q:
    u=q.popleft();seen+=1
    for w in out[u]:
        indeg[w]-=1
        if indeg[w]==0:q.append(w)
print('DAG_VERTICES',seen)
assert seen==len(Fset)
# independent mod2 chain ranks by sparse bitset elimination
faces_by_dim={k:[] for k in range(8)}
for m in F:faces_by_dim[m.bit_count()-1].append(m)
for k in faces_by_dim:faces_by_dim[k].sort()
def gf2_rank(cols):
    piv={};r=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;r+=1;break
    return r
ranks={}
for k in range(1,8):
    idx={m:i for i,m in enumerate(faces_by_dim[k-1])}
    cols=[]
    for hi in faces_by_dim[k]:
        x=0
        b=hi
        while b:
            lsb=b & -b; lo=hi^lsb; x ^= 1<<idx[lo]; b-=lsb
        cols.append(x)
    ranks[k]=gf2_rank(cols)
print('F2_BOUNDARY_RANKS',[ranks[k] for k in range(1,8)])
betti=[]
for k in range(8):
    val=len(faces_by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0)
    if k==0: val-=1
    betti.append(val)
print('REDUCED_F2_BETTI',betti)
assert betti==[0,0,0,1,0,8,0,0]
# structural checks at scale1 and penultimate scale3 for context
# scale3 missing pairs are distance4; verify a perfect matching of 16 antipodal parallel edges.
far=[]
for i in range(N):
    for j in range(i+1,N):
        if DIST[i][j]==4:far.append((i,j))
assert len(far)==16
used=[x for p in far for x in p]
assert len(set(used))==N
print('DISTANCE4_PAIRS',len(far))
print('VERIFY_OK')
