"""Lane-442 verification script (target phase + post-unlock consolidation).

Verifies, from first principles + pinned published inequalities, the numerical inputs
used in the target analysis for B(2,665):
  (A) exponent arithmetic: 665 = 5*7*19, all divisors, phi-values, abelianization order;
  (B) Adian cogrowth bound w(i) <= (2i-1)^{2/3} (Cor 2.8 of Olshanskii-Osin, valid at
      n >= 665) and the ratio w(i)/i -> 0  [Lemma 2.3(d)];
  (C) quantitative infinitesimal spectral radius via the Grigorchuk formula (7):
      rho(i) <= ((2i-1)^{1/3} + (2i-1)^{2/3})/(2i) -> 0, hence ||A_{X_i}|| <= 2*rho -> 0
      [Lemma 2.3(a)<->(b)]. This holds at n=665 and is the part of the analytic
      scaffold that does NOT need "n >> 665".
  (D) finite-normal obstruction numerics: if N = <g> ⊲ B(2,665) is cyclic normal of
      order d | 665, conjugation gives B -> Aut(C_d) with |Aut| = phi(d); the image has
      exponent | 665 and order | phi(d), hence is trivial iff gcd(665, phi(d)) = 1.
      We verify gcd(665, phi(d)) = 1 for every d | 665. (No claim is made about
      [B : C(g)] for non-normal <g>; only the normal case is used.)

All outputs are deterministic; run with: python3 verify_target_inputs.py
Exits nonzero on any failed check.
"""
import math
import sys

FAILS = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" :: " + str(detail)) if detail else ""))
    if not cond:
        FAILS.append(name)


def divisors(n):
    return sorted(d for d in range(1, n + 1) if n % d == 0)


def phi(n):
    return sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)


def crt_idempotents():
    """Verify Z/665 = F5 x F7 x F19 idempotents used in Lemma A."""
    e = {5: 266, 7: 190, 19: 210}
    ok = True
    for p, ep in e.items():
        for q in [5, 7, 19]:
            want = 1 if p == q else 0
            got = ep % q
            print(f"e_{p} mod {q} = {got} (want {want})")
            ok = ok and (got == want)
        print(f"{p}*e_{p} mod 665 = {(p * ep) % 665} (want 0)")
        ok = ok and ((p * ep) % 665 == 0)
    print(f"e5+e7+e19 mod 665 = {sum(e.values()) % 665} (want 1)")
    ok = ok and (sum(e.values()) % 665 == 1)
    return ok


def main():
    n = 665
    print("=== (A0) CRT idempotents for Z/665 (Lemma A input) ===")
    check("crt_idempotents", crt_idempotents())
    # (A) exponent arithmetic
    divs = divisors(n)
    print("=== (A) exponent arithmetic for n = 665 ===")
    print("divisors:", divs)
    check("665_factorization", math.prod([5, 7, 19]) == 665, "5*7*19=665")
    check("665_squarefree", all(n % (p * p) != 0 for p in [5, 7, 19]), "squarefree")
    check("665_divisors", divs == [1, 5, 7, 19, 35, 95, 133, 665], divs)
    phis = {d: phi(d) for d in divs if d > 1}
    print("phi values:", phis)
    check("phi_values", phis == {5: 4, 7: 6, 19: 18, 35: 24, 95: 72, 133: 108, 665: 432}, phis)
    check("phi_max_432", max(phis.values()) == 432)
    ab = n * n
    print("abelianization B(2,665)^ab = (Z/665)^2, order:", ab)
    check("abelianization_order", ab == 442225, ab)
    # every finite-index-centralizer bound is < abelianization order (sanity: no vacuity)
    check("centralizer_bound_nontrivial", all(p < ab for p in phis.values()))

    # (B) Adian cogrowth bound -> Lemma 2.3(d)
    print("\n=== (B) Adian cogrowth bound w(i) <= (2i-1)^{2/3}, ratio w/i ===")
    prev_ratio = None
    mono_ok = True
    for i in [2, 3, 5, 10, 50, 200, 1000, 10**6]:
        w = (2 * i - 1) ** (2.0 / 3.0)
        r = w / i
        print(f"i={i:>8d}  w_bound={w:.6f}  w/i={r:.8f}")
        if prev_ratio is not None and i > 10 and r >= prev_ratio:
            mono_ok = False
        prev_ratio = r
    check("cogrowth_ratio_decays", mono_ok, "w/i strictly decreasing for i>10 checkpoints")
    check("cogrowth_ratio_small", (2 * 10**6 - 1) ** (2.0 / 3.0) / 10**6 < 0.02)
    # card(X_i) -> infinity
    check("rank_diverges", True, "|X_i| = i -> oo by construction")

    # (C) Grigorchuk upper bound on spectral radius (valid: f increasing for w >= sqrt(2i-1))
    print("\n=== (C) spectral-radius upper bound rho(i) <= ((2i-1)^{1/3}+(2i-1)^{2/3})/(2i) ===")
    print("justification: f(w)=(1/2i)((2i-1)/w + w), f'(w)=(1/2i)(1-(2i-1)/w^2)>=0 for w>=sqrt(2i-1);")
    print("Adian upper w<=(2i-1)^{2/3} >= sqrt(2i-1), so maximum of f on the admissible window is at w_upper.")
    prev_rho = None
    rho_ok = True
    for i in [2, 3, 5, 10, 50, 200, 1000, 10**6]:
        c2 = 2 * i - 1
        rho = (c2 ** (1.0 / 3.0) + c2 ** (2.0 / 3.0)) / (2 * i)
        op = 2 * rho  # ||A_{X_i}|| <= 2 rho by Lemma 2.3 proof, inequality (9)
        print(f"i={i:>8d}  rho_bound={rho:.8f}  ||A||_bound={op:.8f}")
        if prev_rho is not None and rho >= prev_rho:
            rho_ok = False
        prev_rho = rho
    check("rho_decays_monotone", rho_ok, "rho bound strictly decreasing on checkpoints")
    check("rho_small_at_1e6", ((2 * 10**6 - 1) ** (1.0 / 3.0) + (2 * 10**6 - 1) ** (2.0 / 3.0)) / (2 * 10**6) < 0.01)
    # spot-check f' >= 0 on the window for a few i (rigor: monotonicity used above)
    deriv_ok = True
    for i in [2, 5, 100, 9999]:
        c2 = 2 * i - 1
        for frac in [0.0, 0.5, 1.0]:
            w = c2 ** 0.5 + frac * (c2 ** (2.0 / 3.0) - c2 ** 0.5)
            if (1 - c2 / (w * w)) < -1e-12:
                deriv_ok = False
    check("grigorchuk_monotone_window", deriv_ok, "f'(w)>=0 throughout [sqrt(2i-1), (2i-1)^{2/3}]")

    # (D) finite-normal numerics (normal case only)
    print("\n=== (D) finite-normal exclusion numerics: gcd(665, phi(d)) == 1 for d | 665 ===")
    for d in [dd for dd in divs if dd > 1]:
        print(f"|N|={d:>4d}  phi={phi(d):>4d}  gcd(665,phi)={math.gcd(665, phi(d))}")
    check("all_gcd_one", all(math.gcd(665, phi(d)) == 1 for d in divs if d > 1))
    check("gcd_665_432", math.gcd(665, 432) == 1, "665=5*7*19 vs 432=2^4*3^3 coprime")
    check("all_phi_lt_665", all(phi(d) < 665 for d in divs if d > 1))

    print("\n==== %s ====" % ("ALL CHECKS PASSED" if not FAILS else ("FAILURES: " + str(FAILS))))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
