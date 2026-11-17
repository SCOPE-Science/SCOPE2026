#!/usr/bin/env python3
"""Exhaustive verification of six-word deletion covers over four symbols.

Only Python's standard library is required. A second, independently structured
lexicographic six-subset enumerator is provided in enumerate.cpp.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
WORDS = tuple(product(range(4), repeat=3))
INDEX = {w: i for i, w in enumerate(WORDS)}
SHADOW = tuple(sum(1 << (4*x+y) for x,y in {(a,b), (a,c), (b,c)})
               for a,b,c in WORDS)
SUPPORT = tuple(tuple(i for i,s in enumerate(SHADOW) if s & (1 << j))
                for j in range(16))


def list_optimal_covers():
    """Every six-set cover is reached by branching on an uncovered ordered pair.

    At depth d, disallow branches for which the remaining 6-d words, covering
    at most three pairs each, cannot possibly cover the uncovered pairs.
    """
    result = set()
    visited = set()

    def visit(chosen, covered):
        if chosen in visited:
            return
        visited.add(chosen)
        depth = len(chosen)
        if covered == 65535:
            if depth == 6:
                result.add(chosen)
            return
        if depth == 6 or 16-covered.bit_count() > 3*(6-depth):
            return
        missing = [j for j in range(16) if not covered & (1 << j)]
        next_pair = min(missing, key=lambda j: sum(i not in chosen for i in SUPPORT[j]))
        for i in SUPPORT[next_pair]:
            if i not in chosen:
                visit(tuple(sorted((*chosen, i))), covered | SHADOW[i])

    visit((), 0)
    return result


def excess(code):
    return sum(SHADOW[i].bit_count() for i in code)-16


def generate_catalog():
    covers = list_optimal_covers()
    assert len(covers) == 644
    transformations = []
    for p in permutations(range(4)):
        for reversed_word in (False, True):
            transformations.append(tuple(INDEX[tuple(p[x] for x in
                              (w[::-1] if reversed_word else w))] for w in WORDS))

    def canonical(code):
        return min(tuple(sorted(t[i] for i in code)) for t in transformations)

    orbit_groups = defaultdict(list)
    for code in covers:
        orbit_groups[canonical(code)].append(code)
    reps = sorted(orbit_groups)
    orbit_index = {rep: j for j,rep in enumerate(reps)}
    assert len(reps) == 21
    assert Counter(len(v) for v in orbit_groups.values()) == {8:1, 12:3, 24:9, 48:8}
    assert Counter(excess(code) for code in covers) == {0:120, 1:336, 2:188}
    assert len([rep for rep in reps if excess(rep) == 0]) == 5
    assert sum(len(orbit_groups[r]) for r in reps if excess(r) == 0) == 120

    fmt = lambda c: ','.join(''.join(map(str,WORDS[i])) for i in c)
    catalog = ['words\torbit_id\texcess']
    for code in sorted(covers):
        catalog.append(f'{fmt(code)}\t{orbit_index[canonical(code)]}\t{excess(code)}')
    orbit_table = ['orbit_id\trepresentative\tsize\texcess\tperfect\tstabilizer_order']
    for j,rep in enumerate(reps):
        size = len(orbit_groups[rep]); e=excess(rep)
        assert 48 % size == 0
        assert all(excess(c)==e for c in orbit_groups[rep])
        orbit_table.append(f'{j}\t{fmt(rep)}\t{size}\t{e}\t{int(e==0)}\t{48//size}')
    return covers, '\n'.join(catalog)+'\n', '\n'.join(orbit_table)+'\n'


def main():
    covers,catalog,orbits=generate_catalog()
    if '--write' in sys.argv:
        (ROOT/'codebooks.tsv').write_text(catalog, encoding='utf-8')
        (ROOT/'orbits.tsv').write_text(orbits, encoding='utf-8')
    else:
        assert (ROOT/'codebooks.tsv').read_bytes() == catalog.encode()
        assert (ROOT/'orbits.tsv').read_bytes() == orbits.encode()
    if '--cpp' in sys.argv:
        pos = sys.argv.index('--cpp')
        lines = Path(sys.argv[pos+1]).read_text(encoding='utf-8').splitlines()
        expected = [','.join(''.join(map(str,WORDS[i])) for i in c) for c in sorted(covers)]
        assert lines == expected, 'Lexicographic C++ census differs from pair-branching census'
    print('VERIFY_OK',len(covers),'codebooks',21,'orbits',120,'perfect',flush=True)

if __name__ == '__main__':
    main()
