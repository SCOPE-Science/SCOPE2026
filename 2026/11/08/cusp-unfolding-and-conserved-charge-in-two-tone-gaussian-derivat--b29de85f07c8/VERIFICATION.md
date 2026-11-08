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

The analytic proof is supplied in `RESULT.md`. The standalone Python 3 `CHECK.py` requires only the standard library. Invoke `python CHECK.py`; its successful terminal marker is `ALL_CUSP_ZERO_CHECKS_PASSED`.

The checker independently integrates the defining transform for several window orders, verifies all calculated zero counts and charge sums in 52 noncritical parameter regimes, and checks fold conditions and the cubic cusp coefficient. Numerical integration does not prove the all-orders claim; the closed-form Gaussian Fourier transform, monotonicity proof, and local degree arguments establish the unrestricted theorem. No independent audit was conducted.
