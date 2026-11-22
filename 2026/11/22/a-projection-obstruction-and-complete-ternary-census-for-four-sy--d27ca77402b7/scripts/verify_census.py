#!/usr/bin/env python3
"""Exact finite census for ternary length-four comma-free distance-three codes.
No third-party libraries. Exhaustively adds codewords in ascending lexicographic order.
"""
from itertools import product, permutations
from collections import Counter

sigma='012'
all_words=[''.join(w) for w in product(sigma, repeat=4)]
def middle(x,y):
    xy=x+y
    return (xy[1:5],xy[2:6],xy[3:7])
words=tuple(w for w in all_words if w not in middle(w,w))
assert len(words)==72
index={w:i for i,w in enumerate(words)}
N=len(words)
adj=[[] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if sum(x!=y for x,y in zip(words[i],words[j]))>=3:
            adj[i].append(j)
# For any a,b, and any possible z, test all 3 shifted frames,
# including repeated a,b,z. This is independent of the adjacency graph.
def valid(triple):
    S={words[i] for i in triple}
    return not any(v in S for x in S for y in S for v in middle(x,y))

counts=Counter()
optimal=[]
visited=0

def search(prefix,candidates):
    global visited
    if prefix:
        visited+=1
        assert valid(prefix)
        counts[len(prefix)]+=1
        if len(prefix)==5: optimal.append(tuple(words[i] for i in prefix))
    for i,c in enumerate(candidates):
        new=prefix+(c,)
        if not valid(new):continue
        nxt=[x for x in candidates[i+1:] if x in neighbor[c]]
        search(new,nxt)
neighbor=[set(a) for a in adj]
search((),list(range(N)))
assert counts[5]==1548 and not any(k>5 for k in counts)
assert counts[1]==72
perms=list(permutations(sigma))
def transform(c,p,rev):
    return tuple(sorted(''.join(p[int(x)] for x in (w[::-1] if rev else w)) for w in c))
optset=set(optimal)
unseen=set(optimal);orbit_sizes=[]
while unseen:
    c=min(unseen)
    orbit={transform(c,p,r) for p in perms for r in (0,1)}
    assert orbit <= optset
    unseen.difference_update(orbit)
    orbit_sizes.append(len(orbit))
assert len(orbit_sizes)==129 and Counter(orbit_sizes)=={12:129}
print('candidate_words',len(words),'distance_3_pairs',sum(map(len,adj)))
print('valid_by_size',dict(sorted(counts.items())))
print('optimal_count',len(optimal),'orbits',len(orbit_sizes),'orbit_size_hist',dict(Counter(orbit_sizes)))
print('example', ' '.join(optimal[0]))
