"""Independent exact check by signed linear separations and cube isometries."""
from itertools import combinations, product, permutations
from collections import Counter, deque

V = range(16)
Z = [z for z in product((-1,0,1), repeat=4) if any(z)]
def resolving(S):
    return all(any(sum((1-2*((s>>i)&1))*z[i] for i in range(4)) != 0
                   for s in S) for z in Z)

assert all(not resolving(S) for S in combinations(V,3))
states = sorted(combinations(V,4))
states = [frozenset(S) for S in states if resolving(S)]
index = {S: i for i,S in enumerate(states)}
N = len(states)
assert N == 928
# In four coordinates, resolving is also equivalent to nonsingularity
# of the four sign vectors (a special feature of 3x3 sign cofactors).
def determinant(S):
    A = [[1-2*((s>>j)&1) for j in range(4)] for s in S]
    ans = 0
    for p in permutations(range(4)):
        parity = sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        ans += (-1 if parity%2 else 1)*A[0][p[0]]*A[1][p[1]]*A[2][p[2]]*A[3][p[3]]
    return ans
assert all(resolving(S)==(determinant(S)!=0) for S in combinations(V,4))
print('invertible_sign_matrix_equivalence=PASS')

# An undirected edge is a single coordinate flip of one landmark.
adj = [set() for _ in range(N)]
for i,S in enumerate(states):
    for x in S:
        for b in range(4):
            y = x^(1<<b)
            if y not in S:
                j = index.get((S-{x})|{y})
                if j is not None:
                    adj[i].add(j)
assert all(i in adj[j] for i in range(N) for j in adj[i])

def distances(start):
    d={start:0}; q=deque((start,))
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1;q.append(v)
    assert len(d)==N
    return d

def move_bits(x,p):
    return sum(((x>>i)&1)<<p[i] for i in range(4))

def image(S,p,t):
    return frozenset(move_bits(x,p)^t for x in S)

orbits=[]; unseen=set(range(N))
for i in range(N):
    if i not in unseen:continue
    S=states[i]
    orbit={index[image(S,p,t)] for p in permutations(range(4)) for t in V}
    assert len(orbit)<=384 and orbit<=unseen
    unseen-=orbit
    es=Counter(max(distances(j).values()) for j in orbit)
    ds=Counter(len(adj[j]) for j in orbit)
    orbits.append((tuple(sorted(S)),len(orbit),dict(sorted(ds.items())),dict(sorted(es.items()))))

print('resolving_triples=0')
print('metric_bases=',N,sep='')
print('edges=',sum(map(len,adj))//2,sep='')
print('degree=',dict(sorted(Counter(map(len,adj)).items())),sep='')
print('orbit_count=',len(orbits),sep='')
for rep,sz,d,e in orbits:
    print('orbit rep=',rep,'size=',sz,'degree=',d,'eccentricity=',e)
print('eccentricity=',dict(sorted(Counter(max(distances(j).values()) for j in range(N)).items())),sep='')
assert len(orbits)==8
assert sorted(x[1] for x in orbits)==[16,16,64,64,192,192,192,192]
assert dict(Counter(map(len,adj)))=={7:512,8:384,16:32}
assert dict(Counter(max(distances(j).values()) for j in range(N)))=={8:64,9:592,10:272}
