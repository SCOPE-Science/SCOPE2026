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

# Verification of consecutive cubic GCD law

The executable `verify_cubic_gcd.py` uses only Python's standard library. Run it with `python3 verify_cubic_gcd.py` from the directory containing this file and the script. The real execution printed:

```
PASS: 32 exhaustive prime-power modulus tests
PASS: all dyadic lifting levels through the first empty one
PASS: 24 smooth-root single-lift checks
PASS: 22500 positive integer pairs satisfy the support restrictions
```

This tests the exceptional dyadic depths, small odd prime-power congruence counts, Hensel uniqueness in sampled cases and the universal support obstruction in finite positive boxes. It is not a proof for arbitrarily large moduli or integer pairs. The proof of the unrestricted theorem is in RESULT.md, Steps 1–6, including a uniform large-prime divisor bound required for the full limiting law. The published general convergence and coprimality frameworks are identified in RESULT.md. The independently executable tests were run locally; no independent audit or verification by another party was performed.
