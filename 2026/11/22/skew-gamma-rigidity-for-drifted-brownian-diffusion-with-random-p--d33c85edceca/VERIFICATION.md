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

The stationary claim was checked analytically by deriving the exponential-time drift-diffusion transform, establishing the gamma-tail comparison, proving the sign-balance beta-CDF identity, checking beta-integral sufficiency and using the Hausdorff moment theorem for contraction-law uniqueness. Boundary cases with a unit shape are addressed separately.

For finite reproducibility, execute `python3 verify.py` beside this file. The checker uses built-in exact rational arithmetic and verifies 3,204 moment and beta-CDF assertions; its observed result is `PASS 3204 exact rational moment and beta-CDF checks`. These checks are finite tests, not a substitute for the proof of all positive real shape parameters or all initial laws.

No independent mathematical audit has been performed. Historical priority with respect to unlocated general perpetuity classifications remains a residual risk.
