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

The full analytical proof is in `RESULT.md`. The accompanying `CHECK.py` constructs exact SymPy rational functions for all 125 entries, verifies the nine nontrivial sign classes under norm-weighted permutation, confirms the two polynomial elimination identities, and verifies the independent rational boundary examples. A seeded sample of 200 strictly increasing rational profiles supplements these symbolic identities; this finite check is not an infinite proof.

Run `python CHECK.py` with SymPy installed. The proof does not depend on a numerical optimizer, a finite-grid completeness assumption, or independent verification.
