"""Exact finite verification of one-deletion coding in the 132-avoiding permutations.

Requires only Python 3.9 or later and the sibling LP_CERTIFICATE.json.
The branch-and-bound algorithm implements the elementary proper-coloring
upper bound for clique size; no numerical optimizer is used.
"""
import itertools
import json
from collections import defaultdict
from pathlib import Path


def avoids_132(p):
    return all(not (p[i] < p[k] < p[j])
               for i in range(len(p))
               for j in range(i + 1, len(p))
               for k in range(j + 1, len(p)))


def catalan_perms(n):
    if n == 0:
        return [()]
    res = []
    for a in range(n):
        b = n - 1 - a
        for u in catalan_perms(a):
            for v in catalan_perms(b):
                res.append(tuple(t + b for t in u) + (n - 1,) + v)
    return sorted(res)


def std(p):
    ordering = {v: i for i, v in enumerate(sorted(p))}
    return tuple(ordering[v] for v in p)


def deck(p):
    return frozenset(std(p[:i] + p[i + 1:]) for i in range(len(p)))


def make_graph(perms):
    decks = [deck(p) for p in perms]
    incidence = defaultdict(list)
    for i, outcomes in enumerate(decks):
        for s in outcomes:
            incidence[s].append(i)
    n = len(perms)
    forbidden = [0] * n
    for entries in incidence.values():
        for i, j in itertools.combinations(entries, 2):
            forbidden[i] |= 1 << j
            forbidden[j] |= 1 << i
    full = (1 << n) - 1
    compatible = [full ^ (1 << i) ^ forbidden[i] for i in range(n)]
    return decks, incidence, compatible


def maximum_clique(compatible):
    """Full exact search. Every color class is independent, hence its count
    bounds the size of a clique in a remaining induced subgraph."""
    N = len(compatible)
    best = [0, 0]
    nodes = [0]

    def color_order(P):
        vertices, color_bounds = [], []
        remaining = P
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                vertices.append(v)
                color_bounds.append(color)
                remaining ^= bit
                available ^= bit
                available &= ~compatible[v]
        return vertices, color_bounds

    def search(P, size, chosen):
        nodes[0] += 1
        if not P:
            if size > best[0]:
                best[0], best[1] = size, chosen
            return
        vertices, bounds = color_order(P)
        for i in range(len(vertices) - 1, -1, -1):
            if size + bounds[i] <= best[0]:
                return
            v = vertices[i]
            bit = 1 << v
            search(P & compatible[v], size + 1, chosen | bit)
            P ^= bit

    search((1 << N) - 1, 0, 0)
    return best[0], best[1], nodes[0]


def perm_string(p):
    return ''.join(str(i) for i in p)


def check_lp(n, perms, decks, incidence, cert, best):
    outcomes = sorted(incidence)
    if n <= 5:
        selected = set(cert['cover_outputs'])
        assert len(selected) == best
        assert selected <= {perm_string(o) for o in outcomes}
        for d in decks:
            assert any(perm_string(s) in selected for s in d)
        return (best, best, 1)
    assert n == 6
    den = cert['denominator']
    assert den == 308
    ps = [cert['source_weights'].get(perm_string(p), 0) for p in perms]
    os = [cert['output_cover_weights'].get(perm_string(o), 0) for o in outcomes]
    assert all(isinstance(x, int) and x >= 0 for x in ps + os)
    assert sum(ps) == sum(os) == 4434
    for o in outcomes:
        assert sum(ps[i] for i in incidence[o]) <= den
    assert all(sum(os[i] for i, o in enumerate(outcomes) if o in d) >= den for d in decks)
    assert cert['scaled_totals'] == {'source': 4434, 'cover': 4434}
    # The two rational certificates prove LP opt = 4434/308 = 2217/154.
    return (best, 4434, den)


def main():
    certificates = json.loads((Path(__file__).parent / 'LP_CERTIFICATE.json').read_text('utf-8'))
    sizes = [1, 1, 2, 3, 6, 13]
    catalan = [1, 2, 5, 14, 42, 132]
    for n in range(1, 7):
        perms = catalan_perms(n)
        independent_generation = [p for p in itertools.permutations(range(n)) if avoids_132(p)]
        assert perms == independent_generation
        assert len(perms) == catalan[n - 1]
        decks, incidence, compatible = make_graph(perms)
        assert len(incidence) == (1 if n == 1 else catalan[n - 2])
        maximum, choice_mask, nodes = maximum_clique(compatible)
        assert maximum == sizes[n - 1]
        chosen = [i for i in range(len(perms)) if choice_mask >> i & 1]
        assert len(chosen) == maximum
        for i, j in itertools.combinations(chosen, 2):
            assert decks[i].isdisjoint(decks[j])
        lp = check_lp(n, perms, decks, incidence, certificates[str(n)], maximum)
        print('n=%d sources=%d outputs=%d capacity=%d nodes=%d LP=%d/%d' %
              (n, len(perms), len(incidence), maximum, nodes, lp[1], lp[2]))
    claimed = ['012345','234501','312045','324150','340125','345210',
               '431025','452301','510234','523104','531240','543012','543210']
    words = catalan_perms(6)
    claimed_decks = [deck(tuple(int(x) for x in w)) for w in claimed]
    assert len(set(claimed)) == 13
    assert all(tuple(int(x) for x in w) in words for w in claimed)
    assert all(a.isdisjoint(b) for a,b in itertools.combinations(claimed_decks,2))
    print('CODEBOOK_OK 13')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
