"""Exact finite checks of circular ternary directed-pair observation counts.

Run: python3 verify.py. Requires only Python's standard library.
"""
from itertools import product
from math import comb


def cv(n, k):
    return comb(n + k - 1, k - 1) if n >= 0 else 0


def formula(n):
    """Coefficient of the derived rational generating function."""
    balanced = 0
    for h in range(n // 3 + 1):
        for r in range((n - 3 * h) // 2 + 1):
            # Off-diagonal has total 3*h+2*r. Triples u+v+w=r.
            # h>0 allows the two orientations, h=0 only once.
            balanced += (2 if h else 1) * cv(r, 3) * cv(n - 3 * h - 2 * r, 3)
    # Disconnected active supports (nonempty graph only).
    twice_singleton = 3 * max(n - 1, 0)
    pair_and_singleton = 3 * sum(cv(n - 3 - 2 * r, 3) for r in range((n - 3) // 2 + 1)) if n >= 3 else 0
    three_singletons = comb(n - 1, 2) if n >= 3 else 0
    return balanced - int(n == 0) - twice_singleton - pair_and_singleton - three_singletons


def is_connected(matrix):
    active = {i for i in range(3) if sum(matrix[3*i:3*i+3]) or sum(matrix[i::3])}
    if not active:
        return False
    seen = {next(iter(active))}
    while True:
        new = seen | {j for i in seen for j in active
                      if matrix[3*i+j] or matrix[3*j+i]}
        if new == seen:
            break
        seen = new
    return seen == active


def independent_matrix_count(n):
    """Enumerate all balanced matrices using a unique signed flux parameter."""
    seen = set()
    for h in range(n // 3 + 1):
        for u in range((n - 3*h)//2 + 1):
            for v in range((n - 3*h - 2*u)//2 + 1):
                for w in range((n - 3*h - 2*u - 2*v)//2 + 1):
                    rest = n - 3*h - 2*(u+v+w)
                    for l0 in range(rest+1):
                        for l1 in range(rest-l0+1):
                            l2 = rest-l0-l1
                            for sign in ((1, -1) if h else (1,)):
                                m = [0]*9
                                m[0],m[4],m[8] = l0,l1,l2
                                if sign == 1:
                                    m[1],m[3]=u+h,u
                                    m[5],m[7]=v+h,v
                                    m[6],m[2]=w+h,w
                                else:
                                    m[1],m[3]=u,u+h
                                    m[5],m[7]=v,v+h
                                    m[6],m[2]=w,w+h
                                assert all(sum(m[3*i:3*i+3]) == sum(m[i::3]) for i in range(3))
                                if is_connected(m):
                                    seen.add(tuple(m))
    return len(seen)


def direct_word_count(n):
    spectra = set()
    for word in product(range(3),repeat=n):
        m=[0]*9
        for j in range(n):
            m[3*word[j]+word[(j+1)%n]] += 1
        spectra.add(tuple(m))
    return len(spectra)


def main():
    expected = [0,3,6,11,24,48,95,174,306,510,819,1266,1901,2775]
    assert [formula(n) for n in range(len(expected))] == expected
    for n in range(1, 10):
        assert direct_word_count(n) == formula(n), n
    for n in range(1, 15):
        assert independent_matrix_count(n) == formula(n), n
    print('ALL CHECKS PASSED: exact coefficients n=0..13; circular words n=1..9; balanced connected matrices n=1..14')


if __name__ == '__main__':
    main()
