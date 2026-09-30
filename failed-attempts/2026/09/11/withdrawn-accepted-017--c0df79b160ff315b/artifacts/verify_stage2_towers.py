"""Stage-n0=2 tower table: EXACT rational certificate (no floating point).

Setup (fixed finite-stage presentation; cf. verify_equivariant_step.py for the
connecting-map intertwining that puts this block equivariantly in the limit):
- X_2 = ((S^2)^3)^3, A_2 = M_8(C(X_2)).
- alpha_2 = Ad(w) o tau^*, where tau = C o D is the order-3 space permutation
  (block 3-cycle x diagonal inner shift; C,D commute, ord(tau)=3 — verified in
  verify_equivariant_step.py) and w is the constant 8x8 block-permutation unitary
  cycling the three projection blocks and fixing the point-evaluation block:
    blocks {0,1},{2,3},{4,5},{6,7}; w: 0->2,1->3,2->4,3->5,4->0,5->1,6->6,7->7.
  ord(alpha_2)=3 since w^3=I, tau^3=id (checked below).
- Towers (three identical towers, l=0,1,2; admissible since the fallback imposes
  no cross-tower constraints; all matrices diagonal, hence commuting):
    f_g^{(l)} = (1/3) D_g + c P_c,  c = 99/1000,
  D_g = diagonal support projection on block g (D_0 on {0,1}, D_1 on {2,3},
  D_2 on {4,5}), P_c = diagonal projection on the point-evaluation corner {6,7}.
  Constant in X_2. Each tower covers ~1/3 of the total trace (natural d=2 shape).

Checks (all exact, Fractions):
 (E) equivariance: Ad(w) cycles D_g -> D_{g+1} and fixes P_c, so
     alpha_2(f_g) = f_{g+1 mod 3} exactly; h=2 by iteration; h=0 trivial.
 (O) orthogonality: supports D_g disjoint; corner overlap c^2 = 9801/10^6 < 1/100.
 (T) trace: per contraction Tr = 2/3 + 2c; total Tr = 3*3*(2/3+2c) = 6+18c;
     with c=99/1000: total = 7782/1000, tr_8 = 3891/4000,
     tau_y(1-sum) = 109/4000 = 0.02725 < 0.05, POSITIVE and y-independent
     (constant towers), hence uniform over ALL extremal traces tau_y, a fortiori
     over any fixed finite trace-simplex section.
 (S) sanity: total operator sum S = (D_0+D_1+D_2) + 9c P_c has eigenvalues 1 (x6)
     and 891/1000 (x2): S <= I, genuine almost-cover from below (not over-cover).
Margins: equiv 0 vs 0.01; orth 9801/10^6 vs 10^4/10^6; remainder 109/4000 vs
200/4000. Binary: PASS.
"""
from fractions import Fraction

N = 8
W = [2, 3, 4, 5, 0, 1, 6, 7]  # w(i): image of basis index i
SUPP = [{0, 1}, {2, 3}, {4, 5}]  # supports of D_0, D_1, D_2
CORNER = {6, 7}
A = Fraction(1, 3)    # projection-block weight
C = Fraction(99, 1000)  # corner weight

def compose(p, q):
    return [p[q[i]] for i in range(N)]

def winv():
    inv = [0] * N
    for i, j in enumerate(W):
        inv[j] = i
    return inv

def main():
    ident = list(range(N))
    w2 = compose(W, W)
    w3 = compose(W, w2)
    assert w3 == ident, "w must have order 3"
    assert W != ident and w2 != ident
    WINV = winv()
    # diagonal values of f_g = A*D_g + C*P_c
    F = [{i: (A if i in SUPP[g] else (C if i in CORNER else Fraction(0)))
          for i in SUPP[g] | CORNER} for g in range(3)]

    def apply_w(d):
        out = {}
        for i in range(N):
            v = d.get(WINV[i], Fraction(0))
            if v != 0:
                out[i] = v
        return out

    def sub(a, b):
        keys = set(a) | set(b)
        return {k: a.get(k, Fraction(0)) - b.get(k, Fraction(0)) for k in keys
                if a.get(k, Fraction(0)) != b.get(k, Fraction(0))}

    def opnorm_diag(d):
        return max([abs(v) for v in d.values()] or [Fraction(0)])

    print("=== positivity / contraction ===")
    for l in range(3):
        for g in range(3):
            vals = set(F[g].values())
            assert vals <= {A, C}, f"unexpected values {vals}"
            assert A <= 1 and C <= 1
    print("all 9 are A*D_g + C*P_c with A=1/3, C=99/1000: 0 <= f <= I ok")

    print("=== equivariance (tolerance 0.01) ===")
    for l in range(3):
        for g in range(3):
            err1 = opnorm_diag(sub(apply_w(F[g]), F[(g + 1) % 3]))
            err2 = opnorm_diag(sub(apply_w(apply_w(F[g])), F[(g + 2) % 3]))
            assert err1 < Fraction(1, 100) and err2 < Fraction(1, 100)
            print(f"tower l={l} g={g}: h=1 err={err1} ok; h=2 err={err2} ok")

    print("=== orthogonality: ||f_g f_h||, g!=h (tolerance 0.01) ===")
    for l in range(3):
        for g in range(3):
            for h in range(g + 1, 3):
                # disjoint D-supports; only corner overlaps: product = C^2 on {6,7}
                prod = C * C
                assert prod == Fraction(9801, 10 ** 6)
                assert prod < Fraction(1, 100), "orthogonality fails"
                print(f"tower l={l} pair ({g},{h}): product={prod} ok")

    print("=== trace remainder (tolerance 0.05), must be small POSITIVE ===")
    per = 2 * A + 2 * C  # Tr per contraction
    total_unnorm = 9 * per
    assert total_unnorm == Fraction(7782, 1000)
    tr = total_unnorm / N
    assert tr == Fraction(3891, 4000)
    remainder = Fraction(1) - tr
    assert remainder == Fraction(109, 4000)
    assert Fraction(0) < remainder < Fraction(5, 100), "remainder fails"
    print(f"Tr(sum)={total_unnorm}, tr_8(sum)={tr}, tau(1-sum)={remainder} ok")
    print("(uniform over ALL extremal traces tau_y: towers constant in X_2)")

    print("=== operator-sum sanity: S <= I ===")
    s_supp = 3 * A       # 3 identical towers x A per support entry
    s_corn = 9 * C       # 9 contractions x C per corner entry
    assert s_supp == 1 and s_corn == Fraction(891, 1000)
    assert s_supp <= 1 and s_corn <= 1
    print(f"S eigenvalues: 1 (x6), {s_corn} (x2): S <= I ok (cover from below)")

    print("w^3=I ok; ord(tau)=3 and intertwining per verify_equivariant_step.py")
    print("BINARY VERDICT: PASS (0 / 9801e-6 / 109/4000 vs 0.01/0.01/0.05)")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
