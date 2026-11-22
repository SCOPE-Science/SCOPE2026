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

# Verification and reproduction

The mathematical proof is in `RESULT.md`. The proof requires only compact metric Kantorovich--Rubinstein duality, the finite equal-mass assignment principle, an elementary half-integer rounding inequality, the no-section degree argument and explicit piecewise-linear constructions. The finite diagnostic does not establish the infinite result.

The file `check_wasserstein_double_cover.py` is executable with the Python 3 standard library: `python3 check_wasserstein_double_cover.py`. It uses rational arithmetic to solve each two-source optimal transport problem, checks the path closure condition and repeats 28,810 assertions for integers \(1\le m\le20\), printing `DOUBLE_COVER_W1_EXACT_RATIONAL_OK 28810`. The independent mathematical audit has not been performed.

Limits: equal-weight exactly \(m\) maps, real Lipschitz seminorm quotient, fixed metric circles, no uniform Lipschitz bounds on approximating maps.
