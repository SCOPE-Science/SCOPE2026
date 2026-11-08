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
The proof applies for every fixed integer \(p\ge0\) and all \(n\ge2\). The exact finite covariance and its tridiagonal inverse are derived algebraically. The continuum and discrete spectral limits follow from, respectively, operator-norm convergence of step kernels and compact Jacobi finite sections (with an exact sine-basis exception for \(p=0\)).

To reproduce numerical checks, run `python checks/verify_power_lecture_hall.py` with Python, NumPy, and SciPy. The checker enumerates vertices with exact fractions for \(p=0,1,2,3\) and \(n\le6\), verifies every entry of the inverse product, checks the \(p=0\) finite spectrum, and evaluates top and bottom normalizations at selected larger dimensions. The actual execution returned `POWER_LECTURE_HALL_TWO_EDGE_SPECTRUM_CHECKS_PASSED`.

The numerical bounds used in the checker are tolerances for illustrative finite-dimensional convergence, not validated infinite-dimensional certificates. The decimal values reported for the Jacobi norm and Bessel zero should not be interpreted as formally certified enclosures. Historical priority and any mathematical review by another investigator remain open.
