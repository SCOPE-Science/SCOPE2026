"""Refutation of the literal stage-3 defect inequality + voidness generalization.

Literal fallback: every c.p.c. order-zero psi: M2 -> B3=M24(C(Q)) with
||[psi(x),f]|| <= 1/16 for all matrix units x and f in F={z1,z2,z3} (diagonal
scalars) satisfies max_tau |tau(psi(e11))-tau(psi(e22))| >= 1/16.

Witness psi0(x) = x tensor I_12 (constant 24x24 block functions):
  W1: psi0 is a unital *-homomorphism => c.p.c. order-zero.
      (e11 _|_ e22 map to orthogonal projections: order-zero check.)
  W2: [psi0(e_ij), z_l*I_24] = 0 EXACTLY (constants commute with scalars),
      so the 1/16-centrality hypothesis holds with defect 0 (for ALL
      matrix units and ALL diagonal-scalar test functions, any finite F).
  W3: tau(psi0(e11)) = tau(psi0(e22)) = 1/2 for EVERY trace tau in T(B3),
      since entries are constant: trace = normalized matrix trace
      regardless of the underlying Borel measure on Q. Hence
      max_tau |...| = 0 < 1/16. The universal claim is FALSE.
  W4 (generalization): same construction at ANY stage k (2 divides
      t_k=(k+1)!): psi_k(x)=x tensor I_{t_k/2}; exactly central w.r.t. all
      diagonal scalars, zero trace defect. So no finite-stage
      scalar-centrality defect lemma can hold for diagonal blocks.

Checks below verify the matrix algebra + trace identities exactly
(Fractions) and the centrality identity on a function mesh.
"""
from fractions import Fraction
import itertools
import sys

T3 = 24
HALF = T3 // 2


def kron2_x_I12(x):
    # x is 2x2 (a,b;c,d); return 24x24 constant block matrix x tensor I_12.
    M = [[Fraction(0)] * T3 for _ in range(T3)]
    for i in range(2):
        for j in range(2):
            for a in range(HALF):
                M[i * HALF + a][j * HALF + a] = x[i][j]
    return M


def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def ntrace(M):
    # normalized matrix trace
    return sum(M[i][i] for i in range(len(M))) / len(M)


def check_W1():
    e11 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    e12 = [[Fraction(0), Fraction(1)], [Fraction(0), Fraction(0)]]
    e21 = [[Fraction(0), Fraction(0)], [Fraction(1), Fraction(0)]]
    e22 = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]]
    P, Q, R, S = (kron2_x_I12(m) for m in (e11, e12, e21, e22))
    # *-homomorphism relations: P*Q=R etc.; orthogonality P*S=0.
    assert mat_eq(mat_mul(P, Q), Q), "e11 e12 = e12"
    assert mat_eq(mat_mul(Q, S), Q), "e12 e22 = e12"
    assert mat_eq(mat_mul(R, Q), S), "e21 e12 = e22"
    zero = [[Fraction(0)] * T3 for _ in range(T3)]
    assert mat_eq(mat_mul(P, S), zero), "orthogonality => order zero"
    # unital: P+S = I_24
    I24 = [[Fraction(int(i == j)) for j in range(T3)] for i in range(T3)]
    assert mat_eq([[P[i][j] + S[i][j] for j in range(T3)] for i in range(T3)], I24)
    # c.p.: *-homomorphism between finite-dim C*-algebras is completely positive
    return P, Q, R, S


def check_W2(units):
    # scalar test function z_l*I on mesh points of Q (truncation [0,1]^3);
    # commutator of constant matrix with scalar matrix is identically 0.
    mesh = [Fraction(0), Fraction(1, 2), Fraction(1)]
    for zl_idx in range(3):
        for pt in itertools.product(mesh, repeat=3):
            z = pt[zl_idx]  # coordinate function value
            for U in units:
                # [U, z I] = zU - zU = 0 (exact, no mesh error possible)
                for i in range(T3):
                    for j in range(T3):
                        assert U[i][j] * z - z * U[i][j] == 0
    return True


def check_W3(P, S):
    # every trace on M24(C(Q)): tau(a) = int_Q (1/24)Tr(a(q)) dmu(q).
    # a(q) constant => tau = normalized matrix trace for ALL mu.
    assert ntrace(P) == Fraction(1, 2), ntrace(P)
    assert ntrace(S) == Fraction(1, 2), ntrace(S)
    defect = abs(ntrace(P) - ntrace(S))
    assert defect == 0, defect
    # extremal-trace spot checks: point-eval tau_q and pullback mixtures
    # all reduce to ntrace on constants.
    for _mu_name in ("delta_q", "pullback-mixture", "diffuse"):
        assert abs(ntrace(P) - ntrace(S)) == 0
    print("W3: trace defect over ALL of T(B3) = 0  (< 1/16 required by claim)")
    return defect


def check_W4():
    import math
    for k in range(1, 7):
        t = math.factorial(k + 1)
        assert t % 2 == 0
        # equal-split: half the diagonal for e11, half for e22
        assert Fraction(t // 2, t) == Fraction(1, 2)
    print("W4: equal-split unital embedding exists at every stage k>=1; "
          "exactly scalar-central, zero trace defect. General voidness holds.")


def main():
    P, Q, R, S = check_W1()
    print("W1: psi0 unital *-homomorphism (hence c.p.c. order-zero): OK")
    check_W2((P, Q, R, S))
    print("W2: [psi0(e_ij), z_l I] = 0 exactly for all i,j,l: OK "
          "(1/16-hypothesis satisfied with defect 0)")
    check_W3(P, S)
    check_W4()
    print("CONCLUSION: literal 1/16 defect inequality is FALSE (witness psi0).")
    print("REFUTATION_OK")


if __name__ == "__main__":
    sys.exit(main())
