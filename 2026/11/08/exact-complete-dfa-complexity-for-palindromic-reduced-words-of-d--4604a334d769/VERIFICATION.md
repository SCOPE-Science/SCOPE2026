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

# Reproduction and limits

Execute `python3 checker.py` with Python 3.9 or later; no third-party packages are needed. It builds a deliberately nonminimal DFA from the alternating-prefix definition; performs partition refinement independently of the claimed quotient classification; and compares its minimized size against the closed formula. It also tests directly enumerated words against the required literal palindrome, single-factor, alternating and finite-length conditions.

The checker verifies 2,913 tuples of one to five factors, finite exponents 2, 3, 4, 5 or infinity, with a bounded subset of the five-factor cases, and 1,121,923 short words. The printed counts come from actually running this file. The mathematical proof (not these finite computations) gives the result for all finite products and unbounded exponents. No independent formal proof or external audit is supplied.
