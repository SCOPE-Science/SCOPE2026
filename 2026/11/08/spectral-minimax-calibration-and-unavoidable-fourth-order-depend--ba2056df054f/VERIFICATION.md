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

Run `python verify.py` with Python 3.9+ using only the standard library. The script reports its check count and exits nonzero on a discrepancy.

Verification carried out: scalar variance from stationary second-moment recursion; scalar fourth cumulant from a separate stationary fourth-moment recursion; cross-mode square covariance from a fourth-order two-mode recursion; exhaustive finite-prefix Bernoulli variance identities and exact infinite-tail variance; and a numerical grid sanity check of the minimax ordering probability. See `checks.txt` for the recorded clean run.

The exact-rational calculations cover representative fractions for step, contraction and ordering probability; they are not an exhaustive proof over a continuum. The proof in RESULT.md provides the all-parameter argument via contraction, conditional Gaussianity, geometric-series identities and strict monotonicity of the calibration function. No independent validation has been performed.
