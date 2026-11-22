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

Run `python checker.py` with Python 3, NumPy, SciPy and HiGHS. It rebuilds a 240-variable direct circulation-and-reversal mixed-integer model and a 160-variable necessary quotient-parity model, demands global objective 106 with zero reported solver gap for both, checks integral primal constraints, constructs an Euler circuit, and tests 106 cyclic four-grams directly.

The output observed during preparation was `DIRECT_OPTIMUM 106 RELAXATION_OPTIMUM 106 ... VERIFY_OK`. Reproduction requires available solver libraries and trusts their exact optimality reporting for integer-coefficient constraints. This is not an independent formal proof certificate; no third-party audit has been performed.
