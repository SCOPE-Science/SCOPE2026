"""Exact point counts for a smooth plane quartic over F_9.

Uses only Python's standard library. Finite fields are represented as
F_3[t]/(t^n+t+2), for n=2,4,6. A field element is the base-three
encoding of its coefficient vector. This program checks irreducibility
by exhaustive trial division by all monic polynomials through degree n/2.
"""
import json
from collections import Counter


def mod_poly(a, b):
    a = a[:]
    while len(a) >= len(b):
        s = a[-1]
        if s:
            h = len(a) - len(b)
            for i, v in enumerate(b):
                a[h + i] = (a[h + i] - s * v) % 3
        a.pop()
    return a


def integer_coefficients(k, size):
    out = []
    for _ in range(size):
        out.append(k % 3)
        k //= 3
    return out


def assert_irreducible(n):
    f = [2, 1] + [0] * (n - 2) + [1]
    for d in range(1, n // 2 + 1):
        for code in range(3**d):
            trial = integer_coefficients(code, d) + [1]
            assert any(mod_poly(f, trial)), (n, d, trial)
    return f


class Field:
    def __init__(self, degree):
        self.n = degree
        self.q = 3**degree
        self.polynomial = assert_irreducible(degree)
        self.vectors = [integer_coefficients(j, degree) for j in range(self.q)]
        self.addition = [
            [self.code([(a[i] + b[i]) % 3 for i in range(degree)])
             for b in self.vectors]
            for a in self.vectors
        ]

    def code(self, vec):
        return sum(a * 3**i for i, a in enumerate(vec))

    def add(self, a, b):
        return self.addition[a][b]

    def neg(self, a):
        return self.code([(-v) % 3 for v in self.vectors[a]])

    def multiply(self, a, b):
        n = self.n
        av, bv = self.vectors[a], self.vectors[b]
        c = [0] * (2*n - 1)
        for i in range(n):
            for j in range(n):
                c[i+j] = (c[i+j]+av[i]*bv[j]) % 3
        for j in range(2*n-2, n-1, -1):
            z = c[j]
            if z:
                # t^n = -t-2 = 2t+1 in characteristic three.
                c[j-n] = (c[j-n]+z) % 3
                c[j-n+1] = (c[j-n+1]+2*z) % 3
        return self.code(c[:n])

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.multiply(result, a)
            a = self.multiply(a, a)
            exponent //= 2
        return result


def count(degree):
    f = Field(degree)
    eta = next(e for e in range(f.q) if f.add(f.multiply(e, e), 1) == 0)
    assert f.power(eta, 9) == eta and eta not in (0, 1, 2)
    # For Y != 0, choose Y=1. The affine equation is
    # X^4 + eta + Z^3 + Z = 0.
    fourth_roots = Counter(f.power(x, 4) for x in range(f.q))
    trace_roots = Counter(f.add(f.power(z, 3), z) for z in range(f.q))
    via_z = 0
    via_x = 0
    root_histogram = Counter()
    for z in range(f.q):
        t = f.neg(f.add(eta, f.add(f.power(z, 3), z)))
        root_histogram[fourth_roots[t]] += 1
        via_z += fourth_roots[t]
    for x in range(f.q):
        t = f.neg(f.add(eta, f.power(x, 4)))
        via_x += trace_roots[t]
    assert via_z == via_x
    # At Y=0, the homogeneous equation forces X=0, leaving [0:0:1].
    return {'extension_degree':degree//2,
            'field_order':f.q,
            'modulus_coefficients_low_to_high':f.polynomial,
            'eta_element_base3':eta,
            'affine_points_both_methods':via_z,
            'projective_points':via_z+1,
            'fibre_size_histogram':dict(sorted(root_histogram.items()))}


def main():
    counts = [count(d) for d in (2, 4, 6)]
    assert [d['projective_points'] for d in counts] == [1, 109, 892]
    traces = [9**m+1-d['projective_points']
              for m,d in enumerate(counts, start=1)]
    assert traces == [9, -27, -162]
    a1 = -traces[0]
    a2 = -(traces[1]+a1*traces[0])//2
    a3 = -(traces[2]+a1*traces[1]+a2*traces[0])//3
    coefficients = [1, a1, a2, a3, 9*a2, 9**2*a1, 9**3]
    assert coefficients == [1,-9,54,-189,486,-729,729]
    # Multiply (1-3T+9T^2)^3 independently of Newton's identities.
    term = [1,-3,9]
    poly = [1]
    for _ in range(3):
        nxt = [0] * (len(poly)+2)
        for i,x in enumerate(poly):
            for j,y in enumerate(term):
                nxt[i+j] += x*y
        poly = nxt
    assert poly == coefficients
    assert sum(coefficients) == 343
    print(json.dumps({'point_counts':counts,'power_sums':traces,
                      'zeta_numerator_coefficients':coefficients,
                      'Jacobian_F9_order':sum(coefficients)},
                     indent=2, sort_keys=True))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
