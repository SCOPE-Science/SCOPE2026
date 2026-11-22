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

# Verification of the scalar moment frontier

The analytic proof in `RESULT.md` is the basis for the all-parameter finding. It uses the exact row-reset distribution, strict Jensen inequality, a monotone derivative sign, and an explicit rank-one Gram calculation.

Run `python check.py` with Python 3 and no third-party dependencies. The script compares the moment identity against direct two-atom probabilities using exact fractions for integer exponents, reconstructs the three-by-two witness normal equations and error-tail parameters at rational row strengths, checks convergence toward the critical supremum, and samples the supercritical extremal function and Jensen geometry inequalities. On the reviewed package, it passed 9,048 exact-rational assertions and 232,920 finite floating-point supplementary comparisons.

Finite tests are not exhaustive over real positive exponents and do not certify novelty, infinite-domain results, or correctness by themselves. The noise model concerns fixed right-hand-side corruption and no coefficient-roundoff error. The method does not reject zero-residual row draws. Independent audit has not been performed.
