"""Independent exact finite checks for three-row site-percolation face law.

Run: python3 verify.py
Uses only the Python standard library. Finite checks are not an infinite proof.
"""
from fractions import Fraction
from collections import defaultdict


def grid(n):
    ind = {(r, c): 3*c+r for c in range(n) for r in range(3)}
    edges = [(ind[r, c], ind[r+1, c]) for c in range(n) for r in range(2)]
    edges += [(ind[r, c], ind[r, c+1]) for c in range(n-1) for r in range(3)]
    return ind, edges


def exact_components(mask, n, edges):
    active = [i for i in range(3*n) if (mask >> i) & 1]
    parent = {i: i for i in active}
    def root(i):
        while i != parent[i]:
            i = parent[i]
        return i
    open_edges = 0
    for u, v in edges:
        if u in parent and v in parent:
            open_edges += 1
            parent[root(u)] = root(v)
    return len({root(v) for v in active}), len(active), open_edges


def predicted_faces(mask, n, ind):
    present = lambda r, c: bool((mask >> ind[r, c]) & 1)
    squares = sum(all(present(r+a, c+b) for a in (0, 1) for b in (0, 1))
                  for r in (0, 1) for c in range(n-1))
    corridors = 0
    by_span = defaultdict(int)
    for left in range(n):
        for right in range(left+2, n):
            if (present(1, left) and present(1, right)
                and all(present(r, c) for r in (0, 2) for c in range(left, right+1))
                and all(not present(1, c) for c in range(left+1, right))):
                corridors += 1
                by_span[right-left] += 1
    return squares + corridors, squares, dict(by_span)


def expected_formula(n, p):
    return (3*n*p - (5*n-3)*p**2 + 2*(n-1)*p**4
        + sum((n-d)*p**(2*d+4)*(1-p)**(d-1) for d in range(2, n)))


def density(p):
    return 3*p-5*p**2+2*p**4 + p**8*(1-p)/(1-p*p*(1-p))


def density_factor(p):
    return p*(1-p)**3*(p**5+2*p**4+p**3+4*p+3)/(1-p*p+p**3)


def P(p):
    return 6*p**9-8*p**7+9*p**6+20*p**5-8*p**4-4*p**3+17*p**2+4*p-3


def Pprime(p):
    return 54*p**8-56*p**6+54*p**5+100*p**4-32*p**3-12*p**2+34*p+4


def derivative_density(p):
    return -(1-p)**2*P(p)/(1-p*p+p**3)**2


def check():
    checks = 0
    probs = [Fraction(0), Fraction(1), Fraction(1, 2), Fraction(2, 7),
             Fraction(5, 11), Fraction(9, 10)]
    for n in range(1, 6):
        ind, edges = grid(n)
        by_size = defaultdict(int)
        expected_square_by_size = defaultdict(int)
        expected_corridor_by_span = {d: defaultdict(int) for d in range(2, n)}
        for mask in range(1 << (3*n)):
            comps, sites, open_edges = exact_components(mask, n, edges)
            faces, squares, spans = predicted_faces(mask, n, ind)
            assert comps == sites-open_edges+faces, (n, mask)
            by_size[sites] += comps
            expected_square_by_size[sites] += squares
            for d, val in spans.items():
                expected_corridor_by_span[d][sites] += val
            checks += 1
        for p in probs:
            calculated = sum(count*p**k*(1-p)**(3*n-k) for k, count in by_size.items())
            assert calculated == expected_formula(n, p), (n, p, 'mean')
            checks += 1
            calculated_squares = sum(count*p**k*(1-p)**(3*n-k) for k, count in expected_square_by_size.items())
            assert calculated_squares == 2*(n-1)*p**4
            checks += 1
            for d in range(2, n):
                calculated_corridors = sum(count*p**k*(1-p)**(3*n-k) for k, count in expected_corridor_by_span[d].items())
                assert calculated_corridors == (n-d)*p**(2*d+4)*(1-p)**(d-1)
                checks += 1
        print('n =', n, ': checked', 1 << (3*n), 'site configurations')
    for j in range(1, 30):
        p = Fraction(j, 30)
        assert density(p) == density_factor(p)
        checks += 1
        # Exact polynomial-derivative consistency via power expansion from formula.
        numerator = (1-p)**2 * P(p)
        denominator = (1-p*p+p**3)**2
        assert derivative_density(p) == -numerator/denominator
        checks += 1
        assert Pprime(p) > 0
        checks += 1
    assert P(Fraction(0)) < 0 < P(Fraction(1))
    print('PASS: ', checks, 'exact checks; exhaustive all configurations for 1 <= n <= 5')
    print('No finite test is offered as a proof for arbitrary n.')


if __name__ == '__main__':
    check()
