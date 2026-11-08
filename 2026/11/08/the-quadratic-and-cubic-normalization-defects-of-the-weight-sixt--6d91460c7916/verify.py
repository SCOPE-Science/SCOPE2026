"""Exact integer certificate for the first graded normalization defects.
Run: python verify.py CERTIFICATE.json (Python 3.9+; standard library only).
"""
import json
import sys
from itertools import product


def lyndon_words(max_weight=16):
    out = []
    for length in range(1, max_weight // 2 + 1):
        for letters in product('23', repeat=length):
            word = ''.join(letters)
            if sum(map(int, word)) > max_weight:
                continue
            if all(word < word[i:] + word[:i] for i in range(1, length)):
                out.append(word)
    return sorted(out, key=lambda word: (sum(map(int, word)), word))


def weight_vectors(weights, total):
    n = len(weights)
    vec = [0] * n
    def walk(index, remaining):
        if index == n:
            if remaining == 0:
                yield tuple(vec)
            return
        w = weights[index]
        for k in range(remaining // w + 1):
            vec[index] = k
            yield from walk(index + 1, remaining - k * w)
        vec[index] = 0
    yield from walk(0, total)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'CERTIFICATE.json'
    cert = json.load(open(filename, encoding='utf8'))
    words = lyndon_words()
    assert words == cert['lyndon_words']
    weights = [sum(map(int, w)) for w in words]
    columns = list(weight_vectors(weights, 16))
    assert len(words) == 26 and len(columns) == 37
    colset = set(columns)
    s2 = {add(a, b) for a in columns for b in columns}
    s3 = {add(v, a) for v in s2 for a in columns}
    assert (len(s2), len(s3)) == (630, 6885)

    def monomial(terms):
        vals = [0] * len(words)
        for w, exponent in terms.items():
            vals[words.index(w)] = exponent
        return tuple(vals)

    h = monomial({'2': 2, '3': 1, '223': 1, '233': 1, '2233': 1})
    assert h not in s2
    lhs = tuple(2 * x for x in h)
    a1 = monomial({'233': 2})
    a2 = monomial({'3': 2, '2233': 1})
    a3 = monomial({'2': 1, '223': 2})
    a4 = monomial({'2': 3, '2233': 1})
    assert all(a in colset for a in [a1, a2, a3, a4])
    assert lhs == add(add(a1, a2), add(a3, a4))
    b1 = monomial({'233': 2})
    b2 = monomial({'3': 2, '2233': 1})
    b3 = monomial({'2': 2, '23': 1, '223': 1})
    b4 = monomial({'3': 1, '23': 1, '233': 1})
    assert all(a in colset for a in [b1, b2, b3, b4])
    assert h == subtract(add(add(b1, b2), b3), b4)
    h3 = {add(h, a) for a in columns} - s3
    assert len(h3) == 22

    active = [i for i, w in enumerate(weights) if w != 15]
    assert len(active) == 22
    support = [tuple(a[i] for i in active) for a in columns]
    def normalize_cuts(name):
        cuts = []
        for ell in cert[name]:
            assert len(ell) == len(active) and all(type(z) is int for z in ell)
            mx = max(sum(z * x for z, x in zip(ell, a)) for a in support)
            cuts.append((tuple((i, z) for i, z in enumerate(ell) if z != 0), mx))
        return cuts

    cuts2 = normalize_cuts('separating_cuts_degree_two')
    cuts3 = normalize_cuts('separating_cuts_degree_three')
    assert (len(cuts2), len(cuts3)) == (37, 170)
    def separated(candidate, degree, cuts):
        v = tuple(candidate[i] for i in active)
        return any(sum(z * v[i] for i, z in nonzero) > degree * bound
                   for nonzero, bound in cuts)

    for degree, semigroup, exceptions, cuts in [
        (2, s2, {h}, cuts2),
        (3, s3, h3, cuts2 + cuts3),
    ]:
        count = 0
        for v in weight_vectors(weights, 16 * degree):
            count += 1
            if v in semigroup or v in exceptions:
                continue
            # Weight-15 Lyndon columns are identically zero; this
            # coordinate hyperplane contains the entire degree-d polytope.
            if any(v[i] != 0 for i, w in enumerate(weights) if w == 15):
                continue
            assert separated(v, degree, cuts), (degree, v)
        assert count == {2: 1051, 3: 17457}[degree]
    print('Generators=37; semigroup dimensions=630,6885; normalized dimensions=631,6907')
    print('Degree-2 holes=1; degree-3 holes=22; all cubic holes are products of the quadratic hole')
    print('Every other nonnegative integral exponent has an exact integer separating certificate')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
