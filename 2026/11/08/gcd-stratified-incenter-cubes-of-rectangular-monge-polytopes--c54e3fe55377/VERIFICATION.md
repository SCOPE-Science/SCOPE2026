---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational reproduction and analytical limits

Run `python artifacts/verify.py` from the package root (or `python verify.py` within `artifacts`). Exact combinatorial and rational calculations use the standard library; the independent floating-point linear-programming checks are run when NumPy and SciPy are installed.

The recorded exact tests check 576 pairs with `2 <= p,q <= 25`, 4390 cube-corner profiles with `2 <= p,q <= 12`, and 64 independent Frobenius-metric LP optimizations with `2 <= p,q <= 9`. The independent LP uses the true norm of the projection of a coordinate normal, and has absolute tolerance `3e-8` for its numerical comparison. The exact tests verify the gcd weight identity, monotone potential construction, all nonnegativity and adjacent Monge slacks, support/zero patterns, total mass and tangent-facet counts. Replayed output: `RECT_MONGE_INBALL_CHECKS_PASSED exact_pairs=576 corner_profiles=4390 independent_lp=64`.

The arbitrary-size theorem rests on the coupling identity, exact gcd evaluation and equality classification proved in `RESULT.md`; exhaustive checks on finite parameter rectangles alone do not establish it. Historical priority beyond inspected sources is not independently determined.
