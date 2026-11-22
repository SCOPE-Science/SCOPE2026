"""Exact reproducibility checks for graded one-point extension profiles.

All computations use integers; no third-party dependencies are required.
"""
from itertools import product
from math import comb
from fractions import Fraction


def add(a, b):
    out = [0] * max(len(a), len(b))
    for k, c in enumerate(a): out[k] += c
    for k, c in enumerate(b): out[k] += c
    return out


def mul_linear(a, t):
    out = [0] * (len(a) + 1)
    for k, v in enumerate(a):
        out[k] += v
        out[k + 1] += t * v
    return out


def type_poly(rows):
    """rows: nonempty equal-width binary strings; 0 denotes A->B."""
    r, s = len(rows), len(rows[0])
    assert all(len(row) == s and set(row) <= set('01') for row in rows)
    result = [0] * (r+s+1)
    for a in product(range(3), repeat=r):  # 0=no arc; 1=x->a; 2=a->x
        partial = [1]
        for j in range(s):
            bad_minus = any(a[i] == 1 and rows[i][j] == '0' for i in range(r))
            bad_plus = any(a[i] == 2 and rows[i][j] == '1' for i in range(r))
            partial = mul_linear(partial, 2-int(bad_minus)-int(bad_plus))
        shift = sum(v != 0 for v in a)
        for k, v in enumerate(partial): result[k+shift] += v
    return result


def direct_poly(rows):
    """Independent direct enumeration for small cases."""
    r, s = len(rows), len(rows[0])
    result = [0] * (r+s+1)
    for v in product(range(3), repeat=r+s):
        a, b = v[:r], v[r:]
        if all(not ((rows[i][j] == '0' and a[i] == 1 and b[j] == 2) or
                    (rows[i][j] == '1' and a[i] == 2 and b[j] == 1))
               for i in range(r) for j in range(s)):
            result[sum(t != 0 for t in v)] += 1
    return result


def binpoly(r, s):
    out = [0] * (r+s+1)
    for p in range(r+1):
        for q in range(s+1):
            out[p+q] += comb(r,p)*comb(s,q)*(2**p+2**q-1)
    return out


def mixed_paths(rows):
    r, s = len(rows), len(rows[0]); ans = 0
    for row in rows:
        z = row.count('0'); ans += z*(s-z)
    for j in range(s):
        z = sum(row[j] == '0' for row in rows); ans += z*(r-z)
    return ans


def run():
    cases = 0; cmp = 0; a3 = 0
    for r,s in [(1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3), (3,4), (4,3)]:
        benchmark = binpoly(r,s)
        for bits in product('01', repeat=r*s):
            rows = [''.join(bits[i*s:(i+1)*s]) for i in range(r)]
            val = type_poly(rows)
            if r+s <= 6:
                assert val == direct_poly(rows), (rows, val)
                cmp += 1
            assert all(b >= v for b, v in zip(benchmark, val)), rows
            assert benchmark[3] - val[3] == mixed_paths(rows) if r+s>=3 else True
            if r+s >= 3: a3 += 1
            assert all(benchmark[k] == val[k] for k in range(min(3, r+s+1)))
            if len(set(bits)) > 1:
                assert all(benchmark[k] > val[k] for k in range(3,r+s+1)), rows
            else: assert benchmark == val
            cases += 1
        print(f'{r}x{s}: {2**(r*s)} orientations; coherent coefficients={benchmark}; checked')
    for n in (1, 2, 3):
        exact_avg = sum(Fraction(sum(type_poly([''.join(bits[i*n:(i+1)*n]) for i in range(n)])), 2**(n*n)) for bits in product('01', repeat=n*n))
        expectation = sum(Fraction(comb(n,p)*comb(n-p,q), 1) * (Fraction(1,1)+Fraction(1,2**p)+Fraction(1,2**q))**n for p in range(n+1) for q in range(n-p+1))
        assert exact_avg == expectation, (n, exact_avg, expectation)
        print(f'exact random expectation n={n}: {expectation}')
    print(f'PASS: {cases} orientations; {cmp} independent direct coefficient enumerations; {a3} cubic defect identities')

if __name__ == '__main__': run()
