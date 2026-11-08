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

# Reproducibility and verification

The theorem applies to pure homogeneous harmonic quadratics on a uniformly measured round sphere. Its analytical proof derives invariant orthogonal decomposition, the three truncated spherical moment quotients, and exact antiderivative formulas for all three pairwise eigenvalue differences. These identities hold for every integer \(d\ge3\) and every \(0<a<1\), without relying on numerical extrapolation.

Install `requirements.txt` into a compatible Python environment and run `python check_polar.py`. The checker recomputes the three normalized quotients using 60-digit direct numerical integration, compares each with the analytic gap identity in 84 settings, and checks positivity and ordering. Its observed output was `POLAR_CAP_CHECKS_PASS 420` when executed from the packaged directory. All numerical evaluations are finite consistency checks and are not independent or exhaustive mathematical certification.

No independent audit, external mathematical validation, precision guarantee for other numerical inputs, or noisy-data stability analysis has been performed.
