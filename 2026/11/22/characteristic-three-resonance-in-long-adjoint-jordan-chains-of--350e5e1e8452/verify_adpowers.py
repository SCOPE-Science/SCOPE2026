"""Self-contained finite-field checks of the inner-derivation power-rank law.

No dependencies outside the Python standard library.  GF(4) uses t^2+t+1.
The computation builds the Lie bracket from strict upper-triangular matrix units,
not from the rank formulas used in the mathematical proof.
"""
from collections import Counter
from itertools import product

PAIRS = [(i, j) for i in range(5) for j in range(i + 1, 5)]
IDX = {ij: t for t, ij in enumerate(PAIRS)}
EXTRA = (IDX[(0, 3)], IDX[(0, 4)], IDX[(1, 4)])
ROOT = IDX[(0, 4)]
FREE = (IDX[(0, 3)], IDX[(0, 4)], IDX[(1, 4)])
SEVEN = (IDX[(0, 1)], IDX[(1, 2)], IDX[(2, 3)], IDX[(3, 4)],
         IDX[(0, 2)], IDX[(1, 3)], IDX[(2, 4)])


def field(q):
    if q == 4:
        add = lambda x, y: x ^ y
        neg = lambda x: x
        def mul(x, y):
            r = 0
            for i in range(2):
                if (y >> i) & 1:
                    r ^= x << i
            for i in (2,):
                if (r >> i) & 1:
                    r ^= 0b111 << (i - 2)
            return r
        inv = {1: 1, 2: 3, 3: 2}
    else:
        add = lambda x, y: (x + y) % q
        neg = lambda x: -x % q
        mul = lambda x, y: x * y % q
        inv = {a: pow(a, -1, q) for a in range(1, q)}
    return add, neg, mul, inv


def rank3(rows, add, neg, mul, inv):
    mat = [list(row) for row in rows]
    r = 0
    for j in range(10):
        pivot = next((i for i in range(r, 3) if mat[i][j]), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        pivot_inv = inv[mat[r][j]]
        mat[r] = [mul(pivot_inv, x) for x in mat[r]]
        for i in range(r + 1, 3):
            t = mat[i][j]
            if t:
                mat[i] = [add(v, neg(mul(t, u))) for v, u in zip(mat[i], mat[r])]
        r += 1
        if r == 3:
            break
    return r


def observed(q):
    add, neg, mul, inv = field(q)
    freq = Counter()
    for vals in product(range(q), repeat=7):
        x = [0] * 10
        for k, v in zip(SEVEN, vals):
            x[k] = v
        # M is the matrix for E -> XE - EX on the 10 matrix units.
        M = [[0] * 10 for _ in range(10)]
        for col, (k, l) in enumerate(PAIRS):
            for h in range(k):
                coef = x[IDX[(h, k)]]
                if coef:
                    row = IDX[(h, l)]
                    M[row][col] = add(M[row][col], coef)
            for h in range(l + 1, 5):
                coef = x[IDX[(l, h)]]
                if coef:
                    row = IDX[(k, h)]
                    M[row][col] = add(M[row][col], neg(coef))
        # Independently compose M with itself and then once more.
        sq = [[0] * 10 for _ in range(3)]
        for t, output in enumerate(EXTRA):
            for middle in range(10):
                u = M[output][middle]
                if u:
                    for col in range(10):
                        v = M[middle][col]
                        if v:
                            sq[t][col] = add(sq[t][col], mul(u, v))
        second_rank = rank3(sq, add, neg, mul, inv)
        cubed = [0] * 10
        for k, output in enumerate(EXTRA):
            factor = M[ROOT][output]
            if factor:
                for j in range(10):
                    cubed[j] = add(cubed[j], mul(factor, sq[k][j]))
        third_rank = int(any(cubed))
        freq[(second_rank, third_rank)] += 1
    # Other three matrix entries are arbitrary and never affect these ranks.
    return {pair: n * q**3 for pair, n in freq.items()}


def expected(q):
    p = 2 if q in (2, 4) else q
    D = Counter()
    for bits in product((0, 1), repeat=4):
        word = ''.join(map(str, bits))
        k = sum(bits)
        weight = (q - 1)**k * q**3
        def enter(second_rank, third_rank, count):
            D[(second_rank, third_rank)] += weight * count
        if k == 0:
            enter(0, 0, q**3)
        elif k == 1:
            n = q**2 if p == 2 or word in ('0100', '0010') else q
            enter(0, 0, n)
            enter(1, 0, q**3 - n)
        elif k == 2:
            if word in ('0011', '0110', '1100'):
                enter(2, 0, q**3)
            elif word in ('1010', '0101'):
                enter(0 if p == 2 else 1, 0, q**2)
                enter(1 if p == 2 else 2, 0, q**3 - q**2)
            else:
                if p == 2:
                    enter(0, 0, q**2)
                    enter(1, 0, q**3 - q**2)
                else:
                    enter(1, 0, q**3)
        elif k == 3:
            enter(3 if word in ('0111', '1110') else 2,
                  int(word in ('0111', '1110') or p != 3), q**3)
        else:
            enter(3, 1, q**3)
    return {k: v for k, v in D.items() if v}


if __name__ == '__main__':
    for q in (2, 3, 4, 5):
        actual = observed(q)
        predicted = expected(q)
        assert actual == predicted, (q, actual, predicted)
        assert sum(actual.values()) == q**10
        print('q=%d: exhaustive %d underlying coordinate combinations; %d power-rank strata; PASS' %
              (q, q**7, len(actual)))
        print('  rank-pair census:', ', '.join('%s:%d' % (str(k), v)
                                            for k, v in sorted(actual.items())))
    print('ALL CHECKS PASSED')
