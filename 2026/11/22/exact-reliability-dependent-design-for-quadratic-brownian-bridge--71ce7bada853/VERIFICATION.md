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

`verify.py` is a standalone symbolic/reproducible checker. The risk identity is derived from Gaussian conditional covariance and the integrated Isserlis formula; its symbolic comparisons validate independent polynomial expansions, centering, stationarity and derivative boundary certificates. Numerical checks compare 14,000 random feasible designs at seven positive reliability values against the derived optimum. Run with Python 3, SymPy and NumPy; output should begin `PASS:`.

The proof in RESULT.md, not the random sample, establishes the all-design/all-reliability optimization. This check does not independently certify historical priority. Independent audit has not been performed.
