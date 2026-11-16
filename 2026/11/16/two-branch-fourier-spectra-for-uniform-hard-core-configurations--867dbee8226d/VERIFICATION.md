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

The analytical verification consists of diagonalizing the explicit three-state transfer matrix, using a finite geometric-sum identity to extract both spatial Fourier branches, and proving strict rank from the allowed empty and singleton configurations. The ratio limit follows from uniform exponential convergence of both branch formulas, including the special symmetric zero-frequency term. The standalone `check.py` enumerates every independent set for \(3\le n\le9\) and compares direct covariance Fourier eigenvalues to the formulas within numerical tolerance; it also evaluates the ratio at larger sample lengths. Finite enumeration does not certify an all-size theorem, and historical priority has not been independently audited.
