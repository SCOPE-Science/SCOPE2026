"""Generic check: for s-independent phi=F(x2,y1,y2), H-mean-curvature numerator
restricted to S is (up to an explicit nonzero factor) the Euclidean minimal
surface equation numerator in R^3. Uses undefined function F."""
import sympy as sp

x1, x2, y1, y2, t = sp.symbols('x1 x2 y1 y2 t')
F = sp.Function('F')(x2, y1, y2)
Fx2 = sp.diff(F, x2); Fy1 = sp.diff(F, y1); Fy2 = sp.diff(F, y2)

# Level function f = x1 - F(x2,y1,y2) (no u-dependence since s-independent).
f = x1 - F


def X(g, k):
    gx1 = sp.diff(g, x1); gx2 = sp.diff(g, x2)
    gy1 = sp.diff(g, y1); gy2 = sp.diff(g, y2); gt = sp.diff(g, t)
    if k == 1:
        return sp.expand(gx1 + 2*y1*gt)
    if k == 2:
        return sp.expand(gx2 + 2*y2*gt)
    if k == 3:
        return sp.expand(gy1 - 2*x1*gt)
    return sp.expand(gy2 - 2*x2*gt)


A = [X(f, 1), X(f, 2), X(f, 3), X(f, 4)]
print("A =", A)
S2 = sum(a**2 for a in A)
div = X(A[0], 1) + X(A[1], 2) + X(A[2], 3) + X(A[3], 4)
ZS2 = [X(S2, 1), X(S2, 2), X(S2, 3), X(S2, 4)]
Hnum = sp.expand(div*S2 - sp.Rational(1, 2)*sum(A[i]*ZS2[i] for i in range(4)))
# Restrict to S: x1 = F (t drops out entirely for s-independent phi).
Hres = sp.expand(Hnum.subs({x1: F}))
print("Hnum|S =", Hres)
# Euclidean MSE numerator for graph x1=F over R^3(x2,y1,y2):
# (1+|gF|^2) dF - sum_{i,j} F_i F_j F_ij
g2 = Fx2**2 + Fy1**2 + Fy2**2
dF = sp.diff(Fx2, x2) + sp.diff(Fy1, y1) + sp.diff(Fy2, y2)
grad = [Fx2, Fy1, Fy2]
H2 = [[sp.diff(gi, v) for v in (x2, y1, y2)] for gi in grad]
E = sp.expand((1 + g2)*dF - sum(grad[i]*grad[j]*H2[i][j]
                                for i in range(3) for j in range(3)))
print("Eucl MSE num =", E)
ratio = sp.simplify(Hres / E)
print("ratio Hnum|S / Eucl =", ratio)
print("difference Hres - ratio*E simplifies to:", sp.simplify(Hres - ratio*E))
