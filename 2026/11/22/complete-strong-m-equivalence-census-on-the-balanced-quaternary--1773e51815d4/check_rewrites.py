#!/usr/bin/env python3
"""Independent finite graph/structural check of the (2,2,2,2) theorem.

Does NOT compute scattered-subword signatures; it independently counts local
abba <-> baab switch edges and their connected components.
"""
from itertools import permutations
from collections import Counter

W={''.join(p) for p in permutations('00112233')}
assert len(W)==2520

# Exact SE step with two occurrences each: ABBA <-> BAAB.
def neighbors(w):
    for i in range(5):
        x=w[i:i+4]
        a,b=x[0],x[1]
        if a!=b and x==a+b+b+a:
            yield w[:i]+b+a+a+b+w[i+4:]

# Both orientations are already of form ABBA (rename a,b), so one branch suffices.
N={w:set(neighbors(w)) for w in W}
assert all(v in W and w in N[v] for w,neighbors_set in N.items() for v in neighbors_set)
assert sum(map(len,N.values()))==360
visited=set()
components=[]
for start in sorted(W):
    if start in visited:
        continue
    queue=[start]
    visited.add(start)
    component=set([start])
    while queue:
        u=queue.pop()
        for v in N[u]:
            if v not in visited:
                component.add(v)
                visited.add(v)
                queue.append(v)
    components.append(component)
size_distribution=Counter(map(len,components))
assert size_distribution=={1:2184,2:156,4:6}
assert sum(len(c) for c in components)==2520
# All size-four components have two non-overlapping independent toggles.
assert all(all(len(N[w])==2 for w in c) for c in components if len(c)==4)
assert all(len(N[w])==1 for c in components if len(c)==2 for w in c)
# The six quartets are indexed by an ORDERED split of the four labels into pairs.
quadreps=sorted(min(c) for c in components if len(c)==4)
assert len(quadreps)==6
assert all(set((w[0],w[1],w[4],w[5]))==set('0123') for w in quadreps)
print('vertices=2520')
print('undirected_edges=180')
print('rewrite_components=2346')
print('component_size_histogram='+str(sorted(size_distribution.items())))
print('four_word_class_representatives='+str(quadreps))
