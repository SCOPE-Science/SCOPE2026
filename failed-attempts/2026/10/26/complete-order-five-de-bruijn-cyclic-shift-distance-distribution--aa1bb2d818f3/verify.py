#!/usr/bin/env python3
"""Reproduce the exact minimum cyclic shift-distance census at de Bruijn order five.

Run: python3 verify.py
Python standard library only. No external datasets or packages are required.
"""
from collections import Counter
import csv
from pathlib import Path

ORDER = 5
N = 1 << ORDER
EXPECTED = {8: 36, 10: 114, 12: 1212, 14: 682, 16: 4}
ALL_BITS = (1 << N) - 1


def canonical(word):
    assert len(word) == N and set(word) <= set('01')
    double = word + word
    positions = [i for i in range(N) if double[i:i + ORDER] == '0' * ORDER]
    assert len(positions) == 1, ('not a unique zero window', word)
    i = positions[0]
    return word[i:] + word[:i]


def valid_cycle(word):
    if len(word) != N or set(word) - set('01'):
        return False
    return len({(word + word[:ORDER - 1])[i:i + ORDER] for i in range(N)}) == N


def cycles_dfs():
    """Every cycle starts at its unique all-zero order-five window.

    Enumerate both successors at every extension, rejecting repeated length-5
    windows. The last four cyclic windows are checked on closure. Thus this
    exhaustive backtracking visits every de Bruijn cycle exactly once.
    """
    found = []

    def visit(word, used):
        if len(word) == N:
            closed = word + word[:ORDER - 1]
            new_used = used
            for pos in range(N - ORDER + 1, N):
                v = int(closed[pos:pos + ORDER], 2)
                if (new_used >> v) & 1:
                    return
                new_used |= 1 << v
            if new_used == ALL_BITS:
                assert valid_cycle(word)
                found.append(word)
            return
        for bit in '01':
            v = int(word[-(ORDER - 1):] + bit, 2)
            if not (used >> v) & 1:
                visit(word + bit, used | (1 << v))

    visit('0' * ORDER, 1)
    assert len(found) == len(set(found))
    return sorted(found)


def cycles_euler():
    """Independent Euler-tour generator on the sixteen order-four vertices.

    Each local vertex has two directed outgoing arcs, represented by five-bit
    words. Every Euler tour arises from at least one local ordering of its two
    arcs; 2^16 orderings are tested. Repeated canonical cycles are deduplicated.
    """
    seen = set()
    for mask in range(1 << (1 << (ORDER - 1))):
        next_edge = [0] * (1 << (ORDER - 1))
        reverse_output = []

        def tour(vertex):
            while next_edge[vertex] < 2:
                rank = next_edge[vertex]
                next_edge[vertex] += 1
                bit = ((mask >> vertex) & 1) ^ rank
                tour(((vertex << 1) | bit) & 15)
                reverse_output.append(str(bit))

        tour(0)
        if len(reverse_output) != N:
            continue
        cycle = canonical(''.join(reversed(reverse_output)))
        assert valid_cycle(cycle)
        seen.add(cycle)
    return sorted(seen)


def distances_direct(word):
    return tuple(sum(word[i] != word[(i + shift) % N] for i in range(N))
                 for shift in range(1, N))


def distances_bits(word):
    v = int(word, 2)
    result = []
    for shift in range(1, N):
        shifted = ((v << shift) | (v >> (N - shift))) & ALL_BITS
        result.append((v ^ shifted).bit_count())
    return tuple(result)


def main():
    dfs = cycles_dfs()
    euler = cycles_euler()
    assert dfs == euler
    assert len(dfs) == 2048  # de Bruijn/Flye Sainte-Marie count at order five
    hist = Counter()
    best = []
    rows = []
    for word in dfs:
        d = distances_direct(word)
        assert d == distances_bits(word)
        assert all(d[s - 1] == 16 for s in range(1, 5))
        assert all(d[s - 1] == d[N - s - 1] for s in range(1, N))
        minimum = min(d)
        hist[minimum] += 1
        if minimum == 16:
            best.append(word)
            assert d.count(16) == 26
            assert d.count(18) == 2
            assert d.count(20) == 3
            assert all(d[s - 1] == 18 for s in (5, 27))
            assert all(d[s - 1] == 20 for s in (14, 16, 18))
        rows.append((word, minimum, ','.join(map(str, d))))

    assert dict(hist) == EXPECTED, dict(hist)
    assert len(best) == 4
    assert sum(hist.values()) == 2048
    assert {canonical(w.translate(str.maketrans('01', '10'))) for w in best} == set(best)
    assert {canonical(w[::-1]) for w in best} == set(best)
    orbit = set()
    z = best[0]
    for w in (z, z[::-1], z.translate(str.maketrans('01', '10')),
              z[::-1].translate(str.maketrans('01', '10'))):
        orbit.add(canonical(w))
    assert orbit == set(best)
    path = Path(__file__).resolve().parent / 'certificate.csv'
    if path.is_file():
        with path.open(newline='', encoding='utf-8') as stream:
            reader = csv.reader(stream)
            assert next(reader) == ['cycle', 'minimum_shift_distance', 'shift_distances_1_to_31']
            assert list(reader) == [list(map(str, r)) for r in rows]
    print('CYCLES=2048')
    print('HISTOGRAM=' + repr(dict(sorted(hist.items()))))
    print('OPTIMAL_CYCLES=' + repr(best))
    print('CERTIFICATE=' + ('MATCH' if path.is_file() else 'ABSENT'))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
