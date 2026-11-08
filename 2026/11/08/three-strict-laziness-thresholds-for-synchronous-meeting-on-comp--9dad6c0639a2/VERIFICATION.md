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

# Reproducibility

Run `python checker.py` with Python 3 and SymPy installed. It recomputes the three-orbit transition matrix and inverse, derives the exact difference polynomials, confirms the endpoint identities, computes the Sylvester resultant and its 36 strictly positive coefficients, and independently solves all unordered distinct starting-pair states on six graph sizes at three rational holding probabilities. Expected output: `VERIFY_OK 267 exact state comparisons; 36 strictly positive resultant coefficients; polynomial identities confirmed`.

The symbolic determinant/resultant equalities are exact polynomial identities for arbitrary symbolic graph sizes; finite-state comparisons are only independent cross-checks. The proof's transience and continuity arguments are mathematical arguments, not consequences of any finite test. Neither historical novelty nor independent audit is certified by this checker.
