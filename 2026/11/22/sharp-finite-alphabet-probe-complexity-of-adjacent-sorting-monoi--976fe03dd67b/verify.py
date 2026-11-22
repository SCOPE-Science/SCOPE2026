"""Finite checks for the sharp probe theorem for adjacent comparators.
Python 3.11+, standard library only. No finite test substitutes for the proof.
"""
from collections import deque
from itertools import product
from math import factorial, ceil

def check(n, m):
    words = list(product(range(m), repeat=n))
    wi = {w:i for i,w in enumerate(words)}
    length = len(words)
    generators=[]
    for j in range(n-1):
        generators.append(tuple(wi[w[:j] + tuple(sorted(w[j:j+2])) + w[j+2:]] for w in words))
    descending = tuple(range(n-1,-1,-1))
    identity = tuple(range(length))
    seen = {descending: identity}
    todo = deque([descending])
    while todo:
        p=todo.popleft()
        fn=seen[p]
        for j,g in enumerate(generators):
            q = p[:j] + tuple(sorted(p[j:j+2])) + p[j+2:]
            nxt = tuple(g[z] for z in fn)
            if q not in seen:
                seen[q] = nxt
                todo.append(q)
            else:
                assert seen[q] == nxt, '0-Hecke normal-form action mismatch'
    assert len(seen) == factorial(n)
    all_fns = list(seen.values())
    assert len(set(all_fns)) == factorial(n), 'binary action should be faithful'
    groups = [list(range(1,n))[j:j+m-1] for j in range(0,n-1,m-1)]
    probes = [tuple(sum(k >= i for k in group) for i in range(1,n+1)) for group in groups]
    probe_indices = [wi[x] for x in probes]
    fingerprints = {tuple(f[i] for i in probe_indices) for f in all_fns}
    assert len(probes) == ceil((n-1)/(m-1))
    assert len(fingerprints) == factorial(n)
    long = seen[tuple(range(n))]
    for j in range(n-1):
        p = list(range(n))
        p[j],p[j+1] = p[j+1],p[j]
        coatom = seen[tuple(p)]
        assert coatom != long
        assert tuple(generators[j][z] for z in coatom) == long
        distinguished = 0
        for ix,w in enumerate(words):
            if long[ix] != coatom[ix]:
                out = words[long[ix]]
                assert out[j] != out[j+1]
                distinguished += 1
        assert distinguished > 0
    print(f'CHECK_OK n={n} m={m} elements={len(seen)} probes={len(probes)} inputs={length}')

if __name__ == '__main__':
    for n in range(2,7):
        for m in range(2, min(4,n+1)):
            check(n,m)
    print('VERIFY_OK')
