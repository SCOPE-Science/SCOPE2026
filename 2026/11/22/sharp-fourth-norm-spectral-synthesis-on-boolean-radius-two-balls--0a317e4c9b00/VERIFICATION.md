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

From the directory containing these files, execute `python3 check.py` using the Python 3 standard library. It reports `PASS: 214 exact or numerical supplementary checks`. The checker enumerates all sign patterns to verify complete-graph edge moments through nine vertices, compares exact rational direct Walsh fourth moments to the two-orbit formula, and samples root locations, the signed-weight threshold, and the large-dimensional asymptotic.

Universal correctness is supplied by Steps 1–6 of `RESULT.md`: exact parity-subspace isomorphism; strict complex convexity; full character-to-sign-vector averaging; explicit quartic differentiation; exact even-degree subgraph moment counting; and a Rademacher/chi-square limiting argument with quantitative boundedness. Numerical checks are supplementary, do not establish universal uniqueness, and do not replace the analytic argument.

The referenced scientific papers and indexed mathematical records support the comparison of objectives and known results, not a mathematical independence or independent validation certificate. An independent audit has not been performed.
