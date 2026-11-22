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

# Verification of the stated theorem

Run `python verify.py` with NumPy and SymPy installed. The checker independently verifies nilpotence and singular-vector factorization, the second-moment covariance rule by symbolic monomial integration, the two-state characteristic root, a rational threshold and divergence witness, and 90 parameter/angle test settings with 10,000 Gaussian draws per setting. It reports the reference witness factors approximately 0.410124980474851 and 4.01.

The universal stability boundaries are proved analytically in `RESULT.md`. Simulations are not used as infinite proofs. The positive-probability learned-space statement uses the full support of a two-dimensional Gaussian conditional on the probe; no finite experiment purports to measure an extremely rare event reliably. No independent mathematical validation has been performed.
