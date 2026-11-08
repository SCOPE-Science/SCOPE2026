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

# Verification protocol

Run `python3 verify.py`. The script uses Python's standard-library `fractions.Fraction`, independently constructs every weighted graph Laplacian, performs exact Gauss--Jordan inversion of grounded principal submatrices, and enumerates every leader set of the relevant sizes. It then compares the resulting minima with the closed two-candidate formula for 1,248 positive-rational test cases with \(2\le m\le9\), including tied weights. There are 4,992 explicit matrix-inverse checks and 1,056 sharp threshold checks. It also verifies the eight-leaf example at three leader budgets.

A successful run prints `VERIFY_OK`, the counts above, and the exact costs of \(83/100\), \(3/100\) and \(81/4100\). The proof for all positive real weights is the Schur-complement and strict dominance argument in RESULT.md. Finite enumeration does not establish universal validity by itself. No independent audit is claimed; scientific literature indexing may miss equivalent formulations.
