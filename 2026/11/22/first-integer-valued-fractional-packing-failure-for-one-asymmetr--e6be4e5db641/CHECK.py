"""Finite exact certificates for one-downward-error codes on no-11 words.

Run with Python 3 and CERTIFICATES.json in the same directory.
Uses no third-party modules and no numerical optimizer.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json


def words(n):
    return tuple(''.join(p) for p in product('01', repeat=n)
                 if all(not (p[i] == p[i+1] == '1') for i in range(n-1)))


def down(w):
    yield w
    for i, c in enumerate(w):
        if c == '1':
            yield w[:i] + '0' + w[i+1:]


def maximal_cliques(vertices, adjacency):
    """Bron--Kerbosch with pivot: emits every inclusion-maximal clique once."""
    found = []
    def search(R, P, X):
        if not P and not X:
            found.append(frozenset(R))
            return
        pivot = max(P | X, key=lambda t: len(P & adjacency[t]))
        for v in sorted(P - adjacency[pivot]):
            search(R | {v}, P & adjacency[v], X & adjacency[v])
            P.remove(v)
            X.add(v)
    search(set(), set(vertices), set())
    return found


def validate():
    certs = json.loads((Path(__file__).parent / 'CERTIFICATES.json').read_text('utf-8'))
    capacities = (1, 1, 2, 3, 4, 6, 8)
    counts = (2, 3, 2, 1, 2, 1, 10)
    sources = (2, 3, 5, 8, 13, 21, 34)
    all_max7 = None
    for n in range(1, 8):
        W = words(n)
        assert len(W) == sources[n-1]
        D = {w: frozenset(down(w)) for w in W}
        assert all(D[w] <= set(W) for w in W)
        neighbors = {w: set() for w in W}
        for j, a in enumerate(W):
            for b in W[j+1:]:
                compatible = not (D[a] & D[b])
                # Distinct-word Z-channel confusability is equivalent
                # to at most one 1-to-0 difference in each direction.
                ab = sum(x == '1' and y == '0' for x, y in zip(a, b))
                ba = sum(x == '0' and y == '1' for x, y in zip(a, b))
                assert compatible == (max(ab, ba) >= 2)
                if compatible:
                    neighbors[a].add(b)
                    neighbors[b].add(a)
        maximal = maximal_cliques(W, neighbors)
        best = max(map(len, maximal))
        optima = [c for c in maximal if len(c) == best]
        assert best == capacities[n-1]
        assert len(optima) == counts[n-1]
        c = certs[str(n)]
        C = c['codebook']
        assert len(C) == best and len(set(C)) == best and set(C) <= set(W)
        assert all(D[x].isdisjoint(D[y]) for i, x in enumerate(C) for y in C[i+1:])
        x = {w: Fraction(value) for w, value in c['fractional_primal'].items()}
        y = {w: Fraction(value) for w, value in c['fractional_dual'].items()}
        assert set(x) <= set(W) and set(y) <= set(W)
        assert all(v >= 0 for v in x.values()) and all(v >= 0 for v in y.values())
        expected_lp = Fraction(9 if n == 7 else best)
        assert sum(x.values()) == expected_lp
        assert sum(y.values()) == expected_lp
        for v in W:
            assert sum(x.get(w, Fraction(0)) for w in W if v in D[w]) <= 1
        for w in W:
            assert sum(y.get(v, Fraction(0)) for v in D[w]) >= 1
        if n == 7:
            all_max7 = optima
        print(f'n={n}: sources={len(W)}, maximum={best}, optima={len(optima)}, LP={expected_lp}')
    core = set.intersection(*map(set, all_max7))
    target_core = {'0010001','0100101','1000100','1001001','1010010','1010101'}
    assert core == target_core
    tails = {tuple(sorted(c-core)) for c in all_max7}
    expected_tails = {
        ('0000000','0001010'), ('0000000','0100010'),
        ('0000000','0101000'), ('0000000','0101010'),
        ('0000010','0101000'), ('0000010','0101010'),
        ('0001000','0100010'), ('0001000','0101010'),
        ('0001010','0100000'), ('0100000','0101010'),
    }
    assert tails == expected_tails
    reversal_fixed = sum({w[::-1] for w in c} == set(c) for c in all_max7)
    assert reversal_fixed == 4
    assert (len(all_max7)+reversal_fixed)//2 == 7
    print('n=7: six-word core; ten listed tails; four reversal-fixed optima; seven reversal classes')
    print('VERIFY_OK')


if __name__ == '__main__':
    validate()
