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

The proof is analytic, based on Rule 57's sitewise hold condition and an exhaustive logical classification of both scan-boundary cases. The programs `checks/exhaustive.py` and `checks/symbolic.py` are standalone and require only Python 3's standard library. Run them from the package root. The corresponding output files record successful checks of every initial word for lengths 3 through 17, and independent boundary-equation checks through length 256.

These finite ranges do not establish the theorem for arbitrary length. Infinite validity follows from the hold-propagation lemma and the length-four word recurrence in `RESULT.md`. The arbitrary-length boundary congruence argument was checked separately against the explicit case split, including small lengths 3, 4 and 5. The initial source date is grounded in the preprint submission record, not a later journal revision. No independent external audit has occurred.
