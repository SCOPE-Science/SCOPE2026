"""Independent exhaustive verification of optimal packing-colouring recolouring for PG(2,2)."""
import itertools
from collections import Counter, deque

def plane(q):
    def norm(x):
        a=next(i for i,z in enumerate(x) if z)
        inv=pow(x[a],-1,q)
        return tuple(z*inv%q for z in x)
    vec=sorted({norm(x) for x in itertools.product(range(q),repeat=3) if any(x)})
    v=len(vec)
    adj=[0]*(2*v)
    for i,p in enumerate(vec):
        for j,l in enumerate(vec):
            if sum(a*b for a,b in zip(p,l))%q==0:
                adj[i] |= 1 << (v+j)
                adj[v+j] |= 1 << i
    return v,adj

v,adj=plane(2)
n=2*v
assert v==7
# Actual metric from all-source BFS, not projective-distance assumptions.
dist=[]
for s in range(n):
    d=[n+1]*n;d[s]=0;Q=deque([s]);
    while Q:
        a=Q.popleft()
        for b in range(n):
            if ((adj[a]>>b)&1) and d[b]>d[a]+1:
                d[b]=d[a]+1;Q.append(b)
    dist.append(d)
assert max(map(max,dist))==3
ind=[]
for mask in range(1<<n):
    if mask.bit_count() < v-1:continue
    if all(not ((mask>>i)&1 and (mask&adj[i])) for i in range(n)):
        ind.append(mask)
max_ind=max(x.bit_count() for x in ind)
assert max_ind==v
skeleton=set()
for mask in ind:
    if mask.bit_count() not in (v,v-1):continue
    rem=[i for i in range(n) if not ((mask>>i)&1)]
    for k in (1,2):
        if mask.bit_count()+k !=v+1:continue
        for subset in itertools.combinations(rem,k):
            if all(dist[a][b]>2 for a,b in itertools.combinations(subset,2)):
                skeleton.add((mask, sum(1<<b for b in subset)))
assert len(skeleton)==2*v*(1+2**2),len(skeleton)
# Assign distinct *named* colours 3..8 to all remaining vertices.
states=set()
for a,b in skeleton:
    rem=tuple(i for i in range(n) if not ((a|b)>>i)&1)
    assert len(rem)==v-1
    for order in itertools.permutations(range(3,v+2)):
        c=[0]*n
        for i in range(n):
            if (a>>i)&1:c[i]=1
            elif (b>>i)&1:c[i]=2
        for i,j in zip(rem,order):c[i]=j
        states.add(tuple(c))
assert len(states)==2*v*(1+4)*720,len(states)
print("Fano named states built:",len(states),flush=True)
# Exhaustively test EVERY possible one-vertex one-colour change (not a move template).
def valid(c):
    for a in range(n):
        for b in range(a+1,n):
            if c[a]==c[b] and dist[a][b]<=c[a]:return False
    return True
assert all(valid(c) for c in states)
print("all states validated",flush=True)
deg=Counter();vis=set(); comps=Counter(); edges=0
for c in states:
    cn=list(c);nb=set()
    for i in range(n):
        old=cn[i]
        for k in (1,2): # higher colours already all used; graph diameter 3 blocks duplicate names
            if k==old:continue
            cn[i]=k
            x=tuple(cn)
            if x in states:nb.add(x) # each member of states passed the exhaustive validation above
        cn[i]=old
    d=len(nb)
    deg[d]+=1;edges+=d
    # each state must move exactly within one fixed high-colour assignment
    if d==1:
        a=[x for x in nb][0]
        assert sum(i!=j for i,j in zip(a,c))==1
    elif d==4:
        assert all(sum(i!=j for i,j in zip(a,c))==1 for a in nb)
    else:raise AssertionError(d)
assert deg==Counter({1:40320,4:10080}),deg
assert edges//2==40320
# Degree one leaves guarantee no other connected components and the centers have disjoint stars.
print('PG(2,2): vertices=',n,'optimal classes=',len(skeleton),'named optima=',len(states),'degree histogram=',dict(deg),'edges=',edges//2,'components=',deg[4])
