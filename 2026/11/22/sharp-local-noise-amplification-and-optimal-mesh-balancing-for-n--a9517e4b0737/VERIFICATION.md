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

# Verification of the exact four-knot PCHIP perturbation theorem

The standalone `pchip_sensitivity_verify.py` uses the standard Python library and can be replayed with `python3 pchip_sensitivity_verify.py`. Its seeded exact `fractions.Fraction` computations check 1,200 pairs of nondecreasing inputs on randomly chosen positive rational meshes and evaluation positions, 1,000 exact analytic Jacobian sign/translation identities, three explicitly constructed near-sharp signed perturbations and 300 independent mesh-balancing comparisons. It checks the exact central-cell coefficients 2 for spacings (1,1,1) and 14/5 for (1,2,1). All checks passed.

The infinite claim is not derived from these samples. It rests on the analytic gradient-sign calculation, the sharp boundary approach using positive central and vanishing positive outer secants, and strict convexity of the rational mesh coefficient. The claimed asymptotic is an ordinary one-sided limit with the opposite neighboring mesh held fixed. No formal proof assistant or external independent audit was used.

Known limits: the endpoint slope selection of a finite PCHIP interpolant is outside the theorem; historical priority has residual uncertainty; extension to perturbed knot positions or nonmonotone signals is unproved.
