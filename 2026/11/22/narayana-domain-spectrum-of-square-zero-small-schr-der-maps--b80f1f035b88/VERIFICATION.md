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

Run `python3 verify.py` using Python's standard library. The captured file `verification_output.txt` records the direct exhaustive counts for every \(2\le n\le9\) and ends with `VERIFY_OK`. The program independently enumerates each admissible map from an actual domain and a nondecreasing image sequence, checks the disjoint-image condition that is equivalent to square zero, independently enumerates the two weakly increasing sequences, verifies the exact first two moments as rational numbers, and compares the number of all nilpotents with the classical large Schröder recurrence.

The finite checks cover the given parameter values only. The proof in `RESULT.md`, not code or computational exhaustion, establishes all \(n\ge2\). No external or independent mathematical audit has been performed.
