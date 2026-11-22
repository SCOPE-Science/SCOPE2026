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

# Reproducibility notes

Run `python3 CHECKER.py` with Python 3.10 or later. No downloaded data or external packages are required. The program computes the strongly connected graph inventory for small index sets, expands the arithmetic divisor formula exactly, and enumerates all nonzero generating subsets by *direct semigroup multiplication* for the four parameter pairs \((n,m)=(2,1),(2,2),(2,3),(2,4)\). Full vector comparisons passed: totals \(4,136,3124,57312\). It exhaustively verifies **all** \(n=3,m=2\) generating-subset coefficients by a second lifted-state reachability algorithm (189,504 total), checks the strong-graph arc counts, and tests 512 deterministically sampled multiplication closures.

The general formula is not computationally certified for unbounded indices; its proof is the explicit subgroup-potential bijection, the elementary generation criterion, and divisor Möbius inversion. Historical novelty remains qualified by possible uninspected equivalent formulations, and independent external validation has not occurred.
