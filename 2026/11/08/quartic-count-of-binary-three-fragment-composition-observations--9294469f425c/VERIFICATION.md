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

# Verification details

The self-contained proof and generated-series derivation appear in RESULT.md. `direct_check.py` computes every available length-one/two/three composition multiplicity directly from the binary word for all lengths from one through seventeen. Its expected terminal line is `DIRECT_OK`.

`structural_check.py` independently counts attainable profiles using run numbers, singleton-run numbers, the achievable total lengths for each symbol, and the distinct endpoint correction values. This is checked through length forty-two. The same script computes the integer coefficients of the exact proposed rational series through length eighty and matches the stated piecewise quartic; its expected terminal line begins `STRUCTURAL_OK`.

From a directory with these two standalone scripts, run `python3 direct_check.py` and `python3 structural_check.py`. Both use only the standard Python 3 library. The finite checks do not show the result for infinite lengths; this comes from the complete run classification and geometric-series identities in RESULT.md. No independent audit has been conducted.
