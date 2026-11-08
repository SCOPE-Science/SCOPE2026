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

# Reproducibility and scope

Execute `python3 verify.py` with Python 3 and its standard library; no downloaded dependencies or data are required. The checker carries out independent exhaustive edge-subset enumeration of the complete bipartite graphs of sizes \(K_{2,2}\), \(K_{3,3}\), and \(K_{4,4}\). It records every perfect-matchable tree, extracts its unique matching, contracts that matching, tests quotient and lift uniformity, and checks distances with breadth-first search against a separate binomial prediction. Prüfer-sequence enumeration also checks the exact Cayley pair-distance formula through six vertices.

The test completed successfully: `VERIFY_OK 943 exact assertions`.

The asymptotic Rayleigh distribution and continuum-metric statement are not consequences of finitely many tests. Their proof uses the exact pair-distance tail, conditional bounded differences, a union bound, and classical convergence of uniform Cayley trees to the Brownian continuum random tree. The baseline counting result is pre-existing literature, not a novelty claim. Independent mathematical audit: not performed.
