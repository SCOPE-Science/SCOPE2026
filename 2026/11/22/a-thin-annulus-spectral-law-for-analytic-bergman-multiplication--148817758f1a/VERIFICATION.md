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

The exact spectrum follows from the displayed Laurent-monomial moment ratios. Run `python check_annulus.py` (Python 3, standard library) for exact rational checks and finite numerical diagnostics; expected output: `ANNULAR_BERGMAN_COMMUTATOR_DIAGNOSTIC_OK 779`.

The proof of positivity uses strict moment log-convexity, the thin-annulus limit uses a uniform curvature bound and dominated Riemann sums for every \(p>1/2\), and the exact quadratic coefficient uses a Fourier transform and Plancherel. Finite tests do not certify these infinite-dimensional steps. Global priority against unpublished or unindexed literature remains uncertain; independent mathematical validation has not been performed.
