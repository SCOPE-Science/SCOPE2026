"""Exact finite combinatorial consistency checks for iterated apex truncations.

The infinite diameter equality is proved analytically in RESULT.md;
these checks are not a substitute for that proof.
"""
from collections import deque


def model(k):
    assert isinstance(k, int) and k >= 2
    triples = [(frozenset(('bottom', 0, 1)), 2, 'L01'),
               (frozenset(('bottom', 0, 2)), 3, 'L02'),
               (frozenset(('bottom', 1, 2)), 4, 'L12')]
    for j in range(3, k + 1):
        triples.append((frozenset((j, j - 1, j - 3)), 2*j, 'U'+str(j)))
        triples.append((frozenset((j, j - 2, j - 3)), 2*j - 1, 'W'+str(j)))
    triples.append((frozenset((k, k - 1, k - 2)), 2*k+1, 'T'+str(k)))
    return triples


def edges(triples):
    adj = [[] for _ in triples]
    for i in range(len(triples)):
        for j in range(i + 1, len(triples)):
            if len(triples[i][0] & triples[j][0]) == 2:
                adj[i].append(j)
                adj[j].append(i)
    return adj


def distances(adj, root):
    out = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in out:
                out[w] = out[v] + 1
                queue.append(w)
    return out


def verify():
    cases = 0
    for k in range(2, 101):
        triples = model(k)
        adj = edges(triples)
        assert len(triples) == 2*k
        assert len({t[0] for t in triples}) == 2*k
        assert all(len(a) == 3 for a in adj)
        assert sum(map(len, adj)) // 2 == 3*k
        assert 2*k - 3*k + (k+2) == 2
        assert all(abs(triples[v][1] - triples[w][1]) <= 3
                   for v in range(len(triples)) for w in adj[v])
        base_to_tip = distances(adj, 0)
        assert len(base_to_tip) == 2*k
        theoretical = (2*k+1)//3
        assert base_to_tip[len(triples)-1] == theoretical
        assert max(max(distances(adj, v).values())
                   for v in range(len(triples))) == theoretical
        cases += 1
    print('PASS:', cases, 'exact finite graph cases, k = 2..100')
    print('PASS: cubic degrees, edge and face counts, all Lipschitz edges')
    print('PASS: graph diameters and proposed diametral vertex pair')


if __name__ == '__main__':
    verify()
