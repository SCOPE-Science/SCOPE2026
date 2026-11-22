#!/usr/bin/env python3
"""Finite checks for four-colour single-vertex recolouring of friendship graphs.

The general theorem has a symbolic proof; these checks only detect errors in
small instances and compare two independently defined graph representations.
"""
from collections import deque, Counter
from itertools import permutations, product
from math import factorial

PALETTE = tuple(range(4))

def colorings(t):
    for hub in PALETTE:
        pairs = [p for p in permutations(PALETTE, 2) if hub not in p]
        for blades in product(pairs, repeat=t):
            yield (hub,) + tuple(c for pair in blades for c in pair)

def legal(s):
    t = (len(s)-1)//2
    if len(s) != 2*t+1 or len(set(s[:3])) != 3:
        return False
    return all(len({s[0],s[2*i+1],s[2*i+2]}) == 3 for i in range(t))

def neighbours(s):
    n = len(s)
    for p in range(n):
        for c in PALETTE:
            if c == s[p]:
                continue
            w = s[:p] + (c,) + s[p+1:]
            if legal(w):
                yield w

def key(s):
    # An orbit invariant under global palette renaming and blade permutation;
    # one representative is chosen per such class, not necessarily per full orbit.
    h = s[0]
    others = [c for c in PALETTE if c != h]
    return min(tuple(sorted((dict(zip(others,p))[s[2*i+1]],
                             dict(zip(others,p))[s[2*i+2]])
                       for i in range((len(s)-1)//2)))
               for p in permutations((1,2,3)))

def shortest_distances(s,adj):
    d = {s:0}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1
                q.append(v)
    return d

def check(t):
    s = list(colorings(t))
    S = set(s)
    assert len(S)==4*6**t and all(legal(x) for x in S)
    adj = {}
    for x in s:
        adj[x] = tuple(neighbours(x))
        assert len(set(adj[x])) == len(adj[x])
        assert all(y in S for y in adj[x])
    e = sum(map(len,adj.values()))//2
    hub_edges=sum(sum(y[0]!=x[0] for y in adj[x]) for x in s)//2
    assert e == 4*t*6**t + 6*2**t, (t,e)
    assert hub_edges == 6*2**t
    assert all(x in adj[y] for x in s for y in adj[x])
    deg=Counter(len(adj[x]) for x in s)
    assert deg == Counter({2*t+1:12*2**t, 2*t:4*6**t-12*2**t}) if t>=2 else deg == {3:24}
    reps={}
    for x in s:
        reps.setdefault(key(x),x)
    eccentricities=[]
    for x in reps.values():
        d=shortest_distances(x,adj)
        assert len(d)==len(S), (t,x,len(d))
        eccentricities.append(max(d.values()))
    assert min(eccentricities)==max(eccentricities)==3*t+1
    # Construct the uniform-petal witness; direct shortest-distance confirmation.
    source=(0,)+ (1,2)*t
    target=(3,)+ (2,1)*t
    assert shortest_distances(source,adj)[target] == 3*t+1
    print(f't={t}: vertices={len(S)} edges={e} hub_edges={hub_edges} '
          f'gateway_states={12*2**t} symmetry_reps={len(reps)} '
          f'radius=diameter={3*t+1} witness_distance={3*t+1}')

def check_symbolic_local():
    # For fixed hub, the 6 legal ordered pairs form a six-cycle.  For
    # distinct initial/final hub colours, the two shared legal pairs are
    # antipodal in both local six-cycles, giving min detour <= 3.
    for h in PALETTE:
        pairs=[p for p in permutations(PALETTE,2) if h not in p]
        adj={p:[q for q in pairs if sum(a!=b for a,b in zip(p,q))==1]
             for p in pairs}
        assert len(pairs)==6 and all(len(adj[p])==2 for p in pairs)
        D={p:shortest_distances(p,adj) for p in pairs}
        assert all(len(D[p])==6 and max(D[p].values())==3 for p in pairs)
        for h2 in PALETTE:
            if h==h2:continue
            shared=[p for p in pairs if h2 not in p]
            assert len(shared)==2 and D[shared[0]][shared[1]]==3
            qpair=[p for p in permutations(PALETTE,2) if h2 not in p]
            adj2={p:[q for q in qpair if sum(a!=b for a,b in zip(p,q))==1]
                  for p in qpair}
            D2={p:shortest_distances(p,adj2) for p in qpair}
            assert D2[shared[0]][shared[1]]==3
            assert all(min(D[a][g]+D2[b][g] for g in shared)<=3
                       for a in pairs for b in qpair)
    print('12 ordered center transitions: verified six-cycle gateway-antipode lemma')

if __name__=='__main__':
    check_symbolic_local()
    for t in range(1,6):
        check(t)
    print('All finite checks passed; general proof is separate.')
