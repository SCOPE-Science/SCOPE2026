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

# Verification record

The attached `verify.py` was executed using exact integer arithmetic and returned:

```
ROOT_A_EXACT_OK 764040
```

For dimensions \(n=3,4,5,6,7\), all nonzero directions with initial \(n-1\) coordinates in \(\{-2,-1,0,1,2\}\) and last coordinate set to their negative sum were tested. Every root and every active facet inequality was checked directly, in comparison with the derived strict sign and mass criterion; the star-size bound, extremal sign patterns, and explicit optimal direction partition were also checked. The positive verification result is finite computational support only. The all-dimensional mathematical proof is in `RESULT.md`.

No independent audit or external certification has been performed. Historical priority is provisional.
