"""Exact coefficient certificate and independent finite checks for three-row rook excitation.

Run: python3 proof/verify_rook_gh.py
Requires only the Python 3 standard library.
"""
from collections import defaultdict
from itertools import product

COLORS = range(3)
EXPECTED = {1:3, 2:-9, 4:27, 5:-48, 6:27, 7:36, 8:-27,
            10:-36, 12:27, 14:9, 18:-9, 27:1}


def symbolic_coefficients():
    """Enumerate all 19^3 pairs of nonempty included subpalettes and row palettes.

    An allowed single column has the required color-successor in its full row
    palette or in the other two entries of that same column. Inclusion-exclusion
    ensures that the row palettes occur exactly, rather than merely as upper bounds.
    """
    choices = [(r, s, (-1)**(r.bit_count()-s.bit_count()))
               for r in range(1,8) for s in range(1,8) if s & ~r == 0]
    assert len(choices) == 19
    totals = defaultdict(int)
    for tup in product(choices,repeat=3):
        r = [z[0] for z in tup]
        s = [z[1] for z in tup]
        sign = tup[0][2]*tup[1][2]*tup[2][2]
        available = [tuple(a for a in COLORS if s[i] >> a & 1) for i in range(3)]
        b = 0
        for c in product(*available):
            if all(((r[i] >> ((c[i]+1)%3)) & 1) or ((c[i]+1)%3 in c)
                   for i in range(3)):
                b += 1
        totals[b] += sign
    return {k:v for k,v in sorted(totals.items()) if v}


def predicted(n, coefficients):
    return sum(v*b**n for b,v in coefficients.items())


def neighbors(n):
    # Vertices (j,i): column j in range(n), row i in range(3).
    return [tuple(3*k+i for k in range(n) if k != j) +
            tuple(3*j+h for h in range(3) if h != i)
            for j in range(n) for i in range(3)]


def update(x, ns):
    # Literal three-state GHM update, not the successor-support criterion.
    return tuple(2 if a == 1 else 0 if a == 2 or not any(x[v] == 1 for v in ns[u])
                 else 1 for u,a in enumerate(x))


def independent_exhaustion(n):
    ns = neighbors(n)
    total = 0
    for x in product(COLORS,repeat=3*n):
        y = update(x,ns)
        z = update(y,ns)
        if update(z,ns) == x and y != x:
            total += 1
            assert y == tuple((c+1)%3 for c in x)
    return total

if __name__ == '__main__':
    coefficients = symbolic_coefficients()
    assert coefficients == EXPECTED, (coefficients, EXPECTED)
    print('symbolic coefficients (base:coefficient):', coefficients)
    for n in range(1,11):
        print('n',n,'P3',predicted(n,coefficients),'orbits',predicted(n,coefficients)//3)
        assert predicted(n,coefficients)%3 == 0
    for n in range(1,5):
        direct = independent_exhaustion(n)
        exact = predicted(n,coefficients)
        print('independent exhaustive update n',n,'states',3**(3*n),'primitive_3',direct,'formula',exact)
        assert direct == exact
    print('ALL CHECKS PASS')
