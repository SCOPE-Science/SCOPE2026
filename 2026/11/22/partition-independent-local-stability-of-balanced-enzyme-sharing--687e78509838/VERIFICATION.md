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

# Verification and boundaries

The proof is analytic and self-contained. The exact central-difference comparison implemented in `checker.py` verifies the block Jacobian for \(126\) rational balanced settings with \(20{,}160\) elementwise comparisons. This is a finite consistency check, not a verification of every positive real parameter or partition; these are covered by the spectral inequality in the proof.

The zero eigenvalue due to total substrate conservation is present in the full reduced \(2n\)-dimensional coordinates, but absent from the tangent space of the fixed conservation class. No independent review was performed. The conclusion is local exponential stability, not global convergence.

Run `python checker.py` using Python 3 standard library only.
