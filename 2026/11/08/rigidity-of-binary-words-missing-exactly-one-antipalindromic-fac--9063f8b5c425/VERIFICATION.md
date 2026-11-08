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

Run `python3 verify.py` with Python 3.8 or newer. The checker implements direct antipalindrome-factor sets, an independent equality-edge character test, and a closed-form construction of all five predicted families. It exhaustively checks binary words of lengths 7 through 15 and verifies candidate extension transitions through length 89. The expected final line is `VERIFY_OK exhaustive_binary_words=65408 n=7..15 template_extensions=n7..89`.

For the infinite theorem, the essential logical steps are (1) one new distinct antipalindromic factor per append at most; (2) every even antipalindromic factor is equivalent to an odd palindromic equality-edge word with zero central edge; (3) the listed exhaustive extension table; and (4) a complete finite base at length 7. All quantifiers beyond the tested range are covered by the induction in `RESULT.md`, rather than extrapolation from the checks. Historical priority has not been independently certified.
