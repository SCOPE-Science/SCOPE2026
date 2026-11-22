"""Finite checks for the scale-two Rips complex of an edge-spined hexagon book.
Uses only the Python standard library; independent of the all-parameter proof.
"""
from collections import deque
from itertools import combinations


def graph(h):
    v = ['a', 'b'] + [f'x{i}_{j}' for i in range(h) for j in range(1, 5)]
    adj = {x: set() for x in v}
    def edge(a, b):
        adj[a].add(b)
        adj[b].add(a)
    edge('a', 'b')
    for i in range(h):
        arm = ['a'] + [f'x{i}_{j}' for j in range(1, 5)] + ['b']
        for a, b in zip(arm, arm[1:]):
            edge(a, b)
    return v, adj


def distances(v, adj):
    result = {}
    for x in v:
        dist = {x: 0}
        queue = deque([x])
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if b not in dist:
                    dist[b] = dist[a] + 1
                    queue.append(b)
        assert len(dist) == len(v)
        result[x] = dist
    return result


def cliques(v, dist):
    n = len(v)
    neigh = {i: {j for j in range(i+1, n) if dist[v[i]][v[j]] <= 2} for i in range(n)}
    faces = set()
    def visit(prefix, candidates):
        for index, i in enumerate(candidates):
            face = prefix + (i,)
            faces.add(face)
            visit(face, [j for j in candidates[index+1:] if j in neigh[i]])
    visit((), list(range(n)))
    return faces


def full_simplex(vertices):
    return {tuple(sorted(t)) for k in range(1, len(vertices)+1)
            for t in combinations(vertices, k)}


def expected_complex(v, h):
    ids = {x: j for j, x in enumerate(v)}
    result = set()
    for i in range(h):
        labels = ['a', 'b'] + [f'x{i}_{j}' for j in range(1, 5)]
        opposite = [frozenset(('a', f'x{i}_3')),
                    frozenset((f'x{i}_1', f'x{i}_4')),
                    frozenset((f'x{i}_2', 'b'))]
        for k in range(1, 7):
            for sample in combinations(labels, k):
                if all(not pair.issubset(sample) for pair in opposite):
                    result.add(tuple(sorted(ids[x] for x in sample)))
    for j in [1, 4]:
        result |= full_simplex([ids[x] for x in ['a','b'] + [f'x{i}_{j}' for i in range(h)]])
    return result


def gf2_rank(columns):
    pivots = {}
    for x in columns:
        while x:
            k = x.bit_length()-1
            if k not in pivots:
                pivots[k] = x
                break
            x ^= pivots[k]
    return len(pivots)


def mod2_betti(faces):
    by_dim = {}
    for f in faces:
        by_dim.setdefault(len(f)-1, []).append(f)
    for d in by_dim:
        by_dim[d].sort()
    ranks = {0: 1}  # augmented boundary of the nonempty vertex set
    for d in range(1, max(by_dim)+1):
        index = {f: j for j, f in enumerate(by_dim[d-1])}
        cols = [sum(1 << index[f[:j]+f[j+1:]] for j in range(len(f)))
                for f in by_dim[d]]
        ranks[d] = gf2_rank(cols)
    return {d: len(by_dim[d])-ranks.get(d, 0)-ranks.get(d+1, 0)
            for d in sorted(by_dim)}


def trace_on_reduced_chains(faces, v, map_vertex):
    index = {x: j for j, x in enumerate(v)}
    permutation = [index[map_vertex(x)] for x in v]
    result = -1  # reduced degree-minus-one term
    for f in faces:
        image = [permutation[j] for j in f]
        if set(image) == set(f):
            inv = sum(image[i] > image[j] for i in range(len(image))
                      for j in range(i+1, len(image)))
            result += (-1)**(len(f)-1+inv)
    return result


def reversal(x):
    if x == 'a':
        return 'b'
    if x == 'b':
        return 'a'
    a, b = x[1:].split('_')
    return f'x{a}_{5-int(b)}'


def swap_arms(x):
    if x in {'a','b'}:
        return x
    a, b = x[1:].split('_')
    return f'x{1-int(a)}_{b}' if int(a)<2 else x


def main():
    for h in range(2, 7):
        v, edges = graph(h)
        dist = distances(v, edges)
        faces = cliques(v, dist)
        expected = expected_complex(v, h)
        assert faces == expected, (h, sorted(faces^expected)[:10])
        b = mod2_betti(faces)
        assert {d:k for d,k in b.items() if k} == {2:h}, (h, b)
        t_pole = trace_on_reduced_chains(faces, v, reversal)
        t_swap = trace_on_reduced_chains(faces, v, swap_arms)
        assert (t_pole,t_swap) == (h,h-2), (h,t_pole,t_swap)
        count = [sum(len(f)==k+1 for f in faces) for k in range(max(b)+1)]
        print(f'h={h} vertices={len(v)} face_vector={count} mod2_H2={h} pole_trace={t_pole} arm_transposition_trace={t_swap} VERIFIED')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
