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

# Verification

The self-contained `verify.py` source uses Python 3 and SymPy. Executing `python verify.py` returned:

```text
PASS: 5 general symbolic identities; 4 exact two-step identities; 600 rational PSD comparisons; exact 116-to-zero witness
```

The general algebraic checks independently calculate the theta update from its inverse, recover the rank-one noise coefficient, check the exact Gram matrix, verify the two-by-two determinant factor, and check the first principal entry. The 600 pseudorandom parameter choices are *exact rational* comparisons of matrix positivity against the closed-form polynomial condition, not floating-point evidence or a comprehensive search. The identity \(N^2=0\) and the explicitly proved product formula establish the all-step assertions; neither finite sampling nor simulations certify those claims. The continuous-time energy assertion follows from the standard Itô squared-norm identity and a two-by-two negative-semidefinite test.

Scope limitations: constant positive step, one real Brownian driver, normalized two-dimensional commuting nilpotent drift/noise, drift-implicit theta-Maruyama. The exact two-step zero is a numerical artifact and supplies no accuracy estimate. Independent validation and exhaustive historical-priority verification have not been performed.
