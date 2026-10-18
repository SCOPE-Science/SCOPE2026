#!/usr/bin/env python3
import itertools, json
from collections import Counter, defaultdict, deque

N=8
# Generalized Petersen graph G(8,3): outer vertices 0..7, inner 8..15.
V=tuple(range(16))
edges=set()
for i in range(N):
    edges.add(tuple(sorted((i,(i+1)%N))))
    edges.add(tuple(sorted((i,8+i))))
    edges.add(tuple(sorted((8+i,8+((i+3)%N)))))
edges=tuple(sorted(edges))
assert len(edges)==24
adj={v:set() for v in V}
for a,b in edges:
    adj[a].add(b); adj[b].add(a)

def all_distances():
    out={}
    for s in V:
        d={s:0}; q=deque([s])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y]=d[x]+1; q.append(y)
        assert len(d)==16
        out[s]=d
    return out
D=all_distances()
assert max(D[a][b] for a in V for b in V)==4

def is_face(S,r):
    L=tuple(S)
    return all(D[L[i]][L[j]]<=r for i in range(len(L)) for j in range(i+1,len(L)))

def faces_at(r):
    F=set()
    for mask in range(1,1<<16):
        S=frozenset(i for i in V if mask>>i & 1)
        if is_face(S,r): F.add(S)
    return F

def incidence(upper,lower):
    su=tuple(sorted(upper)); sl=tuple(sorted(lower))
    assert len(su)==len(sl)+1
    for k in range(len(su)):
        if su[:k]+su[k+1:]==sl:
            return -1 if k%2 else 1
    raise AssertionError

def toggle_matching(F,order):
    unmatched=set(F); pairs=[]
    for v in order:
        lowers=sorted((f for f in unmatched if v not in f and (f|{v}) in unmatched), key=lambda x:(len(x),tuple(sorted(x))))
        for f in lowers:
            g=f|{v}
            if f in unmatched and g in unmatched:
                unmatched.remove(f); unmatched.remove(g); pairs.append((f,g))
    return pairs,unmatched

def hasse_and_paths(F,pairs,crit):
    low_to_up={a:b for a,b in pairs}
    succ={f:[] for f in F}; indeg={f:0 for f in F}; wt={}
    for up in F:
        if len(up)<=1: continue
        for x in up:
            lo=frozenset(set(up)-{x})
            if not lo: continue
            s=incidence(up,lo)
            if low_to_up.get(lo)==up:
                a,b=lo,up; w=-s
            else:
                a,b=up,lo; w=s
            succ[a].append(b); indeg[b]+=1; wt[(a,b)]=w
    q=deque(sorted((f for f in F if indeg[f]==0),key=lambda x:(len(x),tuple(sorted(x)))))
    topo=[]
    while q:
        x=q.popleft(); topo.append(x)
        for y in succ[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert len(topo)==len(F), 'matching Hasse orientation has a directed cycle'
    pos={x:i for i,x in enumerate(topo)}
    c2=sorted((f for f in crit if len(f)==3),key=lambda x:tuple(sorted(x)))
    c3=sorted((f for f in crit if len(f)==4),key=lambda x:tuple(sorted(x)))
    B=[]
    for s in c3:
        dp={s:1}
        for x in topo[pos[s]:]:
            val=dp.get(x,0)
            if not val: continue
            for y in succ[x]:
                dp[y]=dp.get(y,0)+val*wt[(x,y)]
        B.append([dp.get(t,0) for t in c2])
    return topo,c2,c3,B

# Scale 1.
F1=faces_at(1)
f1=Counter(len(f)-1 for f in F1)
assert f1==Counter({1:24,0:16})
assert 24-16+1==9

# Scale 2 exact discrete-Morse certificate.
F2=faces_at(2)
f2=Counter(len(f)-1 for f in F2)
assert f2==Counter({2:112,1:72,3:48,0:16})
order=[13,2,12,11,7,1,5,3,0,10,4,8,6,9,14,15]
pairs,crit=toggle_matching(F2,order)
cc=Counter(len(f)-1 for f in crit)
assert len(pairs)==118
assert cc==Counter({2:9,3:2,0:1})
topo,c2,c3,B=hasse_and_paths(F2,pairs,crit)
assert B==[[0]*9,[0]*9]

# Scale 3: exactly one forbidden partner per vertex, hence boundary of 8-cross-polytope.
far=sorted(tuple(sorted((a,b))) for a,b in itertools.combinations(V,2) if D[a][b]==4)
assert len(far)==8
assert sorted(x for e in far for x in e)==list(V)
F3=faces_at(3)
f3=Counter(len(f)-1 for f in F3)
expected={d: (2**(d+1))*__import__('math').comb(8,d+1) for d in range(8)}
assert dict(sorted(f3.items()))==expected
assert len(F3)==3**8-1

# Scale 4 is the full 15-simplex.
assert all(D[a][b]<=4 for a,b in itertools.combinations(V,2))

out={
  'graph': {'vertices':16,'edges':24,'diameter':4,'cycle_rank':9,'distance_4_pairs':[list(e) for e in far]},
  'scale_1': {'f_vector':[16,24],'homotopy':'wedge_9_S1'},
  'scale_2': {
      'f_vector':[16,72,112,48],
      'nonempty_faces':len(F2),
      'toggle_order':order,
      'matched_pairs':len(pairs),
      'critical_counts':{str(k):v for k,v in sorted(cc.items())},
      'critical_2_cells':[sorted(f) for f in c2],
      'critical_3_cells':[sorted(f) for f in c3],
      'morse_boundary_3_to_2':B,
      'hasse_acyclic':True,
      'homotopy':'wedge_9_S2_vee_wedge_2_S3'
  },
  'scale_3': {'f_vector':[f3[d] for d in range(8)],'nonempty_faces':len(F3),'homotopy':'S7'},
  'scale_4': {'homotopy':'contractible'},
  'verification':'PASS'
}
print(json.dumps(out,sort_keys=True,separators=(',',':')))
