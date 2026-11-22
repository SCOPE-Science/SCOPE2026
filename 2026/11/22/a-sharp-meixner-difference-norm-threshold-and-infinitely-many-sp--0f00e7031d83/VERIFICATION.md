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

# Verification

The analytical proof establishes every infinite-dimensional assertion independently of finite computations. The following supplementary checks were run by extracting and executing `check.py` with Python, NumPy and SciPy:

- Eight direct finite-dimensional Gram/Jacobi identities for two geometric weights and four shape parameters.
- Ten finite-section spectral comparisons, including distinct eigenvalues above the essential upper edge at shape parameters below one and absence above the edge in checked finite sections at and above one.
- Two distant sine-block Rayleigh lower-bound certificates exceeding the essential edge.

Command: `python check.py`. Outcome: `PASS: 8 Gram identities, 10 finite spectral tests, 2 block inequalities`.

The finite sections cannot prove infinitely many eigenvalues, density of polynomials, strict monotonicity for every parameter, or historical originality; these are addressed analytically and by literature comparison. Independent audit has not been performed.
