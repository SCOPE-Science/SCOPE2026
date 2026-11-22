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

The statement and its derivation were checked directly from the Green-class edge rule and the complete-graph rooted-forest formula. `check.py` uses exact integer/rational operations, directly generates finite monoids and their principal ideals, compares a Laplacian cofactor against the closed product, and exhaustively checks small rooted parent maps.

Run in a directory containing the standalone checker:

```text
python check.py
```

The expected final marker is `GREEN_DIVISIBILITY_ARBORESCENCES_OK`. This does not constitute independent mathematical verification, and the finite tests do not establish the universally quantified theorem. The written proof supplies that deduction.
