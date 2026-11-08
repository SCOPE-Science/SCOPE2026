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

# Reproducibility and limits

Run `python3 checker.py` using only the Python standard library. The checker computes every distinct output obtained from all two-position deletions of all \(q\)-ary words for \(q=2,3,4\) and short block lengths, compares the pointwise identity, then forms and compares the full rational conditional mixture, mean and variance. It also checks the earlier binary formula at lengths \(2\) through \(39\).

Actual replay output:

```
PASS: 9240 exhaustive pointwise cases; 18 exact finite-distribution and moment comparisons; 38 binary specialization comparisons.
```

The exhaustive enumeration covers only those finite parameters. The written proof handles arbitrary integer alphabet size \(q\ge2\) and block length \(n\ge2\). No claim of exhaustive search over the infinite parameter domain, independent mathematical certification, or definitive historical priority is made. The earlier 2008 paper was not obtainable in full text; its documented scope and the relevant accessible 2026 literature were inspected as part of the comparison.
