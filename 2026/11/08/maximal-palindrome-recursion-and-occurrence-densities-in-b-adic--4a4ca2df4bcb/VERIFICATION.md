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

The standalone `verify_maximal_palindromes.py` program was run with Python 3 against the actual accompanying script. It returned:

`VERIFY_OK bases=2..8 lengths_per_base=1..150 length_cases=1050 palindrome_window_tests=27910468 occurrence_checks=23293`

Its prefix lengths are chosen deterministically by the script. The test enumerates all palindromic factors up to the stated length within each finite prefix, compares nonextendibility against the recursive prediction, and compares every observed occurrence of each generated palindrome with the exact start-position formula within that finite prefix.

No infinite quantifier, all-base assertion or natural-density limit is certified by finite enumeration. Those follow from the proof in `RESULT.md`. No independent audit has been performed.
