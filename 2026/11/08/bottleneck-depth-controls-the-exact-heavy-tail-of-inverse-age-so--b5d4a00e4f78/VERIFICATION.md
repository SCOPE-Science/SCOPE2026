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

# Verification record

The theorem has a direct proof in `RESULT.md`. The additional checks below are finite reproducibility tests and do not establish the infinite-parameter theorem by enumeration.

Run `python verify.py` with a standard Python 3 interpreter. The actual run reported:

- Exact dynamic-programming versus exhaustive eligible adoption order agreement for 408 small-graph instances.
- Exact rational Laplace-transform agreement for 816 test values using independent adoption-order summation.
- Finite-state uniformization probabilities in 17 additional cases.
- Exact path and star formulas checked by independent uniformization for 14 motif sizes.

`verify.py` is part of the same package. No third-party dependencies or input data are required. No confidence intervals, random seeds, numerical tolerances masquerading as a proof, or independent audit are asserted. This result addresses continuous-time rate \(a/(t+2)\), not the paper's discrete random-asynchronous update. For general graphs, algorithmic enumeration may be exponential in the number of vertices.
