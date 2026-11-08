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

The embedded `verify.py` uses only the Python 3 standard library. Run `python verify.py` in a directory containing that file. It checks direct unilateral comparisons and cut weights for all \(98{,}112\) action profiles at \(54\) rational parameter settings, and checks the Perrin gap enumeration for rim lengths through \(100\). It prints `VERIFY_OK` if all assertions hold.

This is finite consistency testing. The proof for arbitrary rim length and arbitrary positive real spoke ratio is the local-best-response and cyclic-gap argument in `RESULT.md`. No independent external audit has been performed.
