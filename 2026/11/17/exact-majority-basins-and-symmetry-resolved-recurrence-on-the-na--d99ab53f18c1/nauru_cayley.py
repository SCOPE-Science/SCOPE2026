"""Exact shore-factor computation and symmetry census for majority on the 4-star graph.
Pure Python 3, standard library only. Vertices are injective triples over {0,1,2,3}.
"""
from itertools import permutations, product
from collections import Counter, deque
import json

V = tuple(permutations(range(4), 3)); index = {v:i for i,v in enumerate(V)}
adj = tuple(tuple(j for j,w in enumerate(V) if sum(a!=b for a,b in zip(v,w)) == 1)
            for v in V)
assert len(V)==24 and all(len(a)==3 for a in adj)
part=[-1]*24;part[0]=0;q=deque([0])
while q:
    v=q.popleft()
    for w in adj[v]:
        if part[w] == -1:part[w]=1-part[v];q.append(w)
        else:assert part[w]!=part[v]
assert part.count(0)==part.count(1)==12
shore=[[i for i in range(24) if part[i]==k] for k in (0,1)]
pos=[{v:i for i,v in enumerate(s)} for s in shore]
H=[]
for k in (0,1):
    indices=[[pos[1-k][w] for w in adj[v]] for v in shore[k]]
    H.append([sum((int(sum((z>>j)&1 for j in nn)>=2)<<i) for i,nn in enumerate(indices))
              for z in range(4096)])
h0,h1=H
g0=tuple(h0[h1[x]] for x in range(4096))
g1=tuple(h1[h0[x]] for x in range(4096))

def shore_data(g):
    fixed=[i for i in range(4096) if g[i]==i]
    root={i:i for i in fixed}; depth={i:0 for i in fixed}
    def resolve(x):
        if x not in root:
            y=g[x];resolve(y)
            root[x]=root[y];depth[x]=depth[y]+1
        return root[x]
    for i in range(4096):resolve(i)
    return fixed,root,depth,Counter(root.values())
fix0,r0,d0,b0=shore_data(g0); fix1,r1,d1,b1=shore_data(g1)
assert len(fix0)==len(fix1)==494
assert max(d0.values())==max(d1.values())==3

# F^(2t)=(g0^t(a),g1^t(b)); F^(2t+1)=(h0 g1^t(b), h1 g0^t(a)).
def cumulative(k):
    t=k//2
    cur0=list(range(4096));cur1=list(range(4096))
    for _ in range(t):
        cur0=[g0[x] for x in cur0]
        cur1=[g1[x] for x in cur1]
    if k%2==0:
        return sum(g0[x]==x for x in cur0)*sum(g1[x]==x for x in cur1)
    return sum(h1[g0[x]]==h1[x] for x in cur0)*sum(h0[g1[x]]==h0[x] for x in cur1)
C=[cumulative(k) for k in range(6)];assert C[-1]==1<<24
P=[C[0]]+[C[i]-C[i-1] for i in range(1,6)]

# Attraction basins, pairing F phases into primitive temporal orbits.
seen=set();fixed_basins=Counter();two_basins=Counter()
for a in fix0:
    for b in fix1:
        if (a,b) in seen:continue
        nxt=(h0[b],h1[a]);assert nxt[0] in fix0 and nxt[1] in fix1
        period=1 if nxt==(a,b) else 2
        size=b0[a]*b1[b]
        seen.add((a,b));seen.add(nxt)
        if period==1:fixed_basins[size]+=1
        else:
            size+=b0[nxt[0]]*b1[nxt[1]]
            two_basins[size]+=1
assert sum(i*c for i,c in fixed_basins.items())==979268
assert sum(i*c for i,c in two_basins.items())==15797948

# Group S_4 on symbols, S_3 on coordinates, with five transposition generators.
def swap_tuple(t,i,j):
    t=list(t);t[i],t[j]=t[j],t[i];return tuple(t)
perms=[]
for i,j in [(0,1),(1,2),(2,3)]:
    perm=tuple(index[tuple((j if z==i else i if z==j else z) for z in v)] for v in V)
    perms.append(perm)
for i,j in [(0,1),(1,2)]:
    perm=tuple(index[swap_tuple(v,i,j)] for v in V)
    perms.append(perm)
for p in perms:
    assert sorted(p)==list(range(24))
    assert all({p[w] for w in adj[v]}==set(adj[p[v]]) for v in range(24))
def comp(p,q):return tuple(p[q[k]] for k in range(24))
group={tuple(range(24))};q=deque(group)
while q:
    x=q.popleft()
    for p in perms:
        z=comp(p,x)
        if z not in group:group.add(z);q.append(z)
assert len(group)==144

def encode(a,b):
    z=0
    for i,v in enumerate(shore[0]):z|=((a>>i)&1)<<v
    for i,v in enumerate(shore[1]):z|=((b>>i)&1)<<v
    return z

def transform(x,p):
    y=0
    while x:
        bit=x&-x;i=bit.bit_length()-1
        y|=1<<p[i];x^=bit
    return y

def update(x):
    a=sum(((x>>v)&1)<<i for i,v in enumerate(shore[0]))
    b=sum(((x>>v)&1)<<i for i,v in enumerate(shore[1]))
    return encode(h0[b],h1[a])

visited=set();classes={1:Counter(),2:Counter()}
for a in fix0:
    for b in fix1:
        start=encode(a,b)
        if start in visited:continue
        period=1 if update(start)==start else 2
        Q=deque([start]);visited.add(start);m=0
        while Q:
            x=Q.popleft();m+=1
            for y in [update(x)]+[transform(x,p) for p in perms]:
                if y not in visited:visited.add(y);Q.append(y)
        classes[period][m]+=1
assert len(visited)==494**2
assert sum(k*v for k,v in classes[1].items())==494
assert sum(k*v for k,v in classes[2].items())==494**2-494

out={
    'vertices':24,'edges':36,'automorphism_count':len(group),
    'shore_fixed_points':[len(fix0),len(fix1)],
    'shore_preperiod_histogram':{str(k):v for k,v in sorted(Counter(d0.values()).items())},
    'shore_basin_histogram':{str(k):v for k,v in sorted(Counter(b0.values()).items())},
    'full_first_entry_counts':{str(i):P[i] for i in range(6)},
    'full_first_entry_cumulative':{str(i):C[i] for i in range(6)},
    'fixed_configurations':494,
    'two_cycle_orbits':(494**2-494)//2,
    'basin_total_fixed':sum(k*v for k,v in fixed_basins.items()),
    'basin_total_period_two':sum(k*v for k,v in two_basins.items()),
    'fixed_basin_histogram':{str(k):v for k,v in sorted(fixed_basins.items())},
    'two_cycle_basin_histogram':{str(k):v for k,v in sorted(two_basins.items())},
    'fixed_symmetry_class_sizes':{str(k):v for k,v in sorted(classes[1].items())},
    'two_symmetry_class_sizes':{str(k):v for k,v in sorted(classes[2].items())},
    'fixed_symmetry_classes':sum(classes[1].values()),
    'two_symmetry_classes':sum(classes[2].values())
}
print(json.dumps(out,sort_keys=True,indent=2))
