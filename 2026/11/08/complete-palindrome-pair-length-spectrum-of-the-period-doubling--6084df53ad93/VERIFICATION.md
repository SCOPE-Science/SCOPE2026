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

# Reproducible checks

Run `python3 verify_period_doubling.py` from the directory containing this file. The script checks the conjugacy-versus-palindrome-pair criterion exhaustively over all binary words through length 13; tests both positive and negative substitution lemmas for small iterates; compares factor sets from independently generated prefixes of lengths 8192 and 16384; and checks all factor counts, good-length classifications, and published enumerator upper-bound equalities at each length from 1 to 192.

The results are exact finite checks. Comparing two finite prefixes cannot itself prove factor completeness for an infinite sequence; the all-length theorem is proved in RESULT.md from the substitution lemmas, the subword-complexity recurrence, and the cited published palindromic-periodicity theorem. The published automaton proof is not reimplemented. No independent scientific audit is represented.
