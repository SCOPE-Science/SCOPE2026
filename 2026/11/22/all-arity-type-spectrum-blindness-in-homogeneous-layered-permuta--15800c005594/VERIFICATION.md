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

# Verification
The complete all-arity proof is the labeled combinatorial species factorization in `RESULT.md`. Independently, `check.py` enumerates every first-order interleaving of old and new labels and every cut mask of decreasing layers, then tests the restriction to the named base. The output `check_output.txt` records 48 exact small-case comparisons across the formula, labeled diagrams and direct popularity enumeration and confirms the two sharp examples. Run from this extracted directory using `python3 check.py`; no special packages are needed.

The exhaustive enumeration is bounded by combined old-plus-new size six, hence does not certify the all-arity theorem. The all-arity assertion relies on the bijection described in the proof. Independent mathematical audit has not been performed.
