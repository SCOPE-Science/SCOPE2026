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

# Verification

The proof calculates the first exit clocks on each mixed threshold quadrant and the forward-invariant alternating strip. The basin area is the exact sum of squared interval widths. Piecewise differentiation at every \(\lambda_m=2^{-1/m}\) proves strict cusp maxima. An exact rescaling of the last geometric bin yields the \(3/4\) limit. None of these infinite claims is inferred from simulations.

Run `python verify.py` with Python 3 (standard library only). It checks rational bin partitions and direct finite-orbit classifications, as well as the rational value at the first minimum. Tested cases are finite and are corroboration, not an exhaustive parameter sweep. No external independent audit has been performed.
