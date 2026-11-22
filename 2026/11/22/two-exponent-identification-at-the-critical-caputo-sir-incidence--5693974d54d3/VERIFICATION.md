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

Run `python3 check.py` with Python 3. The checker uses only standard-library `math` and `random` and performs 500 seeded critical-parameter coefficient comparisons (five Caputo orders, 100 random positive parameter choices each) plus special tests of the exact half-order identities. The observed run output was:

```
PASS: 500 critical parameter cases and the exact resonant half-order example
```

A separate symbolic simplification confirmed that substituting the critical equation \(\gamma=(\beta/N)(N-2I_0)\) reduces the three claimed coefficient identities to zero. The actual universal mathematical evidence is the coefficient recurrence, strict Gamma log-convexity and Puiseux-exponent contradiction in RESULT.md, not these examples.

Scope: ideal continuous-time SIR incidence from a known initial instant. The calculation establishes neither numerical stability of exponent recovery under noise nor exact recovery of \(\beta\), \(\gamma\), or \(I_0\). No independent scientific audit has been performed.
