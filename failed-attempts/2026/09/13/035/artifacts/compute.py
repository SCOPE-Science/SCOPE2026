"""Verification script for triconfluent-Heun transport Galois-Stokes dichotomy.
Checks: SL2 normal form r(x), sqrt expansion, symmetric-square twist operators,
case-1 tridiagonal determinants D_m(s), Stokes directions, formal exponents.
"""
import sympy as sp
import json

x, s, t = sp.symbols('x s t')
Pcoef = -(3*x**2 + s)   # T(y) = y'' + Pcoef*y' + t*x*y
Qcoef = t*x
# SL2 normal form: y = z*exp(-int P/2) => z'' = r z, r = P^2/4 + P'/2 - Q
r = sp.expand(Pcoef**2/4 + sp.diff(Pcoef, x)/2 - Qcoef)
print("r =", r)

# sqrt(r) series in 1/x
X = sp.symbols('X')  # X = 1/x
# ansatz sqrt = 3/2 x^2 + s/2 + c1/x + c3/x^3 ; solve c1, c3
c1, c3 = sp.symbols('c1 c3')
sq = sp.Rational(3,2)*x**2 + s/2 + c1/x + c3/x**3
diff = sp.expand(sq**2 - r)
# coeffs of x^1 and x^{-1} must vanish
eq1 = sp.expand(diff).coeff(x, 1)
# get coeff of 1/x: substitute x=1/X, multiply
diffX = sp.expand(diff.subs(x, 1/X)*X**4)
eq2 = diffX.coeff(X, 5)  # corresponds to x^{-1} term
sol = sp.solve([eq1, eq2], [c1, c3])
print("c1, c3 =", sol)
c1v = sol[c1]; c3v = sol[c3]

# [sqrt r]_inf polynomial part and b
sqrt_trunc = sp.Rational(3,2)*x**2 + s/2
rem = sp.expand(r - sqrt_trunc**2)
print("r - [sqr]^2 =", rem)  # expect -(t+3)*x
# rem = -2*a_n*b*x^{n-1} with a_n=3/2, n=2 -> b=(t+3)/3
b = (t+3)/3
print("b =", b)

# Formal exponents: seek z = x^rho exp(+/-(x^3/2+sx/2)); 3 rho x = -/+(t+3) x.
rho_plus = -(t+3)/3
rho_minus = (t+3)/3
print("rho_- =", sp.simplify(rho_minus), " sum =", sp.simplify(rho_plus + rho_minus))

# Stokes directions: Re(x^3)=0 -> theta = pi/6 + k*pi/3
import cmath
dirs = [cmath.pi/6 + k*cmath.pi/3 for k in range(6)]
print("Stokes dirs (deg) =", [round(d*180/cmath.pi, 6) for d in dirs])

# ---- Case 1 matrices M^{(m)}: T_{s,3m}(P)=0, P=sum a_j x^j ----
def case1_matrix(m):
    # rows k=0..m (coeff of x^k in T(P)), cols a_0..a_m
    M = sp.zeros(m+1, m+1)
    for k in range(m+1):
        if k-1 >= 0:
            M[k, k-1] = 3*(m-k+1)
        if k+1 <= m:
            M[k, k+1] = -s*(k+1)
        if k+2 <= m:
            M[k, k+2] = (k+1)*(k+2)
    return M

Dm = {}
for m in range(0, 9):
    M = case1_matrix(m)
    d = sp.factor(sp.det(M))
    Dm[m] = str(d)
    print(f"m={m} t={3*m}: D_m(s) =", d)

# numeric roots of D_m for small m
for m in range(1, 9):
    M = case1_matrix(m)
    d = sp.det(M)
    poly = sp.Poly(d, s)
    if poly is None or d == 0:
        print(f"m={m}: identically zero")
        continue
    print(f"m={m}: deg_s={poly.degree()}, roots=", sp.nroots(d) if poly.degree() > 0 else "nonzero const")

# ---- Symmetric square L2(v)=v'''-4 r v'-2 r' v; twist w=eps*(3x^2+s) ----
rp = sp.diff(r, x)
eps, d = sp.symbols('eps d')
w = eps*(3*x**2 + s)
wp = sp.diff(w, x)
wpp = sp.diff(wp, x)
A = sp.expand(3*w**2 + 3*wp - 4*r)          # coeff of P'
B = sp.expand(w**3 + 3*w*wp + wpp - 4*r*w - 2*rp)  # coeff of P
print("A =", A)
print("B =", B)
# leading term of L~(x^d): from A*P' and B*P (P''' lower)
# A deg? B deg?
print("deg A =", sp.Poly(A, x).degree(), " deg B =", sp.Poly(B, x).degree())
# leading coefficients as functions of d,eps: plug P=x^d
Pd = x**d
Lt = sp.expand(sp.diff(Pd, x, 3) + 3*w*sp.diff(Pd, x, 2) + A*sp.diff(Pd, x) + B*Pd)
pLt = sp.Poly(Lt, x)
print("deg L~(x^d) =", pLt.degree())
for k in range(pLt.degree(), max(pLt.degree()-5, -1), -1):
    print(f"  coeff x^{k}:", sp.expand(pLt.nth(k)))

with open("output/artifacts/compute_summary.json", "w") as f:
    json.dump({"r": str(r), "c1": str(c1v), "c3": str(c3v),
               "rho_plus": str(rho_plus), "rho_minus": str(rho_minus),
               "D": Dm}, f, indent=1)
print("wrote output/artifacts/compute_summary.json")
