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

# Verification of the rank-four prime law

The theorem is proved for all positive \(e,k\) in `RESULT.md` by an exact recurrence calculation modulo \(17\), a window-difference identity, period minimality, and an order-\(16\) calculation. It does not depend on a finite experiment. Reproduce the finite checks with `python3 verify.py` in a directory containing both `verify.py` and `checks.txt`. The code checks all \(38{,}400\) exponent-length pairs with \(1\le e\le96\), \(1\le k\le400\) against every cyclic starting position and asserts the exact residue and congruence conditions. `checks.txt` is the expected output. No assertions about other primes, exact gcd magnitudes, or higher \(17\)-adic valuations are supported.
