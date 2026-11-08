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

Run `python3 verify.py` using Python 3 and only its standard library. This file accompanies `RESULT.md` and is complete without external inputs. During this review, the script terminated successfully with the following exact output:

```
PASS: 4687 exact comparisons; exhaustive trees n=2..10; recurrences n=2..65; sign laws n=3..250.
```

The independent enumeration constructs each uniform increasing labeled tree via all parent-choice vectors, computes full depths, counts leaf indicators, and compares exact rational second moments to the symbolic formula. Separately, a three-polynomial rational recursion checks sizes through 65, and coefficient identities and sign changes are checked for sizes 3–250. No floating point approximation is used.

The proof in `RESULT.md`, not the finite execution log, establishes the theorem for arbitrary \(n\ge3\). This verification provides neither an independent audit nor certification of historical priority.
