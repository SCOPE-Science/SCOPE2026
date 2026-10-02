"""Exact bifurcation data for f_t = A_b o S_t (symbolic + numeric).

Reproduces the emergent threshold theorem of output/DRAFT.md:
persistent fixed point p2, exact determinant identity, transverse
eigenvalue-1 crossing at t* = (sqrt(3)-1)/(4*pi), closed-form spectrum,
t_c <= t*, weak-multiplier slope -2*pi*sqrt(3).
Run: python3 bifurc.py
Requires: sympy, numpy.
"""
import sympy as sp
import numpy as np

A = sp.Matrix([[3, 1, 0], [1, 1, 1], [0, 1, 1]])
s = sp.symbols('s')
print("A symmetric:", A == A.T)
print("det A:", A.det())

for (c2, c3) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    DS = sp.Matrix([[1, s * c2, 0], [0, 1, s * c3], [0, 0, 1]])
    M = A * DS
    d = sp.expand((M - sp.eye(3)).det())
    print(f"class (c2,c3)=({c2:+d},{c3:+d}): det(M-I) = {d}", end="")
    try:
        roots = sp.solve(d, s)
        print(f"  roots: {roots}")
    except Exception as e:
        print(f"  solve failed: {e}")

DS = sp.Matrix([[1, s, 0], [0, 1, -s], [0, 0, 1]])
M = A * DS
lam = sp.symbols('lam')
print("charpoly p2-class:", sp.expand((M - lam * sp.eye(3)).det()))

An = np.array([[3., 1, 0], [1, 1, 1], [0, 1, 1]])
w, Q = np.linalg.eigh(An)
print("eigvals A:", w)
print("Q orthogonality err:", np.abs(Q @ Q.T - np.eye(3)).max())
t_star = (np.sqrt(3) - 1) / (4 * np.pi)
print("t* =", t_star)

p2 = np.array([0.5, 0.0, 0.5])
print("A p2 - p2 =", An @ p2 - p2)
for t in [0.0, 0.02, 0.04, 0.05, 0.055, 0.057, 0.058, 0.0582, t_star]:
    s2 = 4 * np.pi * t
    DS = np.array([[1, s2, 0], [0, 1, -s2], [0, 0, 1]])
    Mm = An @ DS
    ev = np.linalg.eigvals(Mm)
    print(f"t={t:.6f} s={s2:.6f} |eig|={np.sort(np.abs(ev))} "
          f"det(M-I)={np.linalg.det(Mm - np.eye(3)):.6f}")

t = 0.03
St = lambda x: np.mod(np.array([
    x[0] + 2 * t * np.sin(2 * np.pi * x[1]),
    x[1] + 2 * t * np.sin(2 * np.pi * x[2]),
    x[2]]), 1)
ft = lambda x: np.mod(An @ St(x), 1)
for cand in [(0, 0, 0), (0.5, 0, 0), (0, 0, 0.5), (0.5, 0, 0.5),
              (0, 0.5, 0), (0.5, 0.5, 0.5)]:
    x = np.array(cand, float)
    print(cand, "f_t(x)-x mod 1 =", np.mod(ft(x) - x, 1).round(6))

# Slope of weak multiplier at crossing via left/right eigenvectors.
s_star = float(np.sqrt(3) - 1)
Mc = np.array([[3, 3 * s_star + 1, -s_star],
               [1, s_star + 1, 1 - s_star], [0, 1, 1 - s_star]])
Mp = np.array([[0., 3, -1], [0, 1, -1], [0, 0, -1]])
w_, V = np.linalg.eig(Mc)
W_ = np.linalg.eig(Mc.T)
i = np.argmin(np.abs(w_ - 1))
j = np.argmin(np.abs(W_ - 1))
v = V[:, i]
u = W_[1][:, j]
slope_ds = (u @ Mp @ v) / (u @ v)
print("d mu/ds =", slope_ds, " d mu/dt =", 4 * np.pi * slope_ds)
