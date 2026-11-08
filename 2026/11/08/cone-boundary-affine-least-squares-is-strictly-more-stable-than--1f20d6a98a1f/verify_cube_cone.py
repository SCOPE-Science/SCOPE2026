"""Exact finite-dimensional checks for affine projections with cone/volume sampling.

Use Python 3.10+ and SymPy; all tested finite values are rational.
The universal comparison and asymptotic assertions are proved analytically
in RESULT.md, not inferred from finite calculations.
"""
import math
from functools import lru_cache
from sympy import Rational, binomial, symbols, expand, integrate, factorial


def positive_part(x):
    return max(Rational(0), x)


def stop_loss(n, z):
    """E[(S_n-z)_+] for n independent U[-1,1] variables."""
    z = Rational(z)
    return sum((-1)**k * binomial(n, k) * positive_part(n-2*k-z)**(n+1)
               for k in range(n+1)) / (2**n * factorial(n+1))


def formulas(d):
    a = Rational(3*d, d+2)
    boundary = a*(1+stop_loss(d-1, 1+1/a)+stop_loss(d-1, 1-1/a))
    volume = 1+6*stop_loss(d, Rational(1, 3))
    return boundary, volume


@lru_cache(maxsize=None)
def ih_cell_density(n, cell):
    """Exact density polynomial of S_n on (2 cell-n, 2(cell+1)-n)."""
    x = symbols('x')
    return expand(sum((-1)**k*binomial(n, k)*(x+n-2*k)**(n-1)
                      for k in range(cell+1))/(2**n * factorial(n-1)))


def direct_absolute_integral(n, c, b):
    """Independently integrate |b+c*S_n| against Irwin-Hall density."""
    x = symbols('x'); c, b = Rational(c), Rational(b)
    z = -b/c
    ans = Rational(0)
    for cell in range(n):
        left, right = Rational(2*cell-n), Rational(2*(cell+1)-n)
        knots = sorted(set((left, right, z)) & {left, right})
        if left < z < right:
            knots = [left, z, right]
        else:
            knots = [left, right]
        poly = ih_cell_density(n, cell)
        for a, e in zip(knots[:-1], knots[1:]):
            mid = (a+e)/2
            sign = 1 if b+c*mid>0 else -1
            ans += sign * integrate((b+c*x)*poly, (x, a, e))
    return ans


def run():
    for d in range(2, 11):
        a = Rational(3*d, d+2)
        boundary, volume = formulas(d)
        n = d-1
        direct_boundary = (direct_absolute_integral(n, a, 1+a)
                           + direct_absolute_integral(n, a, 1-a))/2
        direct_volume = direct_absolute_integral(d, 3, 1)
        assert (boundary,volume)==(direct_boundary,direct_volume), (d, boundary, direct_boundary,volume,direct_volume)
        assert 1 < boundary < volume
        assert boundary == Rational(5,3) if d==2 else True
    print('INDEPENDENT_EXACT_IRWIN_HALL_INTEGRALS_OK', 9)

    # The surface and volume Gram matrices are independently obtained
    # from the face-mixture and coordinate-product moments, respectively.
    for d in range(2, 25):
        var_face = Rational(1,d)*1+Rational(d-1,d)*Rational(1,3)
        var_volume = Rational(1,3)
        r2=Rational(d,d+2)
        assert var_face==Rational(d+2,3*d)
        assert var_volume==r2*var_face
        assert 3*r2 == 1/var_face
    print('EXACT_COVARIANCE_AND_RADIAL_MOMENT_IDENTITIES_OK', 23)

    # Check quantitative strictness, representative dimensions, and
    # convergence to the predicted constant without treating these as proof.
    import mpmath as mp
    mp.mp.dps = 50
    gaps=[]
    for d in range(2, 39):
        b,v=formulas(d)
        gaps.append(mp.sqrt(d)*(mp.mpf(v.p)/v.q-mp.mpf(b.p)/b.q))
        assert v>b
    assert gaps[-1]>gaps[10]
    assert gaps[-1]<mp.sqrt(6/mp.pi)
    print('EXACT_STRICT_COMPARISONS_AND_ASYMPTOTIC_SANITY_OK', len(gaps))
    print('EXAMPLE_DIMENSIONS', [(d,str(formulas(d)[0]), str(formulas(d)[1])) for d in (2,3,4,5)])
    print('ALL_CONE_CUBE_AFFINE_PROJECTION_CHECKS_OK')


if __name__=='__main__':
    run()
