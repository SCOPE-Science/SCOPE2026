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

The accompanying `onset_checker.py` is a self-contained Python 3 check using exact rational arithmetic. It compares the prediction with direct divisor enumeration for 153,292 cases and confirms exact multiplicity, not just threshold existence. It does not certify the infinite argument; that is supplied in RESULT.md.

Run with `python3 onset_checker.py`. The expected output is `DIVISOR_ONSET_EXACT_OK 153292`. The test does not assume external data or use stochastic sampling.
