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

# Computational checks

Run `python3 verify.py`. This standard-library program first builds all friendship graph edges and their adjacent-edge neighborhoods from endpoints, then directly enumerates three-colour assignments for triangle counts one through four. For each assignment it compares the original per-edge half-neighborhood requirement with the new structural characterization, and checks the exact six-term count. It additionally rules out two-colour assignments at the same orders. A separately coded grouping over missing-colour words verifies the algebraic closed form through eight triangles. The observed output is:

```text
DIRECT_DEFINITION_AND_CLASSIFICATION_OK 1 named_colorings 6
DIRECT_DEFINITION_AND_CLASSIFICATION_OK 2 named_colorings 108
DIRECT_DEFINITION_AND_CLASSIFICATION_OK 3 named_colorings 2472
DIRECT_DEFINITION_AND_CLASSIFICATION_OK 4 named_colorings 57456
FINITE_GROUPED_FORMULA_OK through m=8
VERIFY_OK
```

No computation verifies the infinitely many remaining values by enumeration. The proof in RESULT.md is required for the general theorem. Independent mathematical audit has not been performed.
