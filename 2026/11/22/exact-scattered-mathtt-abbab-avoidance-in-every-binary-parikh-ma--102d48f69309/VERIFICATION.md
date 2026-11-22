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

# Reproduction and scope

Run `python3 check_bruteforce.py` and `python3 check_dynamic.py` with standard Python 3. Their outputs must be exactly `BRUTEFORCE_OK words 48619 classes 1377` and `DYNAMIC_OK classes 6253 compositions 169`.

The brute-force enumeration directly constructs every binary word for each composition with at most eight letters of either type, scans for scattered `abbab`, and independently computes the scattered `ab` count. Its class histogram checks the asserted exact numerator including the zero-count boundary.

The independent dynamic checker builds words through a six-state greedy subsequence automaton while updating the `ab` count on appending `b`. A separate Gaussian recursion calculates the class denominator. It checks the numerator, denominator, unrefined total, and exact maximum for every composition with up to twelve letters of either type. The two methods have different counting structures; their agreement is finite corroboration. The unrestricted result rests on the explicit partition correspondence and positive-row spread criterion in `RESULT.md`. No independent external audit has been performed.
