#!/usr/bin/env python3
"""Exact finite-state certificate for locating-total domination of circular ladders.

Run with Python 3; uses only the standard library. All computations are integer exact.
"""
from itertools import combinations

N = 256
INF = 10**8

def bit(mask, layer):
    return (mask >> layer) & 1


def signature(c, position, layer):
    """Labels of selected neighbors in a five-column window."""
    candidates = ((position-1, layer), (position+1, layer),
                  (position, 1-layer))
    return frozenset((p, r) for p, r in candidates if bit(c[p], r))


def allowed_window(c):
    """Check total domination at column 1, and its locating pairs forward."""
    for layer in (0, 1):
        u = (1, layer)
        u_sig = signature(c, *u)
        if not u_sig:
            return False
        if bit(c[1], layer):
            continue
        for p in (1, 2, 3):
            for r in (0, 1):
                if p == 1 and r <= layer:
                    continue
                if not bit(c[p], r) and u_sig == signature(c, p, r):
                    return False
    return True


def graph_edges():
    edges = [[] for _ in range(N)]
    for u in range(N):
        c = tuple((u >> (2*k)) & 3 for k in (3, 2, 1, 0))
        for e in range(4):
            if allowed_window(c + (e,)):
                v = ((u << 2) & 255) | e
                edges[u].append((v, e.bit_count()))
    return edges


def matstep(M, edges):
    result = [[INF] * N for _ in range(N)]
    for u in range(N):
        for v, weight in edges[u]:
            for row in range(N):
                val = M[row][u] + weight
                if val < result[row][v]:
                    result[row][v] = val
    return result


def transfer_certificate():
    edges = graph_edges()
    assert sum(len(e) for e in edges) == 729
    M = [[0 if i==j else INF for j in range(N)] for i in range(N)]
    matrices = {}
    answers = {}
    for n in range(1,19):
        M = matstep(M, edges)
        if 5 <= n <= 17:
            answers[n] = min(M[i][i] for i in range(N))
        if n in (8,18):
            matrices[n] = M
    expected = {5:4,6:6,7:6,8:7,9:8,10:8,11:9,12:10,
                13:11,14:12,15:12,16:14,17:14}
    assert answers == expected, (answers, expected)
    A, B = matrices[8], matrices[18]
    finite = 0
    for i in range(N):
        for j in range(N):
            a, b = A[i][j], B[i][j]
            assert (a == INF) == (b == INF), (i, j, a, b)
            if a < INF:
                finite += 1
                assert b == a + 8, (i, j, a, b)
    assert finite == 41728, finite
    print('TROPICAL_CERTIFICATE_OK; states=256; edges=729; finite_entries=41728')
    print('BASE_VALUES_OK', sorted(answers.items()))


def ltd_brute(n, chosen):
    """Independent whole-graph predicate (no local windows or state matrix)."""
    sigs=[]
    for i in range(n):
        for r in range(2):
            v=2*i+r
            neighbors=(2*((i-1)%n)+r,2*((i+1)%n)+r,2*i+1-r)
            sig=frozenset(x for x in neighbors if x in chosen)
            if not sig:
                return False
            if v not in chosen:
                sigs.append(sig)
    return len(sigs)==len(set(sigs))


def brute_small():
    expected={3:(3,14),4:(4,30),5:(4,5),6:(6,172),7:(6,35),8:(7,80)}
    for n,(k_expected,c_expected) in expected.items():
        for k in range(2*n+1):
            count=sum(ltd_brute(n,set(selected)) for selected in combinations(range(2*n),k))
            if count:
                assert (k,count)==(k_expected,c_expected), (n,k,count)
                break
        else:
            raise AssertionError(n)
    print('INDEPENDENT_BRUTE_OK', expected)


def witness_spotcheck():
    # Symbols encode selected row bits (row 0 is the low bit).
    for word, expected in [('30130030', 7),
                           ('30222030110', 9),
                           ('3003030030330030', 14)]:
        selected = {2*i+r for i, symbol in enumerate(word)
                    for r in (0, 1) if (int(symbol) >> r) & 1}
        assert len(selected) == expected
        assert ltd_brute(len(word), selected)
    print('WITNESS_OK')


if __name__ == '__main__':
    transfer_certificate()
    brute_small()
    witness_spotcheck()
    print('VERIFY_OK')
