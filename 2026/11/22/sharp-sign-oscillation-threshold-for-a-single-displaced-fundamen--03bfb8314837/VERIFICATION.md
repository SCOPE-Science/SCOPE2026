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

# Verification and reproducibility

The proof is fully analytic and self-contained in `RESULT.md`. Exact computations are the frequency-projection ratio, the positive dual test, and the cosine coefficients of the Poisson-kernel difference. The latter decay quadratically and hence provide a uniformly convergent series.

Run `python CHECK.py` with Python 3 and no third-party packages. Expected output includes `CHECK_OK supplementary_assertions= 344`. This finite check tests four interior parameters, 41 grid points each, and the explicit Fourier tail bound; it cannot substitute for the all-parameter analytical proof. The critical endpoint is proved by a strict positive-weight integral, not by floating-point proximity.

Limitations: only \(0<\alpha<1\) with one replaced fundamental and all unshifted integer harmonics at least two; no optimal assertion on arbitrary perturbed frequency sequences or interval lengths. Independent audit has not been performed.
