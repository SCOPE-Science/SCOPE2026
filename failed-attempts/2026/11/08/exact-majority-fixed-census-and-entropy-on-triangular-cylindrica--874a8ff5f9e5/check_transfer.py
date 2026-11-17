"""Exact finite-state certificate for fixed majority configurations on C_n Cartesian K_3.

Requires Python 3 and SymPy. All comparisons are over the integers.
"""
import sympy as sp

z = sp.Symbol('z')


def bit(s, r):
    return (s >> r) & 1


def legal(a, b, c):
    for r in range(3):
        votes = bit(a, r) + bit(c, r) + bit(b, (r+1) % 3) + bit(b, (r+2) % 3)
        if bit(b, r) and votes < 2:
            return False
        if not bit(b, r) and votes > 2:
            return False
    return True


T = sp.zeros(64)
for a in range(8):
    for b in range(8):
        for c in range(8):
            if legal(a, b, c):
                T[8*a+b, 8*b+c] = 1
assert sum(T) == 182

P = (z-3)*(z-1)*(z+1)*(z**3+z+1)**2*(z**3-z**2-1) * (z**3-2*z**2+z+1)**2*(z**4+z**2-3*z-3)
assert sp.Poly(T.charpoly(z).as_expr(), z) == sp.Poly(z**42 * P, z)

# Schur recursion: for h(z)=a_d z^d+...+a_0 with |a_0|<|a_d|,
# h has every zero in |z|<1 iff (a_d*h(z)-a_0*z^d*h(1/z))/z does.
# Apply it to p(2*z) for each nontrivial factor.
expected = [
    [(8,1),(63,16),(79,-2)],
    [(8,-1),(63,-4),(59,-32)],
    [(8,1),(21,8),(29,-22)],
    [(16,-3),(247,-96),(51793,17044),(3623,150)],
]
polys = [z**3+z+1,z**3-z**2-1,z**3-2*z**2+z+1,z**4+z**2-3*z-3]
for polynomial, pairs in zip(polys, expected):
    h = sp.Poly(polynomial.subs(z, 2*z), z)
    for leading, constant in pairs:
        assert h.LC() == leading and h.TC() == constant
        assert abs(constant) < abs(leading)
        d = h.degree()
        reverse = sum(h.nth(j)*z**(d-j) for j in range(d+1))
        reduced = sp.Poly(sp.cancel((leading*h.as_expr()-constant*reverse)/z), z)
        h = reduced.primitive()[1]
    assert h.degree() == 0

# Root-power sums using Newton recurrence, independent of eigenvalue approximations.
def powersum(poly, n):
    p = sp.Poly(poly, z)
    d = p.degree()
    c = [p.nth(d-j) for j in range(d+1)]
    S = [d]
    for m in range(1, n+1):
        if m <= d:
            sm = -sum(c[j]*S[m-j] for j in range(1,m)) - m*c[m]
        else:
            sm = -sum(c[j]*S[m-j] for j in range(1,d+1))
        S.append(sm)
    return S[n]

rows = []
Tn = sp.eye(64)
for n in range(1, 12):
    Tn *= T
    formula = 3**n+1+(-1)**n
    formula += 2*powersum(polys[0], n)+powersum(polys[1], n)
    formula += 2*powersum(polys[2], n)+powersum(polys[3], n)
    assert sp.trace(Tn) == formula
    if n >= 3:
        rows.append((n, int(formula)))

print('CHARPOLY_OK')
print('SCHUR_RADIUS_LT_TWO_OK')
print('TRACE_FORMULA_OK')
for n, count in rows:
    print(f'{n}: {count}')
