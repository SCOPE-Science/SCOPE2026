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

The universal proof is in `RESULT.md`, with a deterministic independent checker in `verification/check.py`. Run `python verification/check.py` from the extracted package root. Expected last line begins `HYPERSIMPLEX_FIRST_VOID_PASS`.

Observed checks: 95,682 rational-grid comparisons of brute-force membership against the low/high threshold description; 225 numeric Euclidean projections onto **all** candidate homothetic vertex copies using independent water-filling; seven exact Gram determinants; four Dirichlet means; and Eulerian volume normalization comparisons through dimension 12. These tests confirm formulas for the sampled cases only, not the infinite-dimensional quantifiers. The proof relies on exact algebra, metric inequalities and simplex measure integration, rather than Monte Carlo.

No independently performed mathematical audit is claimed. The external priority comparison is provisional.
