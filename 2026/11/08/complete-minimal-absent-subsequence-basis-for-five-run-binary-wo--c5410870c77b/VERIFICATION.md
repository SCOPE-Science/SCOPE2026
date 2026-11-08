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

# Reproducibility and limits

Run `python3 verify.py` from the extracted package directory. No nonstandard dependencies or network services are required. The code constructs exact subsequence sets and their minimal absent boundaries independently of the symbolic expression, checking all 1024 five-run parameter tuples with run lengths 1 through 4. It additionally checks 220 larger, randomly seeded tuples by confirming absence and all single-letter deletion witnesses of every proposed boundary word; 6600 random patterns are checked against forbidden-basis membership. Recorded expected output includes `EXHAUSTIVE_PARAMETER_TUPLES 1024`, `RANDOM_PATTERN_MEMBERSHIP_TESTS 6600`, and `VERIFICATION_OK`.

The finite tests do not certify the infinite theorem: the run-allocation case analysis in RESULT.md supplies its mathematical proof. General-literature overlap cannot be excluded, especially from a related conference paper whose full text was not available for inspection. This document does not assert independent verification or independent audit.
