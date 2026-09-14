"""Petersen graph as Kneser KG(5,2): vertices = 2-subsets of {0..4}, edges = disjoint pairs."""
from itertools import combinations

BASE = list(combinations(range(5), 2))  # 10 vertices
IDX = {v: i for i, v in enumerate(BASE)}
EDGES = []
for i, u in enumerate(BASE):
    for j, v in enumerate(BASE):
        if j > i and set(u).isdisjoint(v):
            EDGES.append((i, j))
NBR = {i: set() for i in range(10)}
for u, v in EDGES:
    NBR[u].add(v); NBR[v].add(u)

def girth():
    # brute force shortest cycle
    best = 99
    bestc = None
    # BFS from each vertex for shortest cycle through it
    for s in range(10):
        # find shortest cycle: standard BFS on pairs
        import collections
        INF = 99
        dist = {}
        q = collections.deque()
        for w in NBR[s]:
            dist[(s, w)] = 1
            q.append((s, w))
        while q:
            a, b = q.popleft()
            for c in NBR[b]:
                if c == a:
                    continue
                if c == s:
                    if dist[(a, b)] + 1 >= 3 and dist[(a, b)] + 1 < best:
                        best = dist[(a, b)] + 1
                else:
                    if (b, c) not in dist:
                        dist[(b, c)] = dist[(a, b)] + 1
                        q.append((b, c))
    return best

def all_minimal_covers():
    covers = []
    for mask in range(1 << 10):
        ok = True
        for u, v in EDGES:
            if not ((mask >> u) & 1 or (mask >> v) & 1):
                ok = False; break
        if not ok:
            continue
        minimal = True
        for w in range(10):
            if (mask >> w) & 1:
                m2 = mask ^ (1 << w)
                ok2 = True
                for u, v in EDGES:
                    if not ((m2 >> u) & 1 or (m2 >> v) & 1):
                        ok2 = False; break
                if ok2:
                    minimal = False; break
        if minimal:
            covers.append(mask)
    return covers

def max_independent():
    best = []
    for mask in range(1 << 10):
        s = bin(mask).count('1')
        if s <= len(best):
            continue
        ok = True
        for u, v in EDGES:
            if (mask >> u) & 1 and (mask >> v) & 1:
                ok = False; break
        if ok:
            best = [i for i in range(10) if (mask >> i) & 1]
    return best

if __name__ == '__main__':
    print('n=10 check:', len(BASE), 'edges:', len(EDGES))
    print('degrees:', sorted(len(NBR[i]) for i in range(10)))
    print('girth:', girth())
    covers = all_minimal_covers()
    from collections import Counter
    print('num minimal covers:', len(covers))
    print('size distribution:', sorted(Counter(bin(m).count('1') for m in covers).items()))
    ind = max_independent()
    print('max independent set size:', len(ind), ind, [BASE[i] for i in ind])
    # every C(10,5) subset check count of independent 5-sets
    n5 = 0
    for S in combinations(range(10), 5):
        ms = set(S)
        if all(not (u in ms and v in ms) for u, v in EDGES):
            n5 += 1
    print('independent 5-sets:', n5)
