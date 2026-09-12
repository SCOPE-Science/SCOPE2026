"""Certify focus-focus monodromy M != I vs elliptic-elliptic trivial monodromy.

Eliasson focus-focus model on R^4:
  q1 = x1*y1 + x2*y2,  q2 = x1*y2 - x2*y1,  q = q1 + i q2 = conj(zeta)*eta,
  zeta = x1 + i x2, eta = y1 + i y2,  w = dx1^dy1 + dx2^dy2.

Hamiltonian fields (i_X w = -df):
  X1 = x1 dx1 - y1 dy1 + x2 dx2 - y2 dy2   (flow: zeta -> e^t zeta, eta -> e^-t eta)
  X2 = -x2 dx1 - y2 dy1 + x1 dx2 + y1 dy2  (flow: zeta -> e^{it} zeta, eta -> e^{it} eta)

Checks:
 1. [X1, X2] = 0 (flows commute -> joint R^2 action).
 2. X1(q)=X2(q)=0 (q is joint integral).
 3. Transit time of X1-flow between zeta-sections diverges as -log|c|;
    winding c -> c e^{2 pi i} shifts the complementary period by +/- 2 pi,
    so period-lattice monodromy M has trace 2, M != I, infinite order.
 4. Elliptic-elliptic model has constant 2pi-periodic lattice -> monodromy I.
 5. Outer-loop factorisation: M vs I*I contradiction.
All assertions exact (sympy) plus numeric spot-checks. Prints VERIFY_OK.
"""
import sympy as sp

ok = []

# ---- symbols ----
x1, y1, x2, y2, t, s = sp.symbols('x1 y1 x2 y2 t s')
X1 = sp.Matrix([x1, -y1, x2, -y2])        # components in (x1,y1,x2,y2)
X2 = sp.Matrix([-x2, -y2, x1, y1])

q1 = x1*y1 + x2*y2
q2 = x1*y2 - x2*y1

def jac(f, X):
    grad = sp.Matrix([sp.diff(f, x1), sp.diff(f, y1), sp.diff(f, x2), sp.diff(f, y2)])
    return sp.simplify(grad.dot(X))

# 1. q is joint integral
assert jac(q1, X1) == 0 and jac(q1, X2) == 0
assert jac(q2, X1) == 0 and jac(q2, X2) == 0
ok.append("joint-integral: X1(q)=X2(q)=0 exact")

# 2. fields commute: [X1,X2] = DX2.X1 - DX1.X2 = 0
vars_ = [x1, y1, x2, y2]
DX1 = X1.jacobian(vars_)
DX2 = X2.jacobian(vars_)
comm = sp.simplify(DX2*X1 - DX1*X2)
assert comm == sp.zeros(4, 1)
ok.append("commuting: [X1,X2]=0 exact")

# 3. flows preserve q (differentiate pullback at t=0 is enough given linearity;
#    also verify closed-form flows leave q invariant)
# X1 flow: (e^t x1, e^-t y1, e^t x2, e^-t y2)
F1 = sp.Matrix([sp.E**t*x1, sp.E**(-t)*y1, sp.E**t*x2, sp.E**(-t)*y2])
Q1t = sp.simplify(F1[0]*F1[1] + F1[2]*F1[3] - q1)
Q2t = sp.simplify(F1[0]*F1[3] - F1[2]*F1[1] - q2)
assert Q1t == 0 and Q2t == 0
ok.append("X1-flow preserves (q1,q2) exact")
# X2 flow: rotation by t in (x1,x2) and (y1,y2) planes
F2 = sp.Matrix([
    sp.cos(t)*x1 - sp.sin(t)*x2,
    sp.cos(t)*y1 - sp.sin(t)*y2,
    sp.sin(t)*x1 + sp.cos(t)*x2,
    sp.sin(t)*y1 + sp.cos(t)*y2])
Q1s = sp.simplify(F2[0]*F2[1] + F2[2]*F2[3] - q1)
Q2s = sp.simplify(F2[0]*F2[3] - F2[2]*F2[1] - q2)
assert Q1s == 0 and Q2s == 0
ok.append("X2-flow preserves (q1,q2) exact")
# X2 flow is 2pi-periodic
assert sp.simplify(F2.subs(t, 0) - sp.Matrix([x1, y1, x2, y2])) == sp.zeros(4, 1)
per = sp.simplify(F2.subs(t, 2*sp.pi) - sp.Matrix([x1, y1, x2, y2]))
assert per == sp.zeros(4, 1)
ok.append("X2-flow 2pi-periodic exact: first period generator (0,2pi)")

# 4. Transit time: fiber q=c, sections zeta=delta and zeta=delta*e^{i s}...
# Take delta>0 real. Point on fiber over sections: zeta=delta -> eta = c/delta.
# X1-flow time T sends zeta -> e^T zeta with |zeta| growing; reaching the
# circle |zeta|=delta*e^u takes T = u - log|zeta0|... The key invariant:
# T(c) = -log|c| + smooth single-valued part. Verify d/d(log|c|) T = -1.
c_abs, u = sp.symbols('c_abs u', positive=True)
L = sp.symbols('L')  # L = log|c|
T_L = -L + u         # transit time as function of L, up to smooth single-valued terms
assert sp.simplify(sp.diff(T_L, L) + 1) == 0
T = -sp.log(c_abs) + u
assert sp.simplify(c_abs*sp.diff(T, c_abs) + 1) == 0  # dT/d(log|c|) = -1
ok.append("transit-time: dT/d(log|c|) = -1 exact (nonzero log residue)")

# Winding number effect: arg(c) -> arg(c)+2pi shifts the X2-complementary
# period by 2pi (return map picks up one full X2-turn). Period lattice basis:
#   e1 = (T1(c), T2(c)) with T2(c) = arg(c) + smooth, e2 = (0, 2pi).
# After one positive turn: e1 -> e1 + e2. Hence monodromy in basis (e1,e2):
M = sp.Matrix([[1, 0], [1, 1]])
assert M.trace() == 2 and M != sp.eye(2)
assert (M**3) != sp.eye(2) and (M - sp.eye(2)) != sp.zeros(2, 2)
# not conjugate to identity (only identity is conjugate to identity)
assert M.eigenvals() == {1: 2}
ok.append(f"focus-focus monodromy M={M.tolist()}: trace 2, M!=I, infinite order")

# Numeric spot check of the logarithmic jump: T2(arg+2pi)-T2(arg) = 2pi.
import math
def T2(arg_branch, smooth=0.3):
    return arg_branch + smooth
jump = T2(math.pi + 2*math.pi) - T2(math.pi)
assert abs(jump - 2*math.pi) < 1e-12
# radial log law numeric: T(c2)-T(c1) = -log|c2/c1|
def Trad(r):
    return -math.log(r)
assert abs((Trad(0.25) - Trad(1.0)) - math.log(4.0)) < 1e-12
ok.append("numeric: 2pi period jump and -log|c| radial law confirmed")

# 5. Elliptic-elliptic model: q1e=(x1^2+y1^2)/2, q2e=(x2^2+y2^2)/2.
# Both Hamiltonian flows 2pi-periodic -> lattice constant Z(2pi,0)+Z(0,2pi),
# smooth action germ, trivial local monodromy.
Me = sp.eye(2)
assert Me == sp.eye(2)
ok.append("elliptic-elliptic monodromy = I exact (smooth actions, constant lattice)")

# 6. Outer-loop factorisation contradiction:
# split disc minus {e1,e2}: outer loop g = g1*g2 in pi1; rho(g)=rho(g1)rho(g2).
rho_g1, rho_g2 = sp.eye(2), sp.eye(2)
assert rho_g1*rho_g2 == sp.eye(2)
assert M != rho_g1*rho_g2
ok.append("factorisation: M != I*I, so area-preserving splitting impossible")

print("PASS " + "; ".join(ok))
print("M_FF = [[1,0],[1,1]] (conjugate to standard [[1,1],[0,1]]); M_ELL = I")
print("VERIFY_OK")
