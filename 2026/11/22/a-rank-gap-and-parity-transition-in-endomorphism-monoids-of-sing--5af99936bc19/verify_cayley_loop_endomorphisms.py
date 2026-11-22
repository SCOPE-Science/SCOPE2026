"""Standalone checks for a characteristic-two looped cyclic evolution algebra.

All operations are computed directly from e_i*e_j=delta_ij(e_i+e_(i+1)).
No packages beyond Python's standard library are required.
"""
from itertools import product


def binary_square_image(v, n):
    return v ^ (((v << 1) | (v >> (n - 1))) & ((1 << n) - 1))


def is_binary_endomorphism(columns, n):
    for i in range(n):
        if binary_square_image(columns[i], n) != (columns[i] ^ columns[(i + 1) % n]):
            return False
        for j in range(i):
            if binary_square_image(columns[i] & columns[j], n):
                return False
    return True


def binary_predicted(n):
    w = (1 << n) - 1
    predicted = {tuple([0]*n), tuple([w]*n)}
    for j in range(n):
        predicted.add(tuple(1 << ((i+j) % n) for i in range(n)))
    return predicted


def exhaust_binary(n):
    solutions = {cs for cs in product(range(1 << n), repeat=n)
                 if is_binary_endomorphism(cs, n)}
    assert solutions == binary_predicted(n), (n, len(solutions), solutions ^ binary_predicted(n))
    print(f'F2 n={n}: all {(1<<n)**n} linear maps checked, {len(solutions)} endomorphisms')


# F4 represented by 0, 1, z, z+1; z^2=z+1.
def f4mul(a,b):
    p = 0
    for i in range(2):
        if (b >> i) & 1:
            p ^= a << i
    if p & 8: p ^= 0b1110
    if p & 4: p ^= 0b111
    return p


def f4_product(x,y):
    n = len(x)
    out = [0]*n
    for i in range(n):
        t = f4mul(x[i], y[i])
        out[i] ^= t
        out[(i+1)%n] ^= t
    return tuple(out)


def f4_is_hom(columns, n):
    for i in range(n):
        square = f4_product(columns[i], columns[i])
        rhs = tuple(columns[i][j] ^ columns[(i+1)%n][j] for j in range(n))
        if square != rhs: return False
        for t in range(i):
            if any(f4_product(columns[t], columns[i])): return False
    return True


def exhaust_f4(n):
    vecs = list(product(range(4), repeat=n))
    found = set()
    for columns in product(vecs, repeat=n):
        if f4_is_hom(columns, n): found.add(columns)
    w = tuple([1]*n)
    expected = {tuple([tuple([0]*n)]*n)}
    for a in (1,2,3): expected.add(tuple([tuple(f4mul(a,x) for x in w)]*n))
    for j in range(n):
        expected.add(tuple(tuple(1 if h==(i+j)%n else 0 for h in range(n)) for i in range(n)))
    assert found == expected, (found ^ expected)
    print(f'F4 n={n}: all {4**(n*n)} linear maps checked, {len(found)} endomorphisms')


def test_composition():
    for n in (3,4,5,6):
        zero = tuple([0]*n)
        w = (1<<n)-1
        psi = tuple([w]*n)
        def apply(columns, x):
            y = 0
            for i in range(n):
                if (x >> i)&1: y ^= columns[i]
            return y
        def compose(left,right):
            return tuple(apply(left,c) for c in right)
        assert compose(psi,psi) == (psi if n%2 else zero)
        for r in range(n):
            rot = tuple(1<<((i+r)%n) for i in range(n))
            assert compose(rot,psi) == psi
            assert compose(psi,rot) == psi
        print(f'F2 n={n}: monoid composition law checked')


if __name__ == '__main__':
    exhaust_binary(3)
    exhaust_binary(4)
    exhaust_f4(3)
    test_composition()
    print('CYCLIC_CAYLEY_ENDOMORPHISMS_VERIFIED')
