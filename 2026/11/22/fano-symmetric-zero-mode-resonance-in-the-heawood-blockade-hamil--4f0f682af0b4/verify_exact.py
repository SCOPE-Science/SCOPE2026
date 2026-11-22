"""Exact, self-contained finite certificates for a two-shore blockade model.

Uses Python 3, NumPy and SymPy. Only integer and finite-field arithmetic
is used; no floating-point computation is relied upon for a proof.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent


def build():
    nbr = [0] * 14
    for i, p in enumerate(range(1, 8)):
        for j, ell in enumerate(range(1, 8)):
            if ((p & ell).bit_count() % 2) == 0:
                nbr[i] |= 1 << (7 + j)
                nbr[7 + j] |= 1 << i
    states = [s for s in range(1 << 14)
              if all(not ((s >> i) & 1) or not (s & nbr[i])
                     for i in range(14))]
    even = [s for s in states if s.bit_count() % 2 == 0]
    odd = [s for s in states if s.bit_count() % 2 == 1]
    columns = {s: k for k, s in enumerate(even)}
    A = np.zeros((len(odd), len(even)), dtype=np.int64)
    B = A.copy()
    for i, s in enumerate(odd):
        for v in range(14):
            new = s ^ (1 << v)
            if new in columns:
                (A if v < 7 else B)[i, columns[new]] = 1
    return states, even, odd, A, B


def exact_integer_rank(X):
    rows = [{j: int(v) for j, v in enumerate(row) if v}
            for row in X]
    r = 0
    for j in range(X.shape[1]):
        pivot_row = next((k for k in range(r, len(rows))
                          if j in rows[k]), None)
        if pivot_row is None:
            continue
        rows[r], rows[pivot_row] = rows[pivot_row], rows[r]
        pivot = rows[r]
        a = pivot[j]
        for k in range(r + 1, len(rows)):
            b = rows[k].get(j, 0)
            if b == 0:
                continue
            g = math.gcd(a, b)
            c, d = a // g, b // g
            new = {h: c * v for h, v in rows[k].items() if h != j}
            for h, v in pivot.items():
                if h == j:
                    continue
                w = new.get(h, 0) - d * v
                if w:
                    new[h] = w
                else:
                    new.pop(h, None)
            if new:
                common = 0
                for v in new.values():
                    common = math.gcd(common, v)
                if common > 1:
                    new = {h: v // common for h, v in new.items()}
            rows[k] = new
        r += 1
        if r == len(rows):
            break
    return r


def permutations():
    points = list(range(1, 8))
    inc = {ell: frozenset(p for p in points
                           if ((p & ell).bit_count() % 2) == 0)
           for ell in points}
    result = []
    for a, b, c in itertools.permutations(points, 3):
        def image(p):
            return ((a if p & 1 else 0) ^ (b if p & 2 else 0)
                    ^ (c if p & 4 else 0))
        if len({image(p) for p in points}) != 7:
            continue
        line_image = {ell: next(q for q, I in inc.items()
                                if I == frozenset(image(p) for p in inc[ell]))
                      for ell in points}
        result.append([image(p) - 1 for p in points] +
                      [7 + line_image[ell] - 1 for ell in points])
    return result


def orbit_counts(states):
    group = permutations()
    assert len(group) == 168
    seen = set()
    even_orbits = odd_orbits = 0
    for s in states:
        if s in seen:
            continue
        orbit = {sum(1 << perm[i] for i in range(14) if (s >> i) & 1)
                 for perm in group}
        assert not (seen & orbit)
        seen.update(orbit)
        if s.bit_count() % 2:
            odd_orbits += 1
        else:
            even_orbits += 1
    assert len(seen) == len(states)
    return even_orbits, odd_orbits


def det_mod(AA, BB, t, prime):
    M = (AA * t + BB) % prime
    d = 1
    for j in range(len(M)):
        k = next((k for k in range(j, len(M)) if M[k, j]), None)
        if k is None:
            return 0
        if k != j:
            M[[j, k]] = M[[k, j]]
            d = -d % prime
        pivot = int(M[j, j])
        d = d * pivot % prime
        inv = pow(pivot, -1, prime)
        inds = np.flatnonzero(M[j + 1:, j]) + j + 1
        if len(inds):
            factors = M[inds, j] * inv % prime
            M[inds, j:] = (M[inds, j:] -
                           factors[:, None] * M[j, j:]) % prime
    return d


def minor_identity_checks(A, B, only=None):
    idx = json.loads((HERE / 'minor_indices.json').read_text())
    primes = [int(sp.nextprime(1000000007 + 1000 * j)) for j in range(12)]
    modulus = math.prod(primes)
    assert len(set(primes)) == len(primes)
    t = sp.symbols('t')
    q = 1440*t**8 + 7125*t**6 - 17018*t**4 + 7125*t**2 + 1440
    common = -4334215495680 * t**80 * (t*t-1)**9 * q**6
    for k, factor in [(0, t*t-5), (1, 5*t*t-1)]:
        if only is not None and k != only:
            continue
        ind = idx[f'minor_{k}']
        rows, cols = ind['rows'], ind['cols']
        assert len(rows) == len(cols) == 225
        assert len(set(rows)) == len(set(cols)) == 225
        AA, BB = A[np.ix_(rows, cols)], B[np.ix_(rows, cols)]
        deg = np.count_nonzero(AA + BB, axis=1)
        # For |t|=1 each nonzero matrix entry has modulus one.
        # Hadamard plus Cauchy's coefficient estimate bounds every
        # determinant coefficient by sqrt(product(row nonzero counts)).
        bound2 = math.prod(int(d) for d in deg)
        candidate = sp.Poly(sp.expand(common * factor), t, domain=sp.ZZ)
        assert candidate.degree() <= 225
        max_claim_coeff = max(abs(int(c)) for c in candidate.all_coeffs())
        bound = math.isqrt(bound2) + 1
        assert modulus > 2 * (bound + max_claim_coeff)
        coef = [int(c) for c in candidate.all_coeffs()]
        for p in primes:
            modular_coef = [c % p for c in coef]
            for x in range(226):
                observed = det_mod(AA, BB, x, p)
                claimed = 0
                for c in modular_coef:
                    claimed = (claimed * x + c) % p
                assert observed == claimed, (k, p, x)
        # The difference has degree <=225, and vanishes at 226
        # distinct points modulo each prime. Therefore all integer
        # coefficients are divisible by their product. The proved
        # coefficient bounds make that possible only for zero.
    return primes


def main():
    import sys
    only = None if len(sys.argv) == 1 else int(sys.argv[1])
    assert only is None or only in (0, 1)
    states, even, odd, A, B = build()
    assert (len(states), len(even), len(odd)) == (458, 232, 226)
    assert orbit_counts(states) == (13, 14)
    for t, expected in [(0, 155), (1, 216), (2, 225)]:
        assert exact_integer_rank(A * t + B) == expected
    primes = minor_identity_checks(A, B, only)
    # Distinct 225-minor factors are (t^2-5) and (5t^2-1).
    # Their common factors away from 0, +/-1 are powers of q(t).
    # For u=t^2+t^-2 >=2, q(t)/t^4 = 1440*u^2+7125*u-19898;
    # this is increasing and at u=2 equals 112>0.
    assert 1440*2**2+7125*2-19898 == 112
    print('PASS: 458 states; 13/14 invariant orbits; ranks 155,216,225;')
    print('minor identities certified by',len(primes),'primes; selection',only)
    if only is None:
        print('Real-parameter nullities: t=0:148; |t|=1:26; otherwise:8.')

if __name__ == '__main__':
    main()
