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

# Reproducibility and logical boundaries

Run `python3 check_circular_arc.py` with Python 3 (standard library only). The program checks every one of the \(2^d\) target label sets at each \(d\in\{3,4,5,6,7\}\) against all cyclic intervals in each displayed witness row, yielding 248 distinct supported patterns and 14 witness rows overall. It also tests equality of all 35 triple traces and positive coverage of all 21 pair traces in the seven-point construction, and numerical strictness of four middle-layer bounds.

Observed successful final line:

```text
CIRCULAR_ARC_STUMP_PASS 248 WITNESSES 14 LOWER_BOUNDS 4
```

The proof that \(\ell d\ge\binom d{\lfloor d/2\rfloor}\) is necessary for arbitrarily selected \(d\) points is mathematical, not empirical. The finite checker verifies explicit constructive lower bounds only. The classification stops at eight features; nothing here determines the next coordinate threshold or an asymptotic covering rate. The cited seven-point tight-cycle decomposition is established prior work, not independently claimed as novel. Independent audit has not been performed.
