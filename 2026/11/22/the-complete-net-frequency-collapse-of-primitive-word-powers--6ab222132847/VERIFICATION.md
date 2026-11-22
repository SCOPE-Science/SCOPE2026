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

# Verification and reproduction

Run `python3 verify_bruteforce.py` and `python3 verify_phases.py` with Python 3 standard library. The first enumerates all factors and their frequencies for 2679 cases, with the exact two intervals and an exponent-two counterexample. The second independently computes duplicates by pairwise string equality for 1154 cases and tests the distinct-rotation premise. The accompanying `brute_output.txt` and `phase_output.txt` are captured output from their execution. No third-party files, source trees, or external downloads are needed.

These are finite consistency tests, not a proof of infinite quantifiers. The mathematical derivation in `RESULT.md` gives the universal proof; source comparison and inaccessible full preprint risks are documented in `REVIEW.md` and `AUDIT.json`. No independent audit was performed.
