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

# Verification notes

Execute `python3 verify.py` from the same extracted directory using Python 3 and its standard library. The checker computes closed-neighborhood fractions as exact rational numbers, tests every possible opposite-color swap for 85 complete multipartite graph structures with at most eight vertices, and checks the exact integration polynomial and extrema across 184 biclique/minority-population parameter configurations with \(1\le a,b\le7\). Its expected successful output is:

```
PASS: 85 multipartite structures, all nonconstant colorings and opposite-color swaps
PASS: 184 biclique/minority-count configurations, exact integration extrema
```

The human proof in `RESULT.md` establishes the unrestricted parameter theorem; finite enumerations alone do not. The verifier does not assess publication priority, the utility's exact functional form beyond the symmetric representative, or independent external validation.
