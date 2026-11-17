"""Independent, factorized exact majority census on the truncated octahedral graph.
Run with Python 3; uses only the standard library.
"""
from itertools import permutations, product
from collections import Counter, deque
import json

# Cartesian realization: all permutations of (0,+/-1,+/-2), with edges at squared distance two.
V=sorted({tuple(z) for a,b in product((-1,1),repeat=2) for z in permutations((0,a,2*b))})
assert len(V)==24
adj=[[j for j,w in enumerate(V) if sum((v[k]-w[k])**2 for k in range(3))==2] for v in V]
assert all(len(row)==3 for row in adj)
assert sum(map(len,adj))==72
# A 24-vertex isomorphism certificate to the adjacent-position-swap Cayley graph.
perms=list(permutations(range(4)))
pid={p:i for i,p in enumerate(perms)}
coord_to_perm=[0,1,6,7,2,4,8,10,3,12,5,14,18,9,20,11,13,19,15,21,16,22,17,23]
assert sorted(coord_to_perm)==list(range(24))
for i in range(24):
    t=perms[coord_to_perm[i]]
    expected=set()
    for j in range(3):
        w=list(t);w[j],w[j+1]=w[j+1],w[j]
        expected.add(pid[tuple(w)])
    assert {coord_to_perm[v] for v in adj[i]}==expected
color=[-1]*24
for i in range(24):
    if color[i]!=-1:continue
    color[i]=0;dq=deque([i])
    while dq:
        u=dq.popleft()
        for v in adj[u]:
            if color[v]==-1:color[v]=1-color[u];dq.append(v)
            else:assert color[u]!=color[v]
L=[i for i in range(24) if color[i]==0];R=[i for i in range(24) if color[i]==1]
assert len(L)==len(R)==12

def side_map(source, target):
    src={v:i for i,v in enumerate(source)}
    in_masks=[sum(1<<src[j] for j in adj[v]) for v in target]
    return [sum((1<<i) for i,m in enumerate(in_masks) if (x&m).bit_count()>=2) for x in range(4096)]

# F(L,R)=(f(R),g(L)); F^2(L,R)=(f*g(L),g*f(R)).
f=side_map(R,L);g=side_map(L,R)
P=[f[g[a]] for a in range(4096)];Q=[g[f[b]] for b in range(4096)]

def orbit_data(H, cross):
    tau=[];iota=[];dest=[]
    for x in range(4096):
        path=[x];seen={x}
        while H[path[-1]]!=path[-1]:
            y=H[path[-1]]
            assert y not in seen, 'two-step dynamics must stabilize'
            path.append(y);seen.add(y)
        target=path[-1]; t=len(path)-1
        # After an odd step, the opposite side applies cross to the successive H-states.
        j=next(k for k in range(t+1) if k==t or cross[path[k]]==cross[path[k+1]])
        # Equality must persist once it occurs.
        assert all(cross[path[k]]==cross[path[k+1]] for k in range(j,t))
        tau.append(t);iota.append(j);dest.append(target)
    return tau,iota,dest

# In odd-step states left is f(Q^k(b)), right is g(P^k(a)).
tL,iL,eL=orbit_data(P,g)
tR,iR,eR=orbit_data(Q,f)
fixed_by_depth=Counter();period2_by_depth=Counter()
for a in range(4096):
    u=eL[a]
    for b in range(4096):
        v=eR[b]
        d=min(2*max(tL[a],tR[b]),2*max(iL[a],iR[b])+1)
        fixed=(f[v]==u and g[u]==v)
        (fixed_by_depth if fixed else period2_by_depth)[d]+=1
res={
 "vertices":24,"states":4096**2,
 "fixed":fixed_by_depth[0],"period2_states":period2_by_depth[0],
 "max_transient":max(fixed_by_depth.keys()|period2_by_depth.keys()),
 "fixed_entry":[fixed_by_depth[d] for d in range(6)],
 "period2_entry":[period2_by_depth[d] for d in range(6)],
 "two_step_side_depths":{"left":dict(sorted(Counter(tL).items())),"right":dict(sorted(Counter(tR).items()))},
 "odd_side_depths":{"left":dict(sorted(Counter(iL).items())),"right":dict(sorted(Counter(iR).items()))}}
assert sum(fixed_by_depth.values())+sum(period2_by_depth.values())==2**24
print(json.dumps(res,sort_keys=True))
