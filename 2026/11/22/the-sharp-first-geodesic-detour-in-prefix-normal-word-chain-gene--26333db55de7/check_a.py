#!/usr/bin/env python3
"""Direct exhaustive check of prefix-normal generator swap graph, n <= 7.
No datasets or external libraries are required.
"""
from collections import Counter, deque
from itertools import permutations


def normal(bits):
    n = len(bits)
    pref = [0]
    for bit in bits:
        pref.append(pref[-1] + bit)
    return all(pref[j + k] - pref[j] <= pref[k]
               for k in range(1, n + 1)
               for j in range(n - k + 1))


def admissible(perm):
    n = len(perm)
    word = [1] * n
    for x in perm:
        word[x - 1] = 0
        if not normal(word):
            return False
    return True


def graph(n):
    vertices = [p for p in permutations(range(1, n + 1)) if admissible(p)]
    index = {p: i for i, p in enumerate(vertices)}
    edges = []
    for p in vertices:
        edges.append([index[v] for j in range(n - 1)
                      if (v := p[:j] + (p[j+1], p[j]) + p[j+2:]) in index])
    return vertices, edges


def kendall(p, q):
    pos = {letter: i for i, letter in enumerate(q)}
    return sum(pos[p[i]] > pos[p[j]]
               for i in range(len(p)) for j in range(i+1,len(p)))


def distances(edges, src):
    distances = [-1] * len(edges)
    distances[src] = 0
    queue = deque([src])
    while queue:
        x = queue.popleft()
        for y in edges[x]:
            if distances[y] == -1:
                distances[y] = distances[x] + 1
                queue.append(y)
    assert all(d >= 0 for d in distances), "Graph disconnected"
    return distances


def main():
    for n in range(1, 8):
        vertices, edges = graph(n)
        histogram = Counter()
        for i, p in enumerate(vertices):
            d = distances(edges, i)
            for j in range(i + 1, len(vertices)):
                k = kendall(p, vertices[j])
                assert d[j] >= k and (d[j]-k) % 2 == 0
                histogram[(k,d[j])] += 1
        bad = {pair:num for pair,num in histogram.items() if pair[0]!=pair[1]}
        print('n=%d vertices=%d edges=%d discordant_pairs=%d distance_profiles=%s' % (
            n,len(vertices),sum(map(len,edges))//2,sum(bad.values()),sorted(bad.items())))
        if n < 7:
            assert not bad
        else:
            assert len(vertices)==220
            assert sum(bad.values())==20
            assert bad=={(4,6):4,(5,7):6,(6,8):4,(7,9):3,(8,10):2,(9,11):1}
    P=(6,4,3,7,2,5,1)
    Q=(6,4,2,5,3,7,1)
    path=[(6,4,3,7,2,5,1),(6,4,7,3,2,5,1),(6,4,7,2,3,5,1),
          (6,4,2,7,3,5,1),(6,4,2,7,5,3,1),(6,4,2,5,7,3,1),
          (6,4,2,5,3,7,1)]
    assert path[0]==P and path[-1]==Q and all(admissible(p) for p in path)
    assert all(kendall(u,v)==1 for u,v in zip(path,path[1:]))
    assert kendall(P,Q)==4 and not admissible((6,4,3,2,7,5,1))
    for n in range(7,13):
        prefix=tuple(range(n,7,-1))
        lifted=[prefix + p for p in path]
        assert all(admissible(p) for p in lifted)
        assert all(kendall(u,v)==1 for u,v in zip(lifted,lifted[1:]))
        assert kendall(lifted[0],lifted[-1])==4
    print('explicit_seven_step_path=PASS, unique_first_geodesic_move_blocked=PASS, lifts_n=7..12=PASS')
if __name__ == '__main__':
    main()
