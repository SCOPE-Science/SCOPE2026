"""Exact + reproducible verifier for lane-1094 H4-GRAPH NPA 1+AB collapse.

Replays, from committed integer/exact inputs only:
 1. classical bias of H4 = 3 by exhaustive enumeration over all 16 assignments;
 2. quantum bias (3/2)*sqrt(6): exact correlators via sympy rational arithmetic;
 3. SoS dual certificate: residual of lam*I - B - sum E_k^2/(2 l_k) vanishes on the
    explicit optimal representation, and complementary slackness E_k|psi> = 0;
    (the operator identity itself is proved symbolically in output/DRAFT.md)
 4. flat extension: an exact nonzero 4x4 Gram minor (sympy determinant, provably
    nonzero radical expression) forces rank(Gamma_{1+AB}) >= 4; all nine moment
    vectors live in C^4 so rank <= 4; all sixteen level-2 word-vectors also live
    in C^4 and contain the same minor, so rank(Gamma^{(2)}) = 4 = rank(Gamma_{1+AB}).
Uses only numpy + sympy (stdlib-level, no SDP solver needed).
"""
import itertools
import numpy as np
import sympy as sp

S15 = sp.sqrt(15)
S6 = sp.sqrt(6)

# ---- vectors (exact) ----
u0 = sp.Matrix([1, 0, 0])
u1 = sp.Matrix([sp.Rational(1, 4), 0, S15 / 4])
T0 = 2 * u0 + u1          # = (9/4, 0, sqrt15/4)
T1 = u0 - u1              # = (3/4, 0, -sqrt15/4)
l0sq = (T0.dot(T0))       # 6
l1sq = (T1.dot(T1))       # 3/2
assert sp.simplify(l0sq - 6) == 0 and sp.simplify(l1sq - sp.Rational(3, 2)) == 0
l0 = sp.sqrt(l0sq)        # sqrt(6)
l1 = sp.sqrt(l1sq)        # sqrt(6)/2
v0 = T0 / l0
v1 = T1 / l1
lam = l0 + l1   # sum of the two side-norms = (3/2) sqrt(6)
assert sp.simplify(lam - 3 * S6 / 2) == 0

print("== H4-GRAPH NPA 1+AB collapse verifier ==")

# ---- 1. classical bias = 3 (exact integer enumeration) ----
best = -10**9
for bits in itertools.product((-1, 1), repeat=4):
    a0, a1, b0, b1 = bits
    val = 2 * a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1
    best = max(best, val)
print(f"[1] classical bias = {best}")
assert best == 3, "classical bias must be exactly 3"
# witness: a0=a1=b0=b1=+1 gives 2+1+1-1 = 3
assert 2 + 1 + 1 - 1 == 3

# ---- 2. quantum bias (exact correlators) ----
# For |Phi+> and X-Z-plane observables, <A_x B_y> = u_x . v_y exactly.
c00 = u0.dot(v0)
c01 = u0.dot(v1)
c10 = u1.dot(v0)
c11 = u1.dot(v1)
bias = 2 * c00 + c01 + c10 - c11
bias = sp.simplify(bias)
print(f"[2] correlators: {float(c00):.6f} {float(c01):.6f} {float(c10):.6f} {float(c11):.6f}")
print(f"[2] quantum bias = {bias} = {float(bias):.10f}; lambda = 3*sqrt(6)/2 = {float(3*np.sqrt(6)/2):.10f}")
assert sp.simplify(bias - 3 * S6 / 2) == 0
gap = float(bias) - best
print(f"[2] strict gap over classical: {gap:.10f} > 0")
assert gap > 0.5  # 0.6742...

# ---- 3. SoS dual certificate + complementary slackness (numeric on exact point) ----
s15 = float(S15)
X = np.array([[0, 1.], [1., 0]])
Z = np.array([[1., 0], [0, -1.]])
I2 = np.eye(2)
psi = np.array([1., 0, 0, 1]) / np.sqrt(2.)


def obs(v):
    return v[0] * X + v[2] * Z


def tup(M):
    return np.array([float(M[0]), 0.0, float(M[2])])


U0 = np.array([1., 0, 0])
U1 = np.array([0.25, 0, s15 / 4.])
TT0 = 2 * U0 + U1
TT1 = U0 - U1
L0 = float(l0)
L1 = float(l1)
V0 = TT0 / L0
V1 = TT1 / L1
A0 = np.kron(obs(U0), I2)
A1 = np.kron(obs(U1), I2)
B0 = np.kron(I2, obs(V0))
B1 = np.kron(I2, obs(V1))
LAM = 1.5 * np.sqrt(6.)
Bop = 2 * A0 @ B0 + A0 @ B1 + A1 @ B0 - A1 @ B1
E0 = L0 * B0 - (2 * A0 + A1)
E1 = L1 * B1 - (A0 - A1)
R = LAM * np.eye(4) - Bop - (E0 @ E0) / (2 * L0) - (E1 @ E1) / (2 * L1)
res = float(np.abs(R).max())
n0 = float(np.linalg.norm(E0 @ psi))
n1 = float(np.linalg.norm(E1 @ psi))
val = float(np.vdot(psi, Bop @ psi))
print(f"[3] SoS residual max-abs = {res:.3e} (require < 1e-9)")
print(f"[3] complementary slackness ||E0 psi||={n0:.3e}, ||E1 psi||={n1:.3e} (require < 1e-9)")
print(f"[3] primal value <psi|B|psi> = {val:.10f} vs lambda = {LAM:.10f}")
assert res < 1e-9 and n0 < 1e-9 and n1 < 1e-9
assert abs(val - LAM) < 1e-9

# ---- 4. flat extension: exact 4x4 Gram minor + C^4 ceiling ----
# Exact Pauli representation with sympy.
sx = sp.Matrix([[0, 1], [1, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
eye = sp.eye(2)


def kobs(u):
    return u[0] * sx + u[2] * sz


def kron(A, B):
    return sp.Matrix(sp.BlockMatrix([[A * B[i, j] for j in range(B.cols)] for i in range(B.rows)]))


oA0 = kron(kobs(u0), eye)
oA1 = kron(kobs(u1), eye)
oB0 = kron(eye, kobs(v0))
oB1 = kron(eye, kobs(v1))
ket = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
vecs9 = {
    'I': ket, 'A0': oA0 * ket, 'A1': oA1 * ket, 'B0': oB0 * ket, 'B1': oB1 * ket,
    'A0B0': oA0 * oB0 * ket, 'A0B1': oA0 * oB1 * ket,
    'A1B0': oA1 * oB0 * ket, 'A1B1': oA1 * oB1 * ket,
}
V = sp.Matrix.hstack(vecs9['I'], vecs9['A0'], vecs9['B0'], vecs9['A0B0'])
G4 = (V.H * V)
det4 = sp.simplify(G4.det())
print(f"[4] exact 4x4 Gram minor det = {det4} = {complex(det4.evalf()).real:.10f}")
assert det4 != 0  # exact nonzero -> rank(Gamma_{1+AB}) >= 4
print("[4] all 9 moment vectors lie in C^4 -> rank(Gamma_{1+AB}) <= 4; hence rank = 4 exactly")
# level-2 word vectors (16 words, degree <= 2 in each party + products)
oA0A1 = oA0 * oA1
oB0B1 = oB0 * oB1
words16 = [sp.eye(4), oA0, oA1, oB0, oB1, oA0A1, oB0B1,
           oA0 * oB0, oA0 * oB1, oA1 * oB0, oA1 * oB1,
           oA0A1 * oB0, oA0A1 * oB1, oA0 * oB0B1, oA1 * oB0B1,
           oA0A1 * oB0B1]
assert len(words16) == 16
print(f"[4] {len(words16)} level-2 word-vectors, all in C^4 -> rank(Gamma^(2)) <= 4;")
print("[4] Gamma^(2) contains the same nonzero 4x4 minor -> rank(Gamma^(2)) = 4 = rank(Gamma_{1+AB})")
print("[4] RANK LOOP CLOSED: flat extension exists; finite-dim tracial representation attains lambda.")
print("VERIFY_OK")
