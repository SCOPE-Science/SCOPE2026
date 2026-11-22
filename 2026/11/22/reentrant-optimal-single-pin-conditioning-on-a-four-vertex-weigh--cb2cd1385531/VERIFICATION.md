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

# Exact certificate replay

Run `python check.py` with Python 3 and its standard library. For each specified gain and one of the four possible pin positions, the program constructs the characteristic polynomial through the tridiagonal continuant, evaluates its values as exact rational numbers at preselected rational endpoints, and verifies four disjoint strict sign changes. Degree four plus positive definiteness yields complete positive eigenvalue enclosures, not sample-based spectral estimates.

Each condition number is bounded by ratios of those rational endpoints. The program verifies all nine strict winner-versus-competitor inequalities in rational arithmetic, and the qualitative return follows by continuity. The independent analytic large-gain argument uses convergence of the penalized Rayleigh minimum to the grounded principal-matrix minimum. A positive-definite block proves the grounded minimum is exactly 1 for site 2; explicit rational test vectors prove it is strictly smaller than 1 for each other site. Total: forty-eight certified root intervals and nine winner comparisons.

**Limits:** The program does not isolate the exact gain values at which winners change or certify a graph-size minimality statement. An external independent review has not been performed. Displayed decimal values are approximate descriptions of separately proven rational enclosures.
