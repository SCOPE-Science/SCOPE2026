"""Exact connected-domination and optimal-exchange census for the 13-vertex Paley graph.
Python standard library; no downloaded tables are used.
"""
from collections import Counter, deque
from itertools import combinations

P=13
QUADRATIC={x*x%P for x in range(1,P)}
assert QUADRATIC=={1,3,4,9,10,12}
ADJ=[sum(1<<j for j in range(P) if (j-i)%P in QUADRATIC) for i in range(P)]
FULL=(1<<P)-1

def connected(mask):
    if not mask:return False
    seen=mask & -mask
    while True:
        newly=seen
        for i in range(P):
            if seen>>i & 1:newly|=ADJ[i]&mask
        if newly==seen:return seen==mask
        seen=newly

def dominating(mask):
    cover=mask
    for i in range(P):
        if mask>>i & 1:cover|=ADJ[i]
    return cover==FULL

def is_cd(mask):return dominating(mask) and connected(mask)

all_cd={s for s in range(1,FULL+1) if is_cd(s)}
by_size=Counter(s.bit_count() for s in all_cd)
minimal=[s for s in sorted(all_cd) if all(s^(1<<i) not in all_cd for i in range(P) if s>>i&1)]
assert len(minimal)==260 and set(s.bit_count() for s in minimal)=={4}

pos={s:i for i,s in enumerate(minimal)}
exchange=[set() for s in minimal]
for j,s in enumerate(minimal):
    for removed in range(P):
        if not(s>>removed&1):continue
        for inserted in range(P):
            if s>>inserted&1:continue
            t=s^(1<<removed)^(1<<inserted)
            if t in pos:exchange[j].add(pos[t])
assert all(i in exchange[j] for i,edges in enumerate(exchange) for j in edges)

def affine_image(s,m,b):
    return sum(1<<((m*i+b)%P) for i in range(P) if s>>i&1)

affine_orbits=[];done=set()
for s in minimal:
    if s in done:continue
    orbit={affine_image(s,m,b) for m in QUADRATIC for b in range(P)}
    assert orbit<=set(minimal)
    assert orbit.isdisjoint(done)
    done|=orbit
    affine_orbits.append((s,orbit))
assert len(done)==260 and len(affine_orbits)==5

def shells(src):
    dist={src:0};q=deque([src])
    while q:
        u=q.popleft()
        for v in exchange[u]:
            if v not in dist:dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==260
    return tuple(Counter(dist.values())[k] for k in range(5))

all_shells={s:shells(i) for i,s in enumerate(minimal)}
assert all(sum(shell)==260 and shell[-1]>0 for shell in all_shells.values())
print('connected_count_by_size', sorted(by_size.items()))
print('inclusion_minimal_count_by_size', [(4,len(minimal))])
print('minimum_exchange_vertices',len(minimal))
print('minimum_exchange_edges',sum(map(len,exchange))//2)
print('radius_diameter', min(len(shell)-1 for shell in all_shells.values()),max(len(shell)-1 for shell in all_shells.values()))
for rep,orb in affine_orbits:
    deg=len(exchange[pos[rep]])
    sh=all_shells[rep]
    assert all(len(exchange[pos[s]])==deg and all_shells[s]==sh for s in orb)
    print('orbit',hex(rep),'size',len(orb),'degree',deg,'shells',sh)
print('CHECKS_PASS')
