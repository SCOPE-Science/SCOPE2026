#!/usr/bin/env python3
"""Direct checks for the q-ary two-read one-deletion confusability clique theorem."""
from itertools import product, combinations
import networkx as nx


def deletion_ball(word):
    return {word[:i] + word[i + 1:] for i in range(len(word))}


def alternating_intervals(word):
    n = len(word)
    for a in range(n):
        for b in range(a + 1, n):
            v = word[a:b+1]
            if all(v[i] == v[i % 2] for i in range(len(v))) and v[0] != v[1]:
                yield (a,b)


def toggle_interval(word, a, b):
    pair = word[a:a+2]
    changed = tuple(pair[(i-a+1)%2] for i in range(a,b+1))
    return word[:a] + changed + word[b+1:]


def graph_by_direct_balls(q,n):
    words=list(product(range(q), repeat=n))
    balls=[deletion_ball(w) for w in words]
    G=nx.Graph()
    G.add_nodes_from(range(len(words)))
    for i in range(len(words)):
        for j in range(i):
            if len(balls[i] & balls[j]) == 2:
                G.add_edge(i,j)
    return G,words


def classify_intervals(word, intervals):
    """Verify the one-pencil/two-pencil dichotomy for a clique anchor."""
    if len(intervals) <= 1:
        return True
    def intersects(a, b):
        return max(a[0], b[0]) <= min(a[1], b[1])
    disjoint = [(a,b) for i,a in enumerate(intervals)
                for b in intervals[i+1:] if not intersects(a,b)]
    if not disjoint:
        return (len({a for a,b in intervals}) == 1 or
                len({b for a,b in intervals}) == 1)
    I,J = disjoint[0]
    if J[0] < I[0]:
        I,J = J,I
    a,b = I
    c,d = J
    if c != b+1 or word[b] != word[c]:
        return False
    pair1 = {word[b-1],word[b]}
    pair2 = {word[c],word[c+1]}
    if pair1 != pair2:
        return False
    if any(v != b and u != c for u,v in intervals):
        return False
    left = sorted(u for u,v in intervals if v == b)
    right = sorted(v for u,v in intervals if u == c)
    return (all(t-s >= 2 for s,t in zip(left,left[1:])) and
            all(t-s >= 2 for s,t in zip(right,right[1:])))


def verify(q,n):
    G,words=graph_by_direct_balls(q,n)
    positions={w:i for i,w in enumerate(words)}
    seen=set()
    for i,w in enumerate(words):
        for a,b in alternating_intervals(w):
            y=toggle_interval(w,a,b)
            assert y!=w and y in positions
            j=positions[y]
            seen.add(tuple(sorted((i,j))))
    assert seen==set(tuple(sorted(e)) for e in G.edges), ('criterion',q,n)
    target=n//2+1
    maximal=list(nx.find_cliques(G))
    measured=max(map(len,maximal))
    assert measured==target, ('clique',q,n,measured,target)
    for clique in maximal:
        for root in clique:
            base=words[root]
            toggles={toggle_interval(base,a,b):(a,b)
                     for a,b in alternating_intervals(base)}
            ints=[toggles[words[v]] for v in clique if v!=root]
            assert classify_intervals(base, ints), ('classification',q,n,base,ints)
    # Explicit all-length lower bound construction instantiated at each n.
    base=tuple(i%2 for i in range(n))
    cand=[base]+[toggle_interval(base,0,2*k-1) for k in range(1,n//2+1)]
    assert len(set(cand))==target
    for a,b in combinations(cand,2):
        assert len(deletion_ball(a)&deletion_ball(b))==2
    return len(words),G.number_of_edges(),len(maximal),measured


def check_family(q,n):
    print('q,n,vertices,edges,maximal_cliques,omega')
    print(q,n,*verify(q,n))


if __name__=='__main__':
    for n in range(2,10):
        check_family(2,n)
    for n in range(2,7):
        check_family(3,n)
    # Four-letter alphabet provides a second independent nonbinary check.
    for n in range(2,5):
        check_family(4,n)
    print('All direct comparisons and clique checks passed.')
