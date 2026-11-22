"""Independent direct Boolean-matrix multiplication check for a rank-one centralizer census.
Python 3.8+; no third-party packages. Run: python3 verify.py
"""
from math import comb
from collections import Counter


def no_zero_rows_columns(c):
    # Inclusion-exclusion on missing rows and columns.
    return sum((-1) ** (i + j) * comb(c, i) * comb(c, j)
               * 2 ** ((c - i) * (c - j))
               for i in range(c + 1) for j in range(c + 1))


def predicted(n, u, v):
    a, b, c = u.bit_count(), v.bit_count(), (u & v).bit_count()
    return (2 ** ((n-a)*(n-b))
            * (1 + no_zero_rows_columns(c)
               * (2**a-1)**(a-c) * (2**b-1)**(b-c)))


def multiply(n, A, B):
    # Row masks; explicit Boolean composition, no row/column-cover reductions.
    result = []
    for row in A:
        out = 0
        for j in range(n):
            if (row >> j) & 1:
                out |= B[j]
        result.append(out)
    return tuple(result)


def actual(n, u, v):
    matrix = tuple(v if (u >> i) & 1 else 0 for i in range(n))
    side = 1 << n
    found = 0
    for bits in range(1 << (n*n)):
        other = tuple((bits >> (i*n)) & (side-1) for i in range(n))
        if multiply(n, matrix, other) == multiply(n, other, matrix):
            found += 1
    return found


def multiplicity(n, a, b, c):
    return comb(n,c)*comb(n-c,a-c)*comb(n-a,b-c)


def run():
    assert [no_zero_rows_columns(i) for i in range(5)] == [1, 1, 7, 265, 41503]
    for n in (1,2,3):
        tally = Counter()
        for u in range(1, 1 << n):
            for v in range(1, 1 << n):
                expected = predicted(n, u, v)
                observed = actual(n, u, v)
                assert observed == expected, (n,u,v,observed,expected)
                tally[(u.bit_count(),v.bit_count(),(u&v).bit_count())] += 1
        for triple, count in tally.items():
            assert count == multiplicity(n,*triple)
        assert sum(tally.values()) == ((1 << n)-1)**2
        print(f'ALL n={n}: {sum(tally.values())} rectangular relations checked against every Boolean matrix')
    n = 4
    representative = {}
    tally = Counter()
    for u in range(1, 1 << n):
        for v in range(1, 1 << n):
            triple = (u.bit_count(),v.bit_count(),(u&v).bit_count())
            representative.setdefault(triple, (u,v))
            tally[triple] += 1
    assert sum(tally.values()) == ((1<<n)-1)**2
    for triple, count in tally.items():
        assert count == multiplicity(n,*triple)
    for triple,(u,v) in representative.items():
        expected = predicted(n,u,v)
        observed = actual(n,u,v)
        assert observed == expected, (n,triple,observed,expected)
    print(f'ORBIT REPRESENTATIVES n=4: {len(representative)} triples checked against all 65,536 matrices')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
