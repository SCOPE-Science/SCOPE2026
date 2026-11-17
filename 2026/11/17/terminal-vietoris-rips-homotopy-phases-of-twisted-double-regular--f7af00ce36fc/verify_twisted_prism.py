"""Finite, reproducible checks for the terminal Rips phase diagram of twisted regular double polygons.
Run with Python 3 standard library: python verify_twisted_prism.py
Numerical tests are not a substitute for the proof valid for arbitrary real parameters.
"""
import math
from collections import defaultdict


def distance_graph(n, twist, height, radius=1.0):
    pts = []
    for layer in (0, 1):
        for j in range(n):
            a = 2.0 * math.pi * (j + layer * twist) / n
            pts.append((radius * math.cos(a), radius * math.sin(a), layer * height))
    d2 = {}
    for i in range(2 * n):
        for j in range(i + 1, 2 * n):
            d2[i, j] = sum((pts[i][k] - pts[j][k]) ** 2 for k in range(3))
    maximum = max(d2.values())
    edges = frozenset(e for e, d in d2.items() if abs(d - maximum) <= 1e-8 * max(1, maximum))
    return edges, maximum


def predicted_graph(n, twist, height, radius=1.0):
    def edge(i, j):
        return tuple(sorted((i, j)))
    cross = set()
    if n % 2:
        steps = ((n - 1) // 2, (n + 1) // 2) if twist == 0 else ((n - 1) // 2,)
    else:
        steps = (n // 2, n // 2 - 1) if twist == 0.5 else (n // 2,)
    for j in range(n):
        for off in steps:
            cross.add(edge(j, n + (j + off) % n))
    if n % 2:
        return frozenset(cross), 'cycle' if twist == 0 else 'matching'
    within = {edge(s * n + j, s * n + (j + n // 2) % n)
              for s in (0, 1) for j in range(n)}
    a = 4 * radius ** 2
    b = 4 * radius ** 2 * math.cos(math.pi * twist / n) ** 2 + height ** 2
    if abs(a-b) <= 1e-8 * max(1, a, b):
        return frozenset(within | cross), 'mobius' if twist == 0.5 else 'squares'
    if a > b:
        return frozenset(within), 'matching'
    return frozenset(cross), 'cycle' if twist == 0.5 else 'matching'


def components(edges, n):
    nb = [set() for _ in range(2 * n)]
    for i, j in edges:
        nb[i].add(j)
        nb[j].add(i)
    seen = set()
    lengths = []
    for i in range(2 * n):
        if i in seen:
            continue
        todo = [i]
        seen.add(i)
        size = 0
        while todo:
            v = todo.pop()
            size += 1
            for w in nb[v] - seen:
                seen.add(w)
                todo.append(w)
        lengths.append(size)
    return sorted(lengths), sorted(set(map(len, nb)))


def expected_homology(n, kind):
    if kind == 'matching':
        return {n - 1: 1}
    if kind == 'squares':
        return {n // 2 - 1: 1}
    if kind == 'mobius':
        assert n % 2 == 0
        return {n // 2 - 1: 1 if n % 4 == 0 else 3}
    m = 2 * n
    if m % 3 == 0:
        return {m // 3 - 1: 2}
    if m % 3 == 1:
        return {(m - 4) // 3: 1}
    return {(m - 2) // 3: 1}


def gf2_rank(columns):
    basis = {}
    for value in columns:
        while value:
            top = value.bit_length() - 1
            if top in basis:
                value ^= basis[top]
            else:
                basis[top] = value
                break
    return len(basis)


def reduced_homology(edges, n):
    # Directly enumerate every independent set. The empty face gives an augmented degree -1 chain.
    nb = [0] * (2*n)
    for i,j in edges:
        nb[i] |= 1 << j
        nb[j] |= 1 << i
    faces = defaultdict(list)
    faces[-1] = [0]
    for mask in range(1, 1 << (2*n)):
        good = True
        for i in range(2*n):
            if mask >> i & 1 and (mask & nb[i]):
                good = False
                break
        if good:
            faces[mask.bit_count() - 1].append(mask)
    maxd = max(faces)
    ranks = {}
    for k in range(0, maxd+1):
        lower = {face: i for i,face in enumerate(faces[k-1])}
        cols = []
        for face in faces[k]:
            x = face
            col = 0
            while x:
                b = x & -x
                col |= 1 << lower[face ^ b]
                x ^= b
            cols.append(col)
        ranks[k] = gf2_rank(cols)
    output = {}
    for k in range(0, maxd+1):
        b = len(faces[k]) - ranks.get(k, 0) - ranks.get(k+1,0)
        if b:
            output[k] = b
    return output


def run():
    tested = 0
    observed = set()
    for n in range(3,31):
        for twist in (0.0, 0.03, 0.13, 0.35, 0.499, 0.5):
            height_critical = 2 * math.sin(math.pi * twist/n)
            for height in (0.13, 0.83, 2.15, height_critical if height_critical > 0 else 0.11):
                observed_edges, diameter2 = distance_graph(n, twist, height)
                theoretical_edges, kind = predicted_graph(n, twist, height)
                assert observed_edges == theoretical_edges, (n, twist, height)
                sizes,degrees = components(observed_edges,n)
                if kind == 'matching':
                    assert sizes == [2]*n and degrees == [1]
                elif kind == 'squares':
                    assert sizes == [4]*(n//2) and degrees == [2]
                elif kind == 'cycle':
                    assert sizes == [2*n] and degrees == [2]
                else:
                    assert sizes == [2*n] and degrees == [3]
                observed.add(kind)
                tested += 1
    print('DIAMETER_GRAPH_OK', tested, 'parameter cases; types',','.join(sorted(observed)))
    checked_betti = 0
    for n in range(3,9):
        for twist in (0.0,0.2,0.5):
            hcrit = 2 * math.sin(math.pi * twist / n)
            for height in (0.1,1.0,hcrit if hcrit else 0.2):
                ed, kind = predicted_graph(n,twist,height)
                observed_betti = reduced_homology(ed,n)
                predicted_betti = expected_homology(n,kind)
                assert observed_betti == predicted_betti, (n,twist,height,kind,observed_betti,predicted_betti)
                checked_betti += 1
    print('MOD2_BETTI_OK',checked_betti,'parameter cases, n=3..8')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
