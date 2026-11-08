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

# Reproducible verification

Run `python3 verify.py` with Python 3.8 or newer (standard library only).

The verifier enumerates all binary words for lengths 0 through 14, independently recomputes the letter counts and \(01\)-subsequence counts, and tests scattered membership for each of the six balanced length-four patterns. It compares exactly 11,640 coefficient counts to the formulas, with strict assertions for each. It also checks the total \(AB+1\) and exact first-moment identities for all \(0\le A,B\le25\). Successful output begins `BALANCED_PATTERN_VERIFY_OK`.

The numerical audit is finite. The infinite assertion and exceptional boundaries require the constructive block-decomposition proof in `RESULT.md`. Neither the observed examples nor the test output are treated as independent certification of the proof. An independent mathematical audit has not been performed.
