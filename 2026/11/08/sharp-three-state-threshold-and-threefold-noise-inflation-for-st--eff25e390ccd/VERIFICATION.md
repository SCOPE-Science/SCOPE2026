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
# Verification record

From the embedded package directory, run `python3 verify.py`. Python standard library only; no data downloads, network or environment-specific paths are required.

The recorded run reports **911 exact-rational assertions passed** across 75 parameter pairs. Checks include stochastic transition sums, invariance, the stationary mass formulas, exact mean and variance, the four-state trapping set, reachability of the claimed recurrent support, the exact example and approaching the strict sharp supremum. All parameter-wide claims are proved analytically in `RESULT.md`; no finite test is used as an infinite certificate.

Scientific limitations: fixed unit lattice, exact pre-rounding arithmetic, i.i.d. conditional rounding, scalar affine iteration and the specified multiplier range. Independent scientific audit not performed.
