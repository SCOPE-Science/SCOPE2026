"""Reproducible formal-data + QES necessary-condition computations.
Even sextic M_{c,d} = d^2/dx^2 - (x^6 + c*x^4 + d*x^2).
Run: python3 qes_formal.py (requires sympy). Verifies WORKLOG claims.
"""
import sympy as sp

x, c, d = sp.symbols('x c d')
P = x**6 + c*x**4 + d*x**2
Q = x**4/4 + c*x**2/4
Qp = sp.diff(Q, x)
e = d - c**2/4
print("residual P-(Qp^2)-e*x^2 =", sp.expand(P - Qp**2 - e*x**2))

s, mu = sp.symbols('s mu')
S = s*Qp + mu/x
res = sp.expand(P - (S**2 + sp.diff(S, x)))
print("x^2 coeff of P-(S^2+S'):", res.coeff(x, 2))
print("-> mu_s = s*(e-3*s)/2")

print("Stokes directions theta_k = pi/8 + k*pi/4:")
for k in range(8):
    print(k, f"pi*{1+2*k}/8")


def det_par(n, eps, parity):
    ks = [k for k in range(n+1) if k % 2 == parity]
    m = len(ks)
    ev = eps*(2*n+3)
    M = sp.zeros(m)
    for j, k in enumerate(ks):
        poly = sp.expand(k*(k-1)*x**(k-2) + 2*eps*(x**3 + c*x/2)*k*x**(k-1)
                         + (eps*(3*x**2 + c/2) - ev*x**2)*x**k)
        for i, kk in enumerate(ks):
            M[i, j] = poly.coeff(x, kk)
    return sp.factor(M.det())


for n in range(9):
    for par, eps in [(0, 1), (0, -1), (1, 1), (1, -1)]:
        if (n - par) % 2 != 0:
            continue
        print(f"n={n} par={'ev' if par == 0 else 'od'} eps={eps:+d} det={det_par(n, eps, par)}")
