"""Bounded PRESET_FALLBACK attempt diagnostic for lane-684 (post-reveal).

Fallback exact success criterion requires:
  (i)   quiver + Kupisch data + canonical M0 of A=A^(2)(5;3,3,3,3,3),
  (ii)  full extended word w (len<=6) with each exchange triangle, the single
        reduction-detour datum naming the intermediate 2-term silting complex
        outside the 2-cluster-tilting subcategory, and the return isomorphism,
  (iii) complete integer K0-monodromy M(w) with char poly, one non-cyclotomic
        factor, and certified rho>1 lower bound.

This script completes what is honestly computable without the reduction machine:
  (i) inventory (reuses probe_hom.py conventions) + Cartan matrix (exact, det=1);
  Coxeter matrix Phi = -C^{-T} C, its palindromic degree-12 char poly, and a
  NUMERIC (uncertified, numpy) spectral-radius estimate ~1.345.

CRITICAL HONESTY NOTE (why this does NOT satisfy the fallback):
  The Coxeter matrix is the CONFINED-loop invariant (AR translation on K0 of
  proj A). The audit plan and topic state confined loops are ENTIRELY OUT OF
  SCOPE for this record. Phi is NOT the K0-monodromy M(w) of any extended
  silting-detour word, so its char poly / numeric radius cannot substitute for
  (ii)-(iii). Steps (ii)-(iii) remain blocked: no reduction presilting P, no
  exchange triangles for the detour, no return isomorphism, hence no certified
  M(w) was produced. This diagnostic is logged as the bounded fallback attempt
  supporting ATTEMPTED_AND_BLOCKED, not as a partial certificate.
Stdlib + sympy + numpy display only; exact parts use sympy Rational.
"""
import sympy as sp

N = 5
ELL = [3] * 5
KEPT = [(a, b) for a in range(N) for b in range(N)
        if a >= b and (a - b + 1) <= ELL[a]]
IDX = {v: i for i, v in enumerate(KEPT)}
LAMS = [(a, b, c) for a in range(N) for b in range(N) for c in range(N)
        if a >= b >= c and (a - c + 1) <= ELL[a]]


def path_exists(v, u):
    if u[0] < v[0] or u[1] < v[1]:
        return False
    seen = {v}
    stack = [v]
    while stack:
        p = stack.pop()
        if p == u:
            return True
        for q in [(p[0] + 1, p[1]), (p[0], p[1] + 1)]:
            if q in IDX and q not in seen and q[0] <= u[0] and q[1] <= u[1]:
                seen.add(q)
                stack.append(q)
    return False


def main():
    print(f"step (i): |K0 proj| = {len(KEPT)}, M0 summands = {len(LAMS)}, "
          f"Kupisch = {ELL}")
    C = sp.Matrix([[1 if path_exists(v, u) else 0
                    for v in KEPT] for u in KEPT])
    print(f"Cartan det = {C.det()} (exact)")
    Phi = (-C.T * C.inv())
    cp = Phi.charpoly()
    print(f"Coxeter charpoly (exact): {cp.as_expr()}")
    print("palindromic coefficients: "
          f"{[cp.nth(i) == cp.nth(12 - i) for i in range(13)]}")
    try:
        import numpy as np
        coef = [1, 1, -2, -2, 1, 1, 0, 1, 1, 0, -2, -2, 1, 1]
        r = np.roots(coef)
        print(f"Coxeter numeric spectral-radius estimate (UNCERTIFIED, "
              f"diagnostic only): {max(abs(x) for x in r):.6f}")
    except ImportError:
        print("numpy unavailable; numeric estimate skipped")
    print("step (ii): BLOCKED -- no reduction datum / exchange triangles / "
          "return iso fixed (see WORKLOG).")
    print("step (iii): NOT PRODUCED -- no M(w), no detour char poly, no "
          "certified rho>1 bound. Coxeter data above is confined-scope and "
          "does not substitute.")


if __name__ == "__main__":
    main()
