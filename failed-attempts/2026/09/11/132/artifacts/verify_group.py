"""Certify infinite order of Theta = Psi o Phi for S3={SW,N,E,SE}.
Stdlib only. Prints GROUP_WORD_OK on success."""
from fractions import Fraction

# 1. Phi, Psi are involutions (exact rational-function check at a generic integer point
#    plus symbolic identity encoded as polynomial equalities verified on samples is NOT proof;
#    instead verify the involution identities as rational functions symbolically by hand-derived
#    formulas: Phi^2(x,y)=(x,y) and Psi^2(x,y)=(x,y) hold identically since
#    1/((1/(x(y+1)))(y+1)) = x and (x^2+1)/(x*((x^2+1)/(x*y))) = y. Check exact Fractions:
x, y = Fraction(3, 2), Fraction(7, 5)
X1 = Fraction(1, 1) / (x * (y + 1))
assert Fraction(1, 1) / (X1 * (y + 1)) == x, "Phi involution failed"
Y1 = (x * x + 1) / (x * y)
assert (x * x + 1) / (x * Y1) == y, "Psi involution failed"

# 2. Fixed-point quintic f(x) = x^5 - x^4 + x^3 + 2x^2 - 1, unique root in (0,1).
def f(v):  # v a Fraction
    return v**5 - v**4 + v**3 + 2*v**2 - 1
a, b = Fraction(634, 1000), Fraction(635, 1000)
fa, fb = f(a), f(b)
assert fa < 0 < fb, (fa, fb)
# f'(x) = x*(5x^3 - 4x^2 + 3x + 4); inner cubic g has g'(x)=15x^2-8x+3, disc 64-180<0,
# so g strictly increasing on R... (g' > 0 since leading coeff positive and disc<0),
# g(0)=4>0 hence g>0 on [0,inf), hence f'>0 on (0,inf): f strictly increasing, unique root.
# Check g'(x) > 0 for all real x: discriminant of 15x^2-8x+3 is 64-4*15*3 = 64-180 = -116 < 0.
assert 64 - 4*15*3 < 0
print("enclosure: f(0.634) =", float(fa), " f(0.635) =", float(fb))
x0_lo, x0_hi = a, b  # x0 in (0.634, 0.635)

# 3. Trace enclosure: tr = x0^3 - 2 in (-2, 2).
tr_lo = x0_lo**3 - 2
tr_hi = x0_hi**3 - 2
assert tr_lo > -2 and tr_hi < 2, (tr_lo, tr_hi)
print("trace interval: [", float(tr_lo), ",", float(tr_hi), "]")
assert float(tr_lo) < -1.74 and float(tr_hi) > -1.75  # strictly inside (-2,2)

# 4. Trace minimal polynomial T(w) = Res_z(f(z), w-(z^3-2)) is irreducible over Q:
#    T mod 5 irreducible (no linear factor + no irreducible-quadratic factor).
mod = 5
T = [1, 18 % 5, 120 % 5, 367 % 5, 527 % 5, 289 % 5]  # coeffs desc w^5..w^0
T = [c % mod for c in T]
print("T mod 5 =", T)
def peval(c, v):
    r = 0
    for a in c:
        r = (r * v + a) % mod
    return r
assert all(peval(T, v) != 0 for v in range(mod)), "T has linear factor mod 5"
# all monic quadratics w^2 + a w + b; keep irreducible ones (no root), trial-divide T
def pmul(p, q):
    r = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] = (r[i+j] + a*b) % mod
    return r
def pmod(p, d):
    p = list(p)
    while len(p) >= len(d) and any(p):
        c = p[0]  # d monic
        for i in range(len(d)):
            p[i] = (p[i] - c*d[i]) % mod
        while p and p[0] == 0:
            p.pop(0)
    return p or [0]
quads = [[1, a, b] for a in range(mod) for b in range(mod)
         if all(peval([1, a, b], v) != 0 for v in range(mod))]
print("irreducible monic quadratics mod 5:", len(quads))
assert len(quads) == 10
for q in quads:
    assert pmod(T, q) != [0], ("T divisible by quadratic mod 5", q)
print("T mod 5 irreducible => T irreducible over Q (degree 5).")

# 5. Cyclotomic exclusion: phi(m)/2 = 5 => m in {11, 22}; minimal poly of 2cos(2pi/11) is
#    M11(w) = w^5+w^4-4w^3-3w^2+3w+1; resultant Res(T,M11) = 3056498369 != 0.
def sylvester_det(P, Q):
    # P, Q integer polys (desc). Determinant of Sylvester matrix via Fraction elimination.
    m, n = len(P)-1, len(Q)-1
    N = m + n
    M = [[Fraction(0)]*N for _ in range(N)]
    for i in range(n):
        for j, c in enumerate(P):
            M[i][i+j] = Fraction(c)
    for i in range(m):
        for j, c in enumerate(Q):
            M[n+i][i+j] = Fraction(c)
    det = Fraction(1)
    for k in range(N):
        piv = next((r for r in range(k, N) if M[r][k] != 0), None)
        assert piv is not None, "singular Sylvester"
        if piv != k:
            M[k], M[piv] = M[piv], M[k]
            det = -det
        det *= M[k][k]
        for r in range(k+1, N):
            fac = M[r][k]/M[k][k]
            for c in range(k, N):
                M[r][c] -= fac*M[k][c]
    return det
Tz = [1, 18, 120, 367, 527, 289]
M11 = [1, 1, -4, -3, 3, 1]
res = sylvester_det(Tz, M11)
print("Res(T,M11) =", res)
assert res != 0
assert res == 3056498369, res
print("GROUP_WORD_OK")
