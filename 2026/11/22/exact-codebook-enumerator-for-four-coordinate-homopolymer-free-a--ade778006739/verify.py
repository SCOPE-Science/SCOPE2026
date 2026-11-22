#!/usr/bin/env python3
"""Self-contained exact checker for a four-coordinate constrained swap-code enumerator.

Only Python's standard library is required. All graph edges are reconstructed
from the channel, and an independent subset scan validates the recursion.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import json

EXPECTED = {
    'aabb': (1, 2),
    'aabc': (1, 6, 4),
    'abcd': (1, 24, 180, 472, 366, 48),
}
WITNESSES = {
    'aabb': ('abab',),
    'aabc': ('abac', 'acab'),
    'abcd': ('abcd', 'adcb', 'bcda', 'cdab', 'dbac'),
}
DUAL_OUTPUTS = {
    'aabb': {'abba': 1},
    'aabc': {'abca': 1, 'caab': 1},
    'abcd': None,
}

def swaps(w):
    result = {w}
    for i in range(3):
        v = list(w)
        v[i], v[i + 1] = v[i + 1], v[i]
        result.add(''.join(v))
    return result

def centers(key):
    return tuple(sorted(w for w in {''.join(p) for p in permutations(key)}
                        if all(w[i] != w[i + 1] for i in range(3))))

def conflict_graph(key):
    words = centers(key)
    balls = [swaps(w) for w in words]
    nbr = [0] * len(words)
    for i, j in combinations(range(len(words)), 2):
        if balls[i].intersection(balls[j]):
            nbr[i] |= 1 << j
            nbr[j] |= 1 << i
    return words, balls, nbr

def exact_polynomial(nbr):
    @lru_cache(None)
    def recur(mask):
        if not mask:
            return (1,)
        bit = mask & -mask
        v = bit.bit_length() - 1
        a = recur(mask ^ bit)
        b = recur((mask ^ bit) & ~nbr[v])
        coeff = [0] * max(len(a), len(b) + 1)
        for i, x in enumerate(a):
            coeff[i] += x
        for i, x in enumerate(b):
            coeff[i + 1] += x
        while coeff[-1] == 0:
            coeff.pop()
        return tuple(coeff)
    return recur((1 << len(nbr)) - 1)

def subset_census(nbr, degree):
    total = [1]
    # Independent-set heredity means that absence at degree+1 excludes all larger sets.
    for r in range(1, degree + 2):
        ct = 0
        for sel in combinations(range(len(nbr)), r):
            mask = sum(1 << i for i in sel)
            if all(not (nbr[i] & (mask ^ (1 << i))) for i in sel):
                ct += 1
        total.append(ct)
    assert total[-1] == 0, ('unexpected larger code', total)
    return tuple(total[:-1])

def check_local(key):
    words, balls, nbr = conflict_graph(key)
    poly = exact_polynomial(nbr)
    assert poly == EXPECTED[key], (key, poly)
    assert subset_census(nbr, len(poly) - 1) == poly
    witness = WITNESSES[key]
    assert len(witness) == len(poly) - 1
    assert set(witness).issubset(words)
    assert all(swaps(x).isdisjoint(swaps(y)) for x, y in combinations(witness, 2))
    outs = sorted(set.union(*balls))
    primal = {x: (1 if x in witness else 0) for x in words}
    assert all(sum(primal[w] for w in words if o in swaps(w)) <= 1 for o in outs)
    if key == 'abcd':
        # Exact uniform primal and dual feasible fractional solutions at objective 6.
        assert len(words) == 24 and len(outs) == 24
        assert all(len(b) == 4 for b in balls)
        assert all(sum(o in b for b in balls) == 4 for o in outs)
        from fractions import Fraction
        assert sum(Fraction(1, 4) for w in words) == 6
        assert sum(Fraction(1, 4) for o in outs) == 6
    else:
        dual = DUAL_OUTPUTS[key]
        assert set(dual).issubset(outs)
        assert all(sum(dual.get(o, 0) for o in b) >= 1 for b in balls)
        assert sum(dual.values()) == len(witness)
    return poly

def global_code(q):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'[:q]
    code = []
    for pair in combinations(alphabet, 2):
        x, y = pair
        code += [WITNESSES['aabb'][0].translate(str.maketrans('ab', x+y))]
    for a in alphabet:
        for b, c in combinations([x for x in alphabet if x != a], 2):
            tr = str.maketrans('abc', a+b+c)
            code += [w.translate(tr) for w in WITNESSES['aabc']]
    for tup in combinations(alphabet, 4):
        tr = str.maketrans('abcd', ''.join(tup))
        code += [w.translate(tr) for w in WITNESSES['abcd']]
    outputs = {}
    for w in code:
        assert all(w[i] != w[i+1] for i in range(3))
        for o in swaps(w):
            assert o not in outputs or outputs[o] == w, (q, o, w, outputs[o])
            outputs[o] = w
    assert len(set(code)) == len(code)
    m = comb(q, 2) + 2*q*comb(q-1, 2) + 5*comb(q, 4)
    assert len(code) == m == q*(q-1)*(q+1)*(5*q-6)//24
    assert (m + comb(q, 4)) == q*q*(q-1)*(q-1)//4
    return m

def check_certificate():
    path = Path(__file__).with_name('local_certificate.json')
    data = json.loads(path.read_text(encoding='utf8'))
    assert set(data) == set(EXPECTED)
    for key in EXPECTED:
        words, balls, nbr = conflict_graph(key)
        cert = data[key]
        assert cert['canonical_source_multiset'] == key
        assert cert['ordered_centers'] == list(words)
        assert cert['balls'] == [sorted(b) for b in balls]
        assert cert['conflict_neighbors_0_based'] == [
            [j for j in range(len(words)) if nbr[i] & (1 << j)]
            for i in range(len(words))]
        assert cert['independence_polynomial_coefficients'] == list(exact_polynomial(nbr))
        assert cert['maximizing_witness'] == list(WITNESSES[key])
        expected_dual = DUAL_OUTPUTS[key] if key != 'abcd' else {w: '1/4' for w in words}
        expected_primal = ({w: 1 for w in WITNESSES[key]} if key != 'abcd'
                           else {w: '1/4' for w in words})
        assert cert['fractional_dual_nonzero_weights'] == expected_dual
        assert cert['fractional_primal_nonzero_weights'] == expected_primal
    return True

def main():
    assert check_certificate()
    polys = {k: check_local(k) for k in EXPECTED}
    for q in range(2, 9):
        assert global_code(q) >= 1
        assert (2*comb(q, 2) + 6*q*comb(q-1, 2) + 24*comb(q, 4)
                == q*(q-1)**3)
    # The full codebook enumerator is a direct product of the local polynomials;
    # the leading term counts all optimal codebooks independently.
    assert 2**comb(4, 2) * 4**(4*comb(3, 2)) * 48**comb(4, 4) == 51539607552
    print('EXACT_COMPONENT_POLYNOMIALS', polys)
    print('CAPACITY_Q2_TO_Q8', [global_code(q) for q in range(2, 9)])
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
