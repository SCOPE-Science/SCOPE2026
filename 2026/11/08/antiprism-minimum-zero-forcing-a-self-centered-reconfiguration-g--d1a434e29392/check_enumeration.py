"""Independent exhaustive zero-forcing enumeration for powers of even cycles.
Usage: python3 check_enumeration.py
"""
from itertools import combinations
from collections import Counter, deque

def closure_time(m, initial):
    neighbors = [sum(1 << ((v + d) % m) for d in (-2, -1, 1, 2)) for v in range(m)]
    full = (1 << m) - 1
    blue = sum(1 << v for v in initial)
    time = 0
    while blue != full:
        new = 0
        for v in range(m):
            if blue & (1 << v):
                missing = neighbors[v] & ~blue
                if missing and not (missing & (missing - 1)):
                    new |= missing
        if not new:
            return None
        blue |= new
        time += 1
    return time

def expected(m):
    return {frozenset((i + d) % m for d in offsets): (m // 2 - 2 if label == 'A' else m // 2 - 1)
            for label, offsets in (('A',(0,1,2,3)), ('B',(0,1,2,4)), ('C',(-2,0,1,2)))
            for i in range(m)}

def graph(states):
    sets = list(states)
    edges = {i:set() for i in range(len(sets))}
    for i, S in enumerate(sets):
        for j in range(i):
            if len(S & sets[j]) == 3:
                edges[i].add(j)
                edges[j].add(i)
    return sets,edges

def ecc(g,s):
    dist = {s:0}
    queue = deque([s])
    while queue:
        a = queue.popleft()
        for b in g[a]:
            if b not in dist:
                dist[b] = dist[a] + 1
                queue.append(b)
    return max(dist.values()) if len(dist)==len(g) else None

def main():
    for m in range(8, 27, 2):
        found = {}
        for S in combinations(range(m), 4):
            time = closure_time(m, S)
            if time is not None:
                found[frozenset(S)] = time
        pred = expected(m)
        assert found == pred, (m, len(found), len(pred), set(found)^set(pred))
        states,edges=graph(found)
        assert len(states)==3*m
        assert sum(map(len,edges.values()))//2 == 9*m
        assert Counter(map(len, edges.values())) == Counter({8:m,5:2*m})
        if m <= 24:
            ec = [ecc(edges,s) for s in edges]
            assert set(ec) == {m//2}, (m,set(ec))
        print('PASS',m,'sets',len(found),'pt',dict(Counter(found.values())), 'edges', 9*m, 'diameter', m//2)
    print('PYTHON_EXHAUSTIVE_PASS')
if __name__ == '__main__':main()
