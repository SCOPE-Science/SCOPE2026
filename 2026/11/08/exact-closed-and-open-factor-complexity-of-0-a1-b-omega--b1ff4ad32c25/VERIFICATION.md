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

# Verification notes

The exact theorem concerns all positive integral run lengths and factor lengths. Its proof is in `RESULT.md`; finite enumeration alone is not a proof.

Execute `python3 verify_closed_complexity.py` from the same directory. It creates the relevant periodic source, obtains every distinct length-`n` factor through all cyclic phases, independently tests each possible proper border and the number of occurrences inside each candidate word, and compares both the closed count and total factor count with the formulas. The default test range is `1 <= a,b <= 12` and `1 <= n <= 2(a+b)+max(a,b)+2`, yielding 5,254 factor-length comparisons over 144 pairs; it also checks the saturation boundary. A larger independent exploration covered 1 <= a,b <= 15 and 10,010 comparisons.

Computational limitation: no finite enumeration certifies the infinite theorem, and no independent scientific audit or external formal proof certification has occurred. The document's proof uses the first-return lemma and a separate classification of short factors.
