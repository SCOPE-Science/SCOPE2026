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

# Reproducible scientific verification

Run `python CHECKER.py` with Python 3's standard library. The script evaluates exact rational Krawtchouk values across multiple dimensions and tests normalization, the first four low-weight formulas, complementary symmetry (even layer), the exact Parseval sum, nonnegativity of all Boolean vertices, cancellation of the weight-two value, and the rational center–leaf star value.

The infinite theorem does not follow from testing finitely many dimensions. Its unbounded-dimension hypotheses and quantifiers are proved by Gram Cauchy–Schwarz, Parseval orthogonality and uniform Stirling/central-binomial estimates in `RESULT.md`. No exact finite-dimensional minimizer or independent audit is asserted.
