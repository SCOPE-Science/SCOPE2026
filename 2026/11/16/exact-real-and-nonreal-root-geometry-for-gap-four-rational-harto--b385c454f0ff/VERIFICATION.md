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
# Reproducibility and limits

The complete proof is in `RESULT.md`. Run `python3 CHECK.py` after installing the dependencies from `requirements.txt`. The script establishes the displayed finite-sum coefficient formulas symbolically for all integer \(h\ge0\); verifies the reduced-polynomial sign identities as polynomial identities; independently reconstructs the coefficients from the published tent weights at 42 parameter values; performs exact real-root counts on the corresponding reduced quartics; and numerically inspects representative full eight-root configurations. At preparation, the checker passed **694 assertions**.

The proof for all admissible denominators is analytical: exact finite sums, Descartes' rule of signs, and the known Fejér-product boundary positivity theorem. The finite computational tests are additional consistency checks, not a substitute for the infinite argument. The investigation does not certify publication priority against all possible historical or unpublished sources; independent mathematical auditing has not been performed.
