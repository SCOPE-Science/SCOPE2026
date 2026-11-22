#!/usr/bin/env python3
"""Exact finite certificate for depth-three dyadic Walsh truncations.

The eight Walsh columns are indexed 0,...,7 in Paley order. A length
vector lists retained row counts for these columns. All calculations
except the separately displayed decimal approximations use integers.
"""
from itertools import product

N = 8
LENGTHS = (1, 2, 4, 8)
STANDARD = (8, 4, 2, 2, 1, 1, 1, 1)
EXPECTED = {tuple(STANDARD[j ^ a] for j in range(N)) for a in range(N)}


def unscaled_walsh(level):
    rows = [[1, 1], [1, -1]]
    for _ in range(1, level):
        top = [[u for v in row for u in (v, v)] for row in rows]
        bottom = [[u for v in row for u in (v, -v)] for row in rows]
        rows = top + bottom
    return rows


def gram8(v):
    # The Gram matrix of the normalized truncation multiplied by 8.
    return [[min(v[i], v[j]) if
             (i // (N // min(v[i], v[j])) ==
              j // (N // min(v[i], v[j]))) else 0
             for j in range(N)] for i in range(N)]


def is_pd_integer(matrix):
    # Bareiss fraction-free elimination, without pivot permutations.
    # Successive diagonal pivots are successive leading determinants.
    a = [row[:] for row in matrix]
    previous = 1
    for k in range(N):
        pivot = a[k][k]
        if pivot <= 0:
            return False
        for i in range(k + 1, N):
            for j in range(i, N):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                q, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][j] = a[j][i] = q
        previous = pivot
    return True


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def characteristic_coefficients(a):
    # Faddeev-LeVerrier identity, exact integer divisions.
    b = [[int(i == j) for j in range(N)] for i in range(N)]
    coefficients = [1]
    for k in range(1, N + 1):
        c = matmul(a, b)
        trace = sum(c[i][i] for i in range(N))
        q, rem = divmod(-trace, k)
        assert rem == 0
        coefficients.append(q)
        b = [[c[i][j] + (q if i == j else 0)
              for j in range(N)] for i in range(N)]
    return coefficients


def check_walsh_gram_identity():
    # Independent verification of the Gram formula directly from
    # the signed Walsh matrix at all pairs of lengths and columns.
    w = unscaled_walsh(3)
    assert len(w) == N and all(len(r) == N for r in w)
    assert all(sum(w[k][i] * w[k][j] for k in range(N))
               == (N if i == j else 0)
               for i in range(N) for j in range(N))
    for i in range(N):
        for j in range(N):
            for l1 in LENGTHS:
                for l2 in LENGTHS:
                    m = min(l1, l2)
                    direct = sum(w[k][i] * w[k][j] for k in range(m))
                    predicted = m if i // (N // m) == j // (N // m) else 0
                    assert direct == predicted


def main():
    check_walsh_gram_identity()
    exceptional = set()
    total = 0
    for v in product(LENGTHS, repeat=N):
        h = gram8(v)
        # 68 I - 5H = 40( (17/10)I - G), because G=H/8.
        k = [[68 * int(i == j) - 5 * h[i][j]
              for j in range(N)] for i in range(N)]
        if not is_pd_integer(k):
            exceptional.add(v)
        total += 1
    assert total == 65536
    assert exceptional == EXPECTED
    expected_coefficients = [1, -20, 96, -144, 64, 0, 0, 0, 0]
    for v in sorted(exceptional):
        assert characteristic_coefficients(gram8(v)) == expected_coefficients
    # For the factor q(t)=t^3-16t^2+32t-16 in det(tI-H),
    # q(68/5)=-3088/125<0<q(14)=40. Its largest real root is
    # in (68/5,14), so every exceptional G has top eigenvalue >17/10.
    assert (68**3 - 16*68**2*5 + 32*68*25 - 16*125) == -3088
    assert 14**3 - 16*14**2 + 32*14 - 16 == 40
    print('PASS: 65536 exact cases, exactly 8 exceptional single branches')
    print('PASS: all 65528 others have lambda_max(G)<17/10')
    print('PASS: every exceptional charpoly(H)=t^4(t-4)(t^3-16t^2+32t-16)')
    print('PASS: exceptional lambda_max(G)>17/10; complete optimizer census')
    for v in sorted(exceptional):
        print('optimal length vector:', v)


if __name__ == '__main__':
    main()
