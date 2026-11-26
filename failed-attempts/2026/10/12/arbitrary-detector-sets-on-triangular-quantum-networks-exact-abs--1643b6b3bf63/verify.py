"""Numerical cross-checks for absorption on J(n,2).
Run: python verify.py (requires NumPy).  Finite checks do not establish
any of the theorems for unbounded n.
"""
import itertools
import math
import random
import numpy as np


def pairs(n):
    return list(itertools.combinations(range(n), 2))


def bipartite_component_count(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    color = [-1] * n
    bipartite = 0
    all_balanced = True
    for root in range(n):
        if color[root] >= 0:
            continue
        color[root] = 0
        stack = [root]
        sizes = [0, 0]
        is_bipartite = True
        while stack:
            a = stack.pop()
            sizes[color[a]] += 1
            for b in adj[a]:
                if color[b] < 0:
                    color[b] = 1 - color[a]
                    stack.append(b)
                elif color[b] == color[a]:
                    is_bipartite = False
        if is_bipartite:
            bipartite += 1
            all_balanced = all_balanced and sizes[0] == sizes[1]
    return bipartite, int(all_balanced)


def predicted_rank(n, detectors):
    if not detectors:
        return 0
    edges = pairs(n)
    remaining = set(edges).difference(detectors)
    b_f, u_f = bipartite_component_count(n, detectors)
    b_g, _ = bipartite_component_count(n, remaining)
    return 1 + n - b_f - u_f + len(detectors) - b_g


def adjacency(n):
    ed = pairs(n)
    a = np.zeros((len(ed), len(ed)), dtype=float)
    for i, x in enumerate(ed):
        for j in range(i + 1, len(ed)):
            if len(set(x).intersection(ed[j])) == 1:
                a[i, j] = a[j, i] = 1.0
    return a


def spectral_rank(a, detectors, ed):
    if not detectors:
        return 0
    w, v = np.linalg.eigh(a)
    mask = [i for i, edge in enumerate(ed) if edge in detectors]
    result = 0
    for eig in np.unique(np.round(w, 8)):
        block = v[:, np.abs(w - eig) < 1.e-7]
        result += np.linalg.matrix_rank(block[mask, :], tol=1.e-8)
    return result


def test_spectral():
    checks = 0
    rng = random.Random(987766)
    for n in range(3, 9):
        ed = pairs(n)
        a = adjacency(n)
        if len(ed) <= 10:
            cases = [set(ed[i] for i in range(len(ed)) if mask & (1 << i))
                     for mask in range(1, 1 << len(ed))]
        else:
            cases = []
            for _ in range(230):
                prob = rng.uniform(0.02, 0.99)
                sample = {edge for edge in ed if rng.random() < prob}
                if sample:
                    cases.append(sample)
        for det in cases:
            predicted = predicted_rank(n, det)
            observed = spectral_rank(a, det, ed)
            assert predicted == observed, (n, det, predicted, observed)
            checks += 1
    return checks


def witnesses(n):
    if n == 3:
        return {(0, 1), (0, 2)}
    if n == 4:
        return {(0, 1), (0, 2), (0, 3)}
    ed = set(pairs(n))
    if n % 2:
        undetected = {tuple(sorted((j, (j + 1) % n))) for j in range(n)}
    else:
        undetected = {tuple(sorted((j, (j + 1) % (n - 1)))) for j in range(n - 1)}
        undetected.add((0, n - 1))
    return ed - undetected


def test_thresholds():
    tests = 0
    for n in range(3, 13):
        es = pairs(n)
        d = witnesses(n)
        expected = (2 if n == 3 else 3 if n == 4 else len(es) - n)
        assert len(d) == expected
        assert predicted_rank(n, d) == len(es)
        tests += 1
    # Exact minimum census on the small sizes, using the separately defined
    # combinatorial formula rather than the constructive bound.
    for n in range(3, 7):
        es = pairs(n)
        minimum = None
        for k in range(1, len(es) + 1):
            if any(predicted_rank(n, set(t)) == len(es)
                   for t in itertools.combinations(es, k)):
                minimum = k
                break
        assert minimum == (2 if n == 3 else 3 if n == 4 else len(es) - n)
        tests += 1
    return tests


def test_loss_spectrum():
    rng = random.Random(640129)
    count = 0
    for n in range(3, 7):
        es = pairs(n)
        a = adjacency(n)
        for _ in range(20):
            p = rng.uniform(.05, 1)
            det = {x for x in es if rng.random() < p}
            if not det:
                det.add(es[0])
            h = a.astype(complex)
            for i, edge in enumerate(es):
                if edge in det:
                    h[i, i] = -0.5j * rng.uniform(.1, 3.)
            eigenvalues = np.linalg.eigvals(h)
            dark = sum(abs(z.imag) < 1.e-7 for z in eigenvalues)
            assert dark == len(es) - predicted_rank(n, det), (n, det, dark)
            assert max(z.imag for z in eigenvalues) < 1.e-7
            count += 1
    return count


if __name__ == '__main__':
    s = test_spectral()
    t = test_thresholds()
    l = test_loss_spectrum()
    print('VERIFY_OK spectral_ranks=%d threshold_checks=%d loss_spectrum=%d' % (s, t, l))
