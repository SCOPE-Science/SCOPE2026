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

## Direct mathematical checks

The exact moment integrals for degrees zero, one and two reconstruct the entire two-by-two Gramian. Its determinant and trace reduce the condition-number calculation to one complex scalar. The negative-square determinant certificate is valid for every complex sensor and establishes the universal lower-bound ceiling and its equality conditions without numerical discretization. The positive branch and strict subcritical claim were checked separately. Finite-dimensional numerical calculations are supplementary only, not proof of exhaustive quantification.

## Reproducibility and limits

Take any real `a>0,c>0`; set `r=c/(2*a)` and any `w` complex, `d=1+abs(w-r)**2`, `M=[[abs(w)**2+r*r,w],[conj(w),1]]`. The frame-operator eigenvalues equal the eigenvalues of `M/d` divided by `2*a` for the unit sensor proportional to `(w-r,1)`. Use exact symbolic arithmetic for equality cases. No independent audit has been performed, and no subcritical E-optimal value is asserted.
