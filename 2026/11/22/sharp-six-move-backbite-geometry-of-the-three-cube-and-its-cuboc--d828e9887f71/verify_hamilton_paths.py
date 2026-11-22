"""Independent vertex-path enumeration and endpoint-rotation certificate on Q3."""
from collections import Counter,deque
from itertools import permutations,product

neighbors=[tuple(v^(1<<j) for j in range(3)) for v in range(8)]
paths=set()
def visit(seq):
    if len(seq)==8:
        paths.add(min(tuple(seq),tuple(reversed(seq))))
        return
    for w in neighbors[seq[-1]]:
        if w not in seq:visit(seq+[w])
for v in range(8):visit([v])
paths=sorted(paths)
assert len(paths)==72
index={p:i for i,p in enumerate(paths)}
# Endpoint rotation: link an endpoint to a new adjacent interior vertex,
# removing the unique old path edge that closes the resulting cycle.
def rotations(p):
    result=set()
    for q in (p,tuple(reversed(p))):
        for k in range(2,8):
            if q[k] in neighbors[q[0]]:
                r=tuple(reversed(q[:k]))+(q[k],)+q[k+1:]
                result.add(min(r,tuple(reversed(r))))
    return result
rot=[{index[r] for r in rotations(p)} for p in paths]
assert all(len(a)==4 for a in rot)
assert all(i in rot[j] for i,aa in enumerate(rot) for j in aa)

def edge_set(p):
    return frozenset(tuple(sorted((a,b))) for a,b in zip(p,p[1:]))
edges=[edge_set(p) for p in paths]
jump=[set() for _ in paths]
for i,p in enumerate(paths):
    for j in range(len(paths)):
        if i!=j and len(edges[i]&edges[j])==6:jump[i].add(j)
assert all(rot[i] <=jump[i] for i in range(72))

def shells(A):
    ecc=[];dist_total=Counter();profiles=[]
    for i in range(72):
        dist={i:0};queue=deque([i])
        while queue:
            v=queue.popleft()
            for w in A[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;queue.append(w)
        assert len(dist)==72
        ec=max(dist.values());ecc.append(ec)
        profiles.append(tuple(Counter(dist.values())[k] for k in range(ec+1)))
        for j in range(i+1,72):dist_total[dist[j]]+=1
    return Counter(ecc),dist_total,Counter(profiles),profiles
rs= shells(rot); js=shells(jump)
assert rs[0]=={6:72} and rs[1]=={1:144,2:408,3:624,4:732,5:504,6:144}
assert js[0]=={6:72} and js[1]=={1:264,2:408,3:576,4:684,5:480,6:144}
assert Counter(map(len,jump))=={9:48,4:24}
# The full 48 cube symmetries are affine coordinate permutations + XOR translations.
aut=[]
for perm in permutations(range(3)):
    for shift in range(8):
        image=tuple((sum(((v>>k)&1)<<perm[k] for k in range(3)))^shift for v in range(8))
        aut.append(image)
assert len(set(aut))==48
seen=set();orbits=[]
for i,p in enumerate(paths):
    if i in seen:continue
    orb={index[min(tuple(g[x] for x in p),tuple(g[x] for x in reversed(p)))] for g in aut}
    seen |= orb
    profile=rs[3][i]
    assert all(rs[3][j]==profile for j in orb)
    ep=(p[0]^p[-1]).bit_count()
    counts=tuple(sorted(sum((a^b)==(1<<k) for a,b in zip(p,p[1:])) for k in range(3)))
    orbits.append((len(orb),ep,counts,profile,js[3][i]))
assert sorted(x[0] for x in orbits)==[24,24,24]
assert sorted(x[3] for x in orbits)==sorted([(1,4,11,17,21,13,5),(1,4,12,18,24,10,3),(1,4,11,17,16,19,4)])
print('Hamilton paths=',len(paths),'48 cube automorphisms, orbits=',len(orbits))
for x in sorted(orbits): print('orbit(size, endpoint distance, sorted axis counts, slide shells, jump shells)=',x)
print('endpoint/backbite edges=',sum(map(len,rot))//2,'degrees',dict(Counter(map(len,rot))))
print('all exchanges=',sum(map(len,jump))//2,'degrees',dict(Counter(map(len,jump))))
print('slide pair histogram=',dict(sorted(rs[1].items())),'jump pair histogram=',dict(sorted(js[1].items())))
print('pass')
