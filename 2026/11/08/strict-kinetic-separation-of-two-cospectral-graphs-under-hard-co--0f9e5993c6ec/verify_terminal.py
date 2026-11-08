"""Exact terminal random-priority adsorption distributions on two 16-site graphs.

Run with Python 3 standard library: python3 verify_terminal.py
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache

N = 16
VERTICES = [(a, b) for a in range(4) for b in range(4)]

def closed_neighborhoods(model):
    neighborhoods = []
    for i, (a, b) in enumerate(VERTICES):
        mask = 1 << i
        for j, (c, d) in enumerate(VERTICES):
            if i == j:
                continue
            if model == 'rook':
                adjacent = a == c or b == d
            elif model == 'shrikhande':
                adjacent = ((c-a) % 4, (d-b) % 4) in {
                    (1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
            else:
                raise ValueError(model)
            if adjacent:
                mask |= 1 << j
        neighborhoods.append(mask)
    assert all(mask.bit_count() == 7 for mask in neighborhoods)
    for u in range(N):
        for v in range(u+1, N):
            common = (neighborhoods[u] & neighborhoods[v]) & ~((1<<u)|(1<<v))
            assert common.bit_count() == 2
    return neighborhoods

def terminal_distribution(model):
    closed = closed_neighborhoods(model)

    @lru_cache(None)
    def distribution(free):
        # First *accepted* vertex is uniformly random among free vertices;
        # rejected earlier arrivals do not affect the remaining free order.
        if free == 0:
            return {0: Fraction(1)}
        outcome = defaultdict(Fraction)
        vertices = free.bit_count()
        remaining = free
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            v = bit.bit_length() - 1
            for tail, probability in distribution(free & ~closed[v]).items():
                outcome[tail | bit] += probability / vertices
        return dict(outcome)

    final = distribution((1 << N) - 1)
    assert sum(final.values()) == 1
    assert all(all(not ((closed[v] & terminal) ^ (1 << v))
                   for v in range(N) if (terminal >> v) & 1)
               for terminal in final)
    for occupied_set in final:
        assert all((closed[v] & occupied_set) for v in range(N)), 'not maximal'
    return final, closed

def inspect_residuals(closed):
    first = 0
    available = ((1 << N) - 1) & ~closed[first]
    shapes = Counter()
    for second in range(N):
        if not (available >> second) & 1:
            continue
        remaining = available & ~closed[second]
        degrees = sorted((closed[v] & remaining).bit_count() - 1
                         for v in range(N) if (remaining >> v) & 1)
        assert remaining.bit_count() == 4
        if degrees == [2, 2, 2, 2]:
            shapes['C4'] += 1
        elif degrees == [2, 2, 3, 3]:
            shapes['K4_minus_edge'] += 1
        else:
            raise AssertionError((second, degrees))
    return dict(shapes)

if __name__ == '__main__':
    rook, r_neighborhoods = terminal_distribution('rook')
    shr, s_neighborhoods = terminal_distribution('shrikhande')
    assert inspect_residuals(r_neighborhoods) == {'C4': 9}
    assert inspect_residuals(s_neighborhoods) == {'C4': 3, 'K4_minus_edge': 6}
    assert len(rook) == 24
    assert all(k.bit_count() == 4 and p == Fraction(1, 24)
               for k, p in rook.items())
    assert len(shr) == 48
    assert Counter((k.bit_count(), p) for k, p in shr.items()) == {
        (3, Fraction(1, 96)): 32, (4, Fraction(1, 24)): 16}
    mean_rook = sum(Fraction(k.bit_count()) * p for k, p in rook.items())
    mean_shr = sum(Fraction(k.bit_count()) * p for k, p in shr.items())
    assert mean_rook == 4 and mean_shr == Fraction(11, 3)
    print('Rook terminal 24 sets, each size 4, probability 1/24; mean 4')
    print('Shrikhande terminal 32 triples at 1/96 and 16 quadruples at 1/24; mean 11/3')
    print('SHRIKHANDE_ROOK_TERMINAL_OK')
