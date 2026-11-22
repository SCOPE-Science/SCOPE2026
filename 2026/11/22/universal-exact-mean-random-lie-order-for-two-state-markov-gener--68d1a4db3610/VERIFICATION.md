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

The analytic proof establishes the full two-state exactness identity, uniqueness of the calibrating mixture for noncommuting generators, strict positivity, fixed-step finite-horizon variance, and a three-state obstruction for every positive step. This is not an independently audited result.

The standalone `verify.py` requires only Python 3 and its standard library. Run `python verify.py`. A successful execution gives `VERIFIED numerical_assertions= 448` and an example of the calibrated probability. The code constructs rate matrices independently from the affine proof, compares full transition matrices, enumerates all order strings for up to eight steps, and checks the independent two-state mean/variance formula and a positive three-state trace gap. Finite floating-point tests are supplementary, not a proof over all rates, steps or trajectories.

The quoted asymptotic is at fixed positive time with \(n=T/h\) an integer. Numerical checks do not cover arbitrarily small or large rates because finite precision can lose cancellation. The impossibility statement concerns the stated three-state pair; it makes no claim about every higher-state pair.
