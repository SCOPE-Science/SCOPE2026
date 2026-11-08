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

# Reproducing checks

Run `python3 verify.py` from the directory containing the extracted files. The verifier uses only the standard library. It constructs literal Abelian-square factor sets independently of the closed theorem, compares these sets with the three classified families for every \(0\le i,j,k\le18\), tests the lower bound, and exhausts all parameters with \(4\le n\le40\) to check the sharp minimum and explicit witness formulas.

Expected final lines:

```
PASS: 6859 triples, independent literal factor sets, counts, lower bounds
PASS: sharp minimum and constructive witnesses at every length 4..40
```

The infinite result requires the complete proof in `RESULT.md`. The finite program is a reproducibility check, not a replacement for quantifier-wide mathematical reasoning. The theorem has not undergone an independent mathematical audit.
