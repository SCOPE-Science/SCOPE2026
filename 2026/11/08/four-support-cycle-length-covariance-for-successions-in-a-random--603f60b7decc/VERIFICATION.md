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

# Reproduction and boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. The script enumerates permutations of orders 4 through 9 and checks the complete local cross-covariance array using exact integer and rational arithmetic. A second route obtains mixed moments from the three distinct forced-arrow configurations and checks their equality with the closed formulas through order 19; it also checks the sum over all succession positions.

Observed output:

`PASS: 2688 exact rational comparisons; all permutations of sizes 4 through 9 enumerated`

The proof for unbounded \(n\) is the explicit contraction bijection and coefficient cancellation in `RESULT.md`. Computations check only the indicated finite cases. No asymptotic experiment, external formal proof, or independent validation is claimed.
