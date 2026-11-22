"""Finite exact checks of random evolution algebra idempotent laws over binary fields."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod


def gf_table(q, modulus):
    out = [[0] * q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            x, y, z = a, b, 0
            while y:
                if y & 1: z ^= x
                x <<= 1
                if x & q: x ^= modulus
                y >>= 1
            out[a][b] = z
    return out


def gl2(k):
    return prod((2**k - 2**i) for i in range(k))


def gaussian(n, k):
    if k == 0: return 1
    return prod(2**n-2**i for i in range(k)) // gl2(k)


def predicted(n, q):
    moments = [prod((Fraction(q**n - q**i, q**n) for i in range(k)), start=Fraction(1)) for k in range(n + 1)]
    p = [sum((Fraction((-1)**(k-d) * 2**((k-d)*(k-d-1)//2) * gaussian(k, d), gl2(k)) * moments[k] for k in range(d, n+1)), Fraction(0)) for d in range(n+1)]
    assert sum(p) == 1 and all(0 <= v <= 1 for v in p)
    return {2**d - 1: int(v * q**(n*n)) for d, v in enumerate(p)}


def xor_products(sq, matrix, mul, n, j):
    value = 0
    for i in range(n):
        value ^= mul[sq[i]][matrix[i*n+j]]
    return value


def observed(n, q, modulus):
    mul = gf_table(q, modulus)
    squares = [mul[x][x] for x in range(q)]
    vectors = list(product(range(q), repeat=n))
    nonzero = [((x, tuple(squares[a] for a in x))) for x in vectors if any(x)]
    hist = Counter()
    for matrix in product(range(q), repeat=n*n):
        count = 0
        for x, sq in nonzero:
            if all((xor_products(sq, matrix, mul, n, j)) == x[j] for j in range(n)):
                count += 1
        hist[count] += 1
    return dict(hist)


def main():
    for n,q,mod in [(1,2,3),(1,4,7),(2,2,3),(2,4,7),(2,8,11),(3,2,3),(4,2,3)]:
        p = predicted(n,q)
        obs = observed(n,q,mod)
        assert obs == p, f'{n=} {q=} observed={obs} predicted={p}'
        print(f'PASS n={n} q={q} total_matrices={q**(n*n)} histogram={dict(sorted(obs.items()))}')
    print('VERIFY_OK')

if __name__ == '__main__': main()
