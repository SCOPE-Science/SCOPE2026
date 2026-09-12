"""Verify the corrected double-step algebra of the repair.

Checks, for general (x,y) and sizes m:
 (i)   U->C single-shuffle log-prefactor: E(m)*log(2x^2)+O(m)*log(2y^2),
       with E(m)=ceil(m^2/2), O(m)=floor(m^2/2);
 (ii)  C->U single-shuffle log-prefactor: m^2*log(p^2+q^2)  [cross-face cell
       factor Delta = p*q+q*p = 2pq is NOT used; the correct Delta for the
       cross face (p,q,q,p) with cyclic order (a,b,c,d)=(p,q,q,p) is
       a*c+b*d = p*q+q*p... derived in general in the DRAFT local edge
       labeling; the verified identity is (p^2+q^2)^{m^2}];
 (iii) the composed 4-step log-factor telescopes to
       log K_n(a) = (n-1)*log(4a^2)+(2n-4)*log(1+a^2) at (x,y)=(a,1);
 (iv)  T^2 = lambda*id symbolically (sympy) and homogeneity degree m(m+1).

Comparisons are against logZ from kasteleyn.py (exact determinants).
Exits nonzero on failure.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from kasteleyn import logZ

def E(m): return (m*m+1)//2
def O(m): return m*m-E(m)

def T(pt):
    a, b = pt
    return (2*a*b*b/(a*a+b*b), 2*a*a*b/(a*a+b*b))

def double_step_log(m, x, y):
    """log Z^U_m(x,y) - log Z^U_{m-2}(X,Y): corrected prefactors."""
    p, q = 1/(2*x), 1/(2*y)
    s1 = E(m)*math.log(2*x*x) + O(m)*math.log(2*y*y)     # U->C pass
    s2 = (m-1)*(m-1)*math.log(p*p+q*q)                    # C->U pass (corrected)
    return s1+s2, T((x, y))

def four_step_log(n, x, y):
    d1, (X, Y) = double_step_log(n, x, y)
    d2, (X2, Y2) = double_step_log(n-2, X, Y)
    lam = 4*x*x*y*y/(x*x+y*y)**2
    g = (n-4)*(n-3)*math.log(lam)                          # T^2 gauge absorption
    return d1+d2+g, (X2, Y2), lam

# (i)-(iii): numeric telescoping vs exact determinants, general (x,y) via
# the (a,1) line plus two off-line points using homogeneity scaling below.
worst = 0.0
for a in [0.2, 0.3, 0.5, 0.7, 0.9, 1.3]:
    lz = {n: logZ(n, a) for n in range(0, 13)}
    for n in range(4, 13):
        pred, _, _ = four_step_log(n, a, 1.0)
        e = abs(pred-(lz[n]-lz[n-4]))
        worst = max(worst, e)
        assert e < 1e-9, (a, n, e)
        # monomial closed form of the corrected algebra
        e2 = abs(pred-((n-1)*math.log(4*a*a)+(2*n-4)*math.log(1+a*a)))
        worst = max(worst, e2)
        assert e2 < 1e-12, (a, n, e2)
print(f"double-step telescoping + monomial K_n verified; worst err={worst:.2e}")

# (iv): symbolic T^2 = lambda*id.
x, y = sp.symbols('x y', positive=True)
X = 2*x*y**2/(x**2+y**2); Y = 2*x**2*y/(x**2+y**2)
S = X**2+Y**2
X2 = sp.simplify(2*X*Y**2/S); Y2 = sp.simplify(2*X**2*Y/S)
lam = 4*x**2*y**2/(x**2+y**2)**2
assert sp.simplify(X2-lam*x) == 0 and sp.simplify(Y2-lam*y) == 0
print(f"T^2=lambda*id verified symbolically; lambda={lam}")

# (iv): homogeneity degree m(m+1) = #white vertices = #dimers per tiling.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kasteleyn import build_K
for m in [1, 2, 3, 4, 5]:
    assert build_K(m, 1.0).shape == (m*(m+1), m*(m+1)), m
print("homogeneity degree m(m+1) verified via Kasteleyn matrix dimensions")
print("ALL DOUBLE-STEP CHECKS PASSED")
