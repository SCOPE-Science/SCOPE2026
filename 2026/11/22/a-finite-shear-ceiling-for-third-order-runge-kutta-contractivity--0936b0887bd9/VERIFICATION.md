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

# Reproducibility and verification

Run `python3 verify.py` using Python 3.9 or later; only the standard library is required. The exact rational coefficient assertions independently verify the polynomial calculus and the derivative factorization for the numerical-stepsize threshold, as well as a globally positive decomposition of the quintic derivative. Another 525 rational matrix calculations evaluate the complete third-order polynomial directly on each matrix, then compare with the nilpotent reduction. The 11,537 direct singular-norm computations supplement the analytic equivalence; no finite grid is presented as proof of universal assertions.

The code isolates the unique positive roots and threshold numerically, and tests both a non-dissipative parameter with a positive-step contraction interval and parameters past the ceiling where contraction is impossible under the proved inequality. The analytic proof in RESULT.md supplies uniqueness, all boundary cases, and the nondegenerate-fold asymptotics. `verification_output.txt` is the actual saved output from running this program. Numerical output is not an independent certification, and historical novelty requires separate human review.
