"""Exact symbolic transfer verification for all-site majority oscillations on cyclic clique cylinders.

Requires Python 3 and SymPy. All coefficients and matrix entries are integers.
"""
from itertools import combinations, product
from sympy import Matrix, Symbol, Poly, factor, trace, nroots, Rational, expand

BALANCED = [sum(1 << i for i in pair) for pair in combinations(range(4), 2)]

def bit(word, row):
    return (word >> row) & 1

def admissible(left, center, right):
    return all(not (bit(left, i) == bit(center, i) == bit(right, i))
               for i in range(4))

def matrix():
    M = Matrix.zeros(36)
    for a, left in enumerate(BALANCED):
        for b, center in enumerate(BALANCED):
            for c, right in enumerate(BALANCED):
                if admissible(left, center, right):
                    M[6*a+b, 6*b+c] = 1
    return M

x = Symbol('x')
EXPECTED = ((x - 1)**3 * (x + 1)**4 * (x*x + 1)**3
            * (x**3 - 2*x*x - 4*x + 1)
            * (x**4 - x**3 - 3*x + 1)**2
            * (x**4 + x**3 + 2*x*x - 3*x + 1)**3)
EXPECT_COUNTS = {3:90, 4:98, 5:270, 6:1388, 7:2940, 8:9866,
                 9:34146, 10:98774, 11:317130, 12:1023212}

if __name__ == '__main__':
    M = matrix()
    assert sum(int(M[i, j] != 0) for i in range(36) for j in range(36)) == 90
    actual = M.charpoly(x).as_expr()
    assert actual.expand() == EXPECTED.expand()
    print('characteristic polynomial factorization verified exactly:')
    print(factor(actual))
    power = M**3
    for n in range(3,13):
        if n > 3: power = power*M
        z = int(trace(power)) + (8 if n%2 == 0 else 0)
        assert z == EXPECT_COUNTS[n], (n, z)
        print(f'n={n} pure K4 states={z}')
    polys=[x**3-2*x*x-4*x+1, x**4-x**3-3*x+1,
           x**4+x**3+2*x*x-3*x+1]
    eigen = [complex(v) for p in polys for v in nroots(p, maxsteps=150)]
    eigen += [1, -1, 1j, -1j]
    maxeig = max(eigen, key=lambda e:abs(e))
    assert abs(maxeig.imag) < 1e-10 and 3.16 < maxeig.real < 3.17
    assert max(abs(v) for v in eigen if abs(v-maxeig)>1e-5) < 2
    print('dominant modulus:', maxeig.real)
    # Exact rational isolation of the three real cubic roots.
    cubic=polys[0]
    assert cubic.subs(x,-2)<0<cubic.subs(x,-1)
    assert cubic.subs(x,0)>0>cubic.subs(x,1)
    assert cubic.subs(x,3)<0<cubic.subs(x,Rational(16,5))
    # Cubic has degree three, so these intervals contain all roots.
    # Schur-Cohn recursive test for both quartics, applied to p(2*w).
    for p in polys[1:]:
        h=Poly(expand(p.subs(x,2*x)),x)
        pairs=[]
        while h.degree()>0:
            coeffs=h.all_coeffs()
            ad,a0=coeffs[0],coeffs[-1]
            assert abs(a0)<abs(ad), (p,pairs)
            pairs.append((int(ad),int(a0)))
            rev=Poly.from_list(coeffs[::-1],gens=x)
            transformed=Poly(ad*h.as_expr()-a0*rev.as_expr(),x)
            assert transformed.nth(0)==0
            h=Poly(transformed.as_expr()/x,x).primitive()[1]
        assert h.degree()==0
        print('strict exact Schur root-isolation certificate:', p, pairs)
    print('three cubic roots isolated in (-2,-1), (0,1), (3,16/5); both quartics inside |z|<2')
    print('all other eigenvalue moduli < 2')
    print('EXACT_TRANSFER_CHECK_PASS')
