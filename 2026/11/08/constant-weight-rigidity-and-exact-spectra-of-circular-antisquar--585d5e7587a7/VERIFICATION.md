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

# Reproduction

Run `python3 -B VERIFY.py` from a directory containing this file and `VERIFY.py`. The script is standard-library-only and deterministically prints `VERIFY_OK` after checking the closed counting formula against all binary words of lengths 1–16; checking all words through length 11 against direct antisquare search up to order three times the period; checking length-refined weight distributions by a separate 32-state transfer automaton through length 40; and checking the sharp support criterion through length 120.

The finite antisquare scan does not prove the absence of arbitrarily long antisquares. The proof relies on the published full minimal-antisquare classification and the periodic transition-code argument. The transfer automaton verifies finite coefficients, not the infinite generating-function identity. The proof itself gives the infinite result.
