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

The analytic evidence is contained in `RESULT.md`: the Zak multiplier formula, Jacobi product nonzero-factor analysis, exact coordinate-cover equivalence, explicit product bounds, and compactness-plus-positive-Hessian proof for the planar collision coefficient. These are the critical universal steps. The ordinary Python 3 standard-library program `verify_gaussian.py` provides finite supplementary checks and must not be interpreted as proving the global minimum, the infinite product, or novelty.

Reproduce from the extracted package with `python3 verify_gaussian.py`. It evaluates the Zak series on a symmetric truncation radius 35, checks the exact derivative product against the truncated series at four widths, and compares twelve small-displacement evaluations with the proved quadratic coefficient. No external packages or external certificates are required.

The optimal lower frame bound is for the explicitly unnormalized Gaussian windows. Bounds at a fixed positive separation are conservative; the collision limit is exact only in the asymptotic sense. General lattice perturbations and complex chirps are not covered. Independent audit has not been performed.
