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

# Reproduction and proof boundaries

Execute `python3 verify.py` from the directory containing this file and `RESULT.md`. The script uses only the Python standard library. It independently simulates the sink-burning test and one-grain additions, enumerates **every** stable state for integer \(n=2,3,4,5,6,7\), and verifies equality between the resulting exact integer avalanche-count coefficients and the closed-form polynomial.

The six verified recurrent-state counts are 12, 81, 432, 2025, 8748, and 35721. For each integer \(2\le n\le80\), a separate combinatorial check tests normalization and the exact positive/maximum counts. All these finite checks passed. The proof for arbitrary \(n\ge2\) relies on the burning criterion, disjoint height-case enumeration, and binomial weak laws in `RESULT.md`; neither a finite simulation nor the algebraic checker establishes an asymptotic theorem by itself.

The result is for a hub source distinct from the sink, and its avalanche statistic counts repeated topplings. It is not a statement about a random source vertex, a leaf source, distinct toppled sites, or a stochastic sandpile. Independent historical-priority and scientific audits have not been performed.
