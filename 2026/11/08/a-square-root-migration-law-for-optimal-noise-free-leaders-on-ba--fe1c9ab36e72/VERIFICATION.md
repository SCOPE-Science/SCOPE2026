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

The independent exact-rational `verify.py` program reconstructs small balanced split graphs, grounds their Laplacians at every leader set for \(2\le n\le5\) and \(1\le k<n\), and independently inverts the resulting matrices by fraction-based Gauss-Jordan elimination. The observed trace agrees with the analytical count formula in all **502** enumerated cases. The code also checks that for \(n=20\), the unique optimal clique-leader counts are \(4\) when \(k=4\) and \(0\) when \(k=7\), with exact costs \(8/5\) and \(381/280\), respectively.

Command: `python3 verify.py`

This is a reproducibility test, not an exhaustive computation for all graph sizes. The limit theorem and eventual exact endpoint choices follow from the uniform asymptotic and derivative arguments in `RESULT.md`. No independent external audit has been performed.
