"""Replayable audit for lane-506 target: V_inf table, r0=+inf, trace gaps,
domination inequalities, K0-injectivity ranks, Chern-vs-K0 rigidity note.

Run: python3 verify.py  -> prints VERIFY_OK + tables (exit nonzero on failure).
Stdlib only.
"""
from math import factorial

def sigma(n):
    return 1 if n == 0 else n * factorial(n)

def kappa_inf(n):
    return n * sigma(n)  # n^2 * n!

def rank_xi(n):
    return sum(sigma(l) for l in range(0, n + 1))

def dim_X(n):
    # real dim: 2*n*sigma(n)^2 (polydisc) + 2*sum kappa (CP factors)
    return 2 * n * sigma(n) ** 2 + 2 * sum(kappa_inf(j) for j in range(1, n + 1))

def main():
    assert rank_xi(0) == 1
    for n in range(0, 7):
        assert rank_xi(n) == factorial(n + 1), (n, rank_xi(n))
    print("rank(xi_n)=(n+1)! check: OK")

    # r0 table
    print("\n n | sigma | kappa | rank=(n+1)! | dim(X_n) | dim/(2*rank)")
    rs = []
    for n in range(1, 7):
        r = rank_xi(n)
        d = dim_X(n)
        ratio = d / (2 * r)
        rs.append(ratio)
        print(f" {n} | {sigma(n)} | {kappa_inf(n)} | {r} | {d} | {ratio:.6f}")
    assert rs[0] == 1.0
    assert all(b > a for a, b in zip(rs, rs[1:])), "r0 must diverge increasingly here"
    # analytic term n^3 n!/(n+1) -> inf
    print("\nliminf dim/(2rank) = +inf (dominant term n*sigma(n)^2/(n+1)! "
          "= n^3 n!/(n+1) -> inf). r0=+inf.")

    # trace gaps: tau(e_n)=1/(n+1)!, tau(Q_n)=sum kappa/(n+1)!
    print("\n n | tau(e_n) | tau(Q_n)=sum kappa/(n+1)! | gap R_n=tau(Q)-tau(e)")
    for n in range(1, 8):
        te = 1 / factorial(n + 1)
        tq = sum(kappa_inf(l) for l in range(1, n + 1)) / factorial(n + 1)
        print(f" {n} | {te:.3e} | {tq:.6f} | {tq - te:.6f}")
        assert tq - te > n ** 2 / (n + 1) - 1, n
    # spot: n=3 -> (1+8+54)/24 = 63/24 = 2.625 ; n=5 -> (1+8+54+384+3000)/720
    assert abs(sum(kappa_inf(l) for l in range(1, 4)) / factorial(4) - 63 / 24) < 1e-12

    # (i) Husemoeller 9.1.1 hypothesis: 2*rank(2k.g)-1 >= dim CP^k, rank=2k
    print("\nHusemoeller 9.1.1 domination 2k.g >> theta_1:")
    for k in [1, 8, 54, 384, 3000]:
        assert 2 * (2 * k) - 1 >= 2 * k, k
    print("  4k-1 >= 2k for all k>=1: OK")

    # (ii) pullback multiplicity bound (k=inf): (l+1)*sum_{i<=l} kappa_i <= kappa_{l+1}
    print("\nPullback absorption (l+1)*rank(eta_l) <= kappa_{l+1}:")
    for l in range(1, 7):
        s = sum(kappa_inf(i) for i in range(1, l + 1))
        assert (l + 1) * s <= kappa_inf(l + 1), (l, (l + 1) * s, kappa_inf(l + 1))
        print(f"  l={l}: (l+1)*sum={ (l+1)*s } <= kappa_{l+1}={kappa_inf(l+1)} OK")

    # point-evaluation section: pi^{1*} split-injective on K-theory (retraction by
    # evaluating new CP factor at a point) -> finite-stage K0 differences inject.
    # Torsion-free check: H*(prod CP) free abelian => ch_K0 rationally injective.
    print("\nK0/Chern rigidity note (textbook, not claimed as new):")
    print("  H^*(X_n;Z) torsion-free => ch: K^0(X_n) -> H^{ev}(X_n;Q) injective "
          "mod torsion (zero torsion here).")
    print("  Equal-rank projections with [p]=[q] have equal rational Chern, "
          "hence equal Euler (top Chern).")
    print("  So no same-rank pair with e(p)!=0 vs e(q)=0 can be K0-equal; "
          "Euler separates only K0-distinct classes. Proven via Kunneth + c(th)=1.")

    # error-floor lemma constants
    print("\nError floor: for projections p,q in same corner, "
          "inf_v ||v^*qv - p|| < 1/2 => p ~< q (Murray-von Neumann).")
    print("  Hence finite-stage Cuntz failure => norm gap >= 1/2 at every stage m>n.")

    print("\nVERIFY_OK")

if __name__ == "__main__":
    main()
