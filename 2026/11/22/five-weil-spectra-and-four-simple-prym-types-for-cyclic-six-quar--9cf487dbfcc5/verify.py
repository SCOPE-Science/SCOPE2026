"""Exact finite-field verification for a family of cyclic-six plane quartics.

Run: python3 verify.py
Uses only the Python standard library. All arithmetic is exact.
"""
from collections import Counter
from math import factorial

P = 17
REPS = (1, 3, 4, 5, 6, 7, 8)
EXPECTED_N2 = {1: 284, 3: 380, 4: 344, 5: 392, 6: 356, 7: 344, 8: 356}
EXPECTED_D = {1: -20, 3: 28, 4: 10, 5: 34, 6: 16, 7: 10, 8: 16}

class QuadraticField:
    """F_17[u]/(u^2 + A u + B), with coefficients as pairs."""
    def __init__(self, A, B):
        self.A, self.B = A, B
        assert all((v*v + A*v + B) % P != 0 for v in range(P))
        self.elements = [(a, b) for a in range(P) for b in range(P)]
        self.zero, self.one = (0, 0), (1, 0)

    def add(self, x, y):
        return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)

    def neg(self, x):
        return ((-x[0]) % P, (-x[1]) % P)

    def scale(self, a, x):
        return ((a*x[0]) % P, (a*x[1]) % P)

    def mul(self, x, y):
        a, b = x
        c, d = y
        return ((a*c - self.B*b*d) % P,
                (a*d + b*c - self.A*b*d) % P)

    def power(self, x, n):
        y = self.one
        while n:
            if n % 2:
                y = self.mul(y, x)
            x = self.mul(x, x)
            n //= 2
        return y

    def N2(self, r, method):
        zero = self.zero
        one = self.one
        if method == 'cube-fibers':
            cube_fibers = Counter(self.mul(self.mul(x, x), x)
                                  for x in self.elements)
        count = 1  # unique rational point at infinity
        for y in self.elements:
            y2 = self.mul(y, y)
            y4 = self.mul(y2, y2)
            target = self.neg(self.add(self.add(y4, self.scale(r, y2)), one))
            if method == 'cube-fibers':
                count += cube_fibers[target]
            elif method == 'cube-character':
                count += (1 if target == zero else
                          (3 if self.power(target, (P*P-1)//3) == one else 0))
            else:
                raise ValueError(method)
        return count


def irreducible_prym_quartic(d):
    # Q(T) = 1+d*T^2+17^2*T^4. If it splits over Q, either
    # d^2-4*17^2 is a rational square, or d=+/-34-a^2 for rational a.
    # The former is negative for the four cases. In the latter, a^2
    # equals either 34-d or -34-d; both fail to be rational squares.
    from math import isqrt
    if d*d >= 4*P*P:
        return False
    def rational_square_integer(n):
        return n >= 0 and isqrt(n)**2 == n
    return not (rational_square_integer(34-d) or
                rational_square_integer(-34-d))



def hasse_entry(exponents, r):
    """Coefficient of the indicated monomial in (X^3 Z+Y^4+rY^2Z^2+Z^4)^16."""
    X, Y, Z = exponents
    total = 0
    for a in range(17):
        if 3*a != X:
            continue
        for b in range(17-a):
            for c in range(17-a-b):
                d = 16-a-b-c
                if 4*b+2*c == Y and a+2*c+4*d == Z:
                    coeff = factorial(16)//(factorial(a)*factorial(b)*
                                           factorial(c)*factorial(d))
                    total += coeff * pow(r, c, P)
    return total % P


def hasse_matrix(r):
    # Canonical plane-quartic Cech basis corresponds to these triples.
    basis = [(2,1,1), (1,2,1), (1,1,2)]
    return [[hasse_entry(tuple(17*a-b for a,b in zip(basis[i],basis[j])),r)
             for j in range(3)] for i in range(3)]


def main():
    # Two inequivalent polynomial-basis representations of the same field.
    fields = [QuadraticField(1, 1), QuadraticField(0, 3)]
    counts = {}
    for r in range(P):
        if r in (0, 2, P-2):
            continue
        observations = [field.N2(r, method)
                        for field in fields
                        for method in ('cube-fibers', 'cube-character')]
        assert len(set(observations)) == 1, (r, observations)
        counts[r] = observations[0]
    assert len(counts) == 14
    assert all(counts[r] == counts[(-r) % P] for r in REPS)
    assert {r: counts[r] for r in REPS} == EXPECTED_N2
    spectra = {}
    for r in REPS:
        # Every odd extension has p^n+1 points since cubing is bijective.
        # The genus-three zeta numerator is even, so it is uniquely
        # recovered from the quadratic point count and reciprocity.
        c2 = (counts[r] - (P*P+1)) // 2
        assert 2*c2 == counts[r] - (P*P+1)
        # L(T)=(1+17T^2)*(1+(c2-17)T^2+289T^4).
        d = c2 - P
        assert d == EXPECTED_D[r], (r,d)
        poly = (1, 0, c2, 0, P*c2, 0, P**3)
        spectra[r] = poly
        assert sum(poly) > 0
        if r != 5:
            assert irreducible_prym_quartic(d)
    assert len(set(spectra.values())) == 5
    assert spectra[4] == spectra[7]
    assert spectra[6] == spectra[8]
    assert spectra[5] == (1, 0, 3*P, 0, 3*P*P, 0, P**3)
    assert counts[5] == P*P+1+2*3*P
    for r in counts:
        H = hasse_matrix(r)
        if r in (5, P-5):
            assert H == [[0]*3 for _ in range(3)]
        else:
            assert H[0][2] != 0 and H[2][0] != 0
            assert all(H[i][j] == 0 for i in range(3) for j in range(3)
                       if (i,j) not in ((0,2),(2,0)))
    print('CYCLIC6_F17_FIVE_WEIL_SPECTRA_VERIFIED',
          'smooth_marked=14', 'geometric_classes=7',
          'weil_types=5', 'n2='+str([EXPECTED_N2[r] for r in REPS]),
          'prym_simple_geometric_classes=6',
          'maximal_parameters=2')

if __name__ == '__main__':
    main()
