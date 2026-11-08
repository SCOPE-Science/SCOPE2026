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

# Reproducibility

Run `python3 verify.py` using Python 3. The script is standalone and uses only the Python standard library.

Actual checks: 8,190 exhaustively enumerated binary words through length 12 for exact finite forbidden-pattern/code correspondence; brute-force enumeration of all good palindromes through length 24; and 840 palindrome construction checks with uniqueness, both parity classes and the explicit prefix-code recurrence. Reported small-length palindrome counts through 24 are `2, 2, 4, 2, 8, 4, 10, 6, 16, 10, 24, 14, 38, 22, 56, 30, 82, 46, 124, 70, 182, 104, 270, 152`.

The finite tests do not certify the infinite theorem. The mathematical proof rests on an explicit injection and on the published unrestricted growth theorem for the same class. An independent scientific audit has not been performed.
