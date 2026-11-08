#!/usr/bin/env python3
"""Exhaustive incidence-model check for minimum independent domination of H(5,2)."""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256

P = list(combinations(range(5), 2))
U = (1 << 10) - 1
D = [sum(1 << j for j, p in enumerate(P) if set(a).isdisjoint(p)) for a in P]

def partner(a):
    b = U
    for j in range(10):
        if a >> j & 1:
            b &= U ^ D[j]
    return b

closed = [(a, partner(a)) for a in range(1 << 10) if partner(partner(a)) == a]
profile = Counter((a.bit_count(), b.bit_count()) for a,b in closed)
assert len(closed) == 187
assert profile == {(0,10):1,(1,7):10,(2,4):15,(2,5):30,(3,3):70,(4,2):15,(4,4):5,(5,2):30,(7,1):10,(10,0):1}, profile
S = [a | (b << 10) for a,b in closed if a.bit_count() + b.bit_count() == 6]
assert len(S) == 100
S = sorted(S)
# Each closed pair represents an independent dominating set; its omitted
# ground-set labels classify whether the state is frozen or mobile.
def label_support(s):
    edges = [P[j] for j in range(10) if (s >> j & 1) or (s >> (10+j) & 1)]
    return frozenset(x for e in edges for x in e)
assert Counter(len(label_support(s)) for s in S) == {3:10,4:90}
assert Counter((s&U).bit_count() for s in S)=={2:15,3:70,4:15}
# Direct token-slide neighbors on the bipartite Kneser graph.
idx = {s:i for i,s in enumerate(S)}
N = [D[i] << 10 for i in range(10)] + [D[i] for i in range(10)]
adj = [set() for s in S]
for i,s in enumerate(S):
    for v in range(20):
        if not (s>>v&1): continue
        for w in range(20):
            if s>>w&1 or not (N[v]>>w&1): continue
            t = s ^ (1<<v) ^ (1<<w)
            if t in idx: adj[i].add(idx[t])
assert all(i in adj[j] for i,L in enumerate(adj) for j in L)
assert Counter(map(len,adj)) == {0:10,2:60,4:30}
assert sum(map(len,adj))//2==120
seen=set();parts=[]
for i in range(100):
    if i in seen:continue
    cc=[i];seen.add(i)
    for v in cc:
        for w in adj[v]:
            if w not in seen:seen.add(w);cc.append(w)
    parts.append(cc)
assert Counter(map(len,parts)) == {1:10,18:5}
assert all(len(label_support(S[c[0]]))==3 for c in parts if len(c)==1)
Qparts=[c for c in parts if len(c)==18]
assert all(len({tuple(sorted(label_support(S[i]))) for i in c})==1 for c in Qparts)
assert len({tuple(sorted(label_support(S[c[0]]))) for c in Qparts})==5
for cc in Qparts:
    hi={i for i in cc if len(adj[i])==4};lo=set(cc)-hi
    assert len(hi)==6 and len(lo)==12
    assert all(len(adj[i])==2 and adj[i] <= hi for i in lo)
    pairs=Counter(tuple(sorted(adj[i])) for i in lo)
    assert len(pairs)==6 and set(pairs.values())=={2}
    # Suppressing each degree-two vertex, then forgetting double edges,
    # must give a connected, 2-regular graph on the six high vertices.
    base={i:set() for i in hi}
    for (u,v),number in pairs.items():base[u].add(v);base[v].add(u)
    assert all(len(base[i])==2 for i in hi)
    q=[next(iter(hi))];visited=set(q)
    for i in q:
        for j in base[i]:
            if j not in visited:visited.add(j);q.append(j)
    assert len(visited)==6
    # All states have eccentricity 6.
    for root in cc:
        dist={root:0};todo=deque([root])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if w not in dist:dist[w]=dist[v]+1;todo.append(w)
        assert len(dist)==18 and max(dist.values())==6
# Explicit isomorphism to the generalized Petersen presentation.
phi=[0,17,6,11,9,10,7,16,1,19,18,3,12,5,14,8,13,2,15,4]
assert sorted(phi)==list(range(20))
Egp=set()
for v in range(10):
    for a,b in ((v,(v+1)%10),(v,10+v),(10+v,10+(v+3)%10)):
        Egp.add(tuple(sorted((phi[a],phi[b]))))
Einc={tuple(sorted((u,v))) for u in range(20) for v in range(u+1,20) if N[u]>>v&1}
assert len(Egp)==len(Einc)==30 and Egp==Einc

# Independently generate the predicted states, without filtering through S.
expected=set()
for T in combinations(range(5),3):
    a=sum(1<<j for j,p in enumerate(P) if set(p)<=set(T))
    assert a.bit_count()==3 and partner(a)==a
    expected.add(a | (a<<10))
for Q in combinations(range(5),4):
    eq=[j for j,p in enumerate(P) if set(p)<=set(Q)]
    full=sum(1<<j for j in eq)
    for x,y in combinations(eq,2):
        if set(P[x]).isdisjoint(P[y]):
            a=(1<<x)|(1<<y); b=full^a
            assert partner(a)==b and partner(b)==a
            expected.add(a | (b<<10)); expected.add(b | (a<<10))
    for triple in combinations(eq,3):
        degree=Counter(v for j in triple for v in P[j])
        if sorted(degree.values())==[1,1,2,2]:
            a=sum(1<<j for j in triple);b=partner(a)
            assert (a&~full)==0 and (b&~full)==0 and b.bit_count()==3
            assert partner(b)==a
            expected.add(a | (b<<10))
assert len(expected)==100 and expected==set(S)
# The matching-index quotient is K_{3,3} minus its diagonal,
# with two internally distinct length-two routes for each quotient edge.
for cc in Qparts:
    Q=label_support(S[cc[0]])
    high=[i for i in cc if len(adj[i])==4]
    key={}
    for i in high:
        a=S[i]&U; b=S[i]>>10
        small=a if a.bit_count()==2 else b
        matching=tuple(P[j] for j in range(10) if small>>j&1)
        assert len(matching)==2 and set(matching[0]).isdisjoint(matching[1])
        key[i]=(0 if a.bit_count()==2 else 1, tuple(sorted(matching)))
    assert len(key)==6
    counts=Counter()
    for i in cc:
        if len(adj[i])==2:
            x,y=sorted(adj[i]); t0,p0=key[x]; t1,p1=key[y]
            assert t0!=t1 and p0!=p1
            counts[(p0,p1) if t0==0 else (p1,p0)]+=1
    assert len(counts)==6 and set(counts.values())=={2}

# Four-label mobile states have exactly six possible occupied vertices.
for cc in Qparts:
    profiles=Counter((S[v]&U).bit_count() for v in cc)
    assert profiles == {2:3,3:12,4:3}
# The extra ten frozen states are the symmetric triangles.
for cc in parts:
    if len(cc)!=1:continue
    a,b=closed[[a|(b<<10) for a,b in closed].index(S[cc[0]])]
    assert a==b and a.bit_count()==3
lines=[f'{s:05x}' for s in S]
edges=sorted((S[i],S[j]) for i in range(100) for j in adj[i] if i<j)
print('OK closure_pairs=187 minimum_size=6 states=100 edges=120 components=10K1+5D(C6 doubled) ecc=6')
print('PROFILE',sorted(profile.items()))
print('STATE_SHA256',sha256(('\n'.join(lines)+'\n').encode()).hexdigest())
print('EDGE_SHA256',sha256(('\n'.join(f'{a:05x} {b:05x}' for a,b in edges)+'\n').encode()).hexdigest())
