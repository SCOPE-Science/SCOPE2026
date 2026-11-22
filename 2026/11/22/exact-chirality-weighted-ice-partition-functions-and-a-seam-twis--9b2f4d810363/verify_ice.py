#!/usr/bin/env python3
"""Independent finite ice-state enumeration and all-order polynomial identities.
All arithmetic is exact Python integers; no external packages are needed.
"""
from collections import Counter


def add(a, b):
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) for i in range(max(len(a), len(b)))]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def scale(a, s):
    return [s*x for x in a]


def power(a, n):
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def formula(n, twist):
    # Trace of the two roots of u^2-(4z^2+1)u+4z^2-2.
    a, b = [2], [1, 0, 4]
    for _ in range(2, n+1):
        a, b = b, add(mul([1, 0, 4], b), scale(mul([-2, 0, 4], a), -1))
    common = b
    result = add(common, scale(power([1, 2], n), 2))
    result = add(result, scale(power([-1, 2], n), -2 if twist else 2))
    result = add(result, [1 if twist else 3])
    return result


def base_edges(n, twist):
    def v(layer, i): return layer*n+i
    edges = [(v(0, i), v(1, i)) for i in range(n)]
    for layer in range(2):
        edges.extend((v(layer, i), v(layer, i+1)) for i in range(n-1))
    if twist:
        edges.extend([(v(0, n-1), v(1, 0)), (v(1, n-1), v(0, 0))])
    else:
        edges.extend([(v(0, n-1), v(0, 0)), (v(1, n-1), v(1, 0))])
    assert len(set(tuple(sorted(e)) for e in edges)) == 3*n
    return edges


def brute_histogram(n, twist):
    original = base_edges(n, twist)
    vertices = [tuple(i for i, e in enumerate(original) if v in e) for v in range(2*n)]
    assert all(len(edges) == 3 for edges in vertices)
    line_edges = []
    for v, inc in enumerate(vertices):
        for i in range(3):
            for j in range(i+1, 3):
                line_edges.append((inc[i], inc[j], v))
    assert len(line_edges) == 6*n
    line_edges.sort(key=lambda e: (max(e[:2]), min(e[:2])))
    remaining = [0] * (3*n)
    incoming = [0] * (3*n)
    local_in = [[0]*3 for _ in range(2*n)]
    positions = [{edge: i for i,edge in enumerate(inc)} for inc in vertices]
    for a,b,_ in line_edges:
        remaining[a] += 1
        remaining[b] += 1
    hist = Counter()

    def dfs(k):
        if k == len(line_edges):
            cyclic = sum(all(t == 1 for t in local) for local in local_in)
            hist[cyclic] += 1
            return
        a, b, vertex = line_edges[k]
        remaining[a] -= 1
        remaining[b] -= 1
        if incoming[a] < 2 and incoming[b]+remaining[b] >= 2:
            incoming[a] += 1
            local_in[vertex][positions[vertex][a]] += 1
            dfs(k+1)
            local_in[vertex][positions[vertex][a]] -= 1
            incoming[a] -= 1
        if incoming[b] < 2 and incoming[a]+remaining[a] >= 2:
            incoming[b] += 1
            local_in[vertex][positions[vertex][b]] += 1
            dfs(k+1)
            local_in[vertex][positions[vertex][b]] -= 1
            incoming[b] -= 1
        remaining[a] += 1
        remaining[b] += 1

    dfs(0)
    return hist


def _trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def verify():
    # Direct graph-wise enumeration does not use a transfer matrix.
    for n in range(3, 8):
        for twist in (False, True):
            got = brute_histogram(n, twist)
            predicted = formula(n, twist)
            for k in set(got) | set(range(len(predicted))):
                assert got.get(k, 0) == (predicted[k] if k < len(predicted) else 0), (n, twist, k, got, predicted)
            print('DIRECT_ICE_POLYNOMIAL_OK', n, 'mobius' if twist else 'prism', sum(got.values()))
    # Exact polynomial seam identity for substantially larger sizes.
    for n in range(3, 101):
        a, b = formula(n, False), formula(n, True)
        delta = add(a, scale(b, -1))
        assert tuple(_trim(delta)) == tuple(_trim(add([2], scale(power([-1, 2], n), 4)))), (n, delta)
        assert sum(a) - sum(b) == 6
    print('ICE_SEAM_POLYNOMIAL_IDENTITY_OK n=3..100')


if __name__ == '__main__':
    verify()
