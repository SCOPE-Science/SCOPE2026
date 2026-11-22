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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The verifier computes shortest-path Apéry minima for residues, independently constructs the whole membership table by additive dynamic programming, compares the resulting sets, and enumerates all maximal missing-integer intervals for each odd \(a\) from \(3\) to \(251\). It compares the entire frequency table with the formulas and checks that the lengths sum to the gap count. The recorded output is:

```text
PASS: 125 complete odd-parameter tests; 1785903 gaps; 896931 maximal gap runs; last a=251
3 [(1, 3), (2, 2)]
5 [(1, 6), (2, 2), (4, 2)]
7 [(1, 15), (4, 2), (6, 2)]
11 [(1, 37), (2, 2), (4, 2), (8, 2), (10, 2)]
17 [(1, 92), (2, 2), (4, 2), (8, 2), (10, 2), (14, 2), (16, 2)]
```

Finite verification does not establish the formulas for unbounded parameters; the Apéry threshold, row-decomposition and genus-subtraction proof establishes that claim. No independent external audit is represented.
