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

The closed-form candidate was derived by exact KKT multipliers for the strictly convex tree-resistance optimization. The proof establishes all parameter ranges \(k\ge3\), \(L\ge3\); the finite diagnostics alone do not establish the theorem.

Run `python3 verify.py`. This checks exact-integer feasibility and multiplier-sign inequalities over 5,684 parameter pairs, and (if NumPy is installed) builds independent transition matrices and compares their nonzero Laplacian eigenvalue reciprocals against the formula for 60 instances. The actual packaged checker execution returned:

```
PASS: 5684 exact-inequality parameter pairs; 60 spectral comparator cases.
Finite diagnostics are not a proof for all parameters.
```

The public proof also states the scope of the Kemeny convention and excludes unproved extensions to unequal-arm or nonuniform-stationary chains. Independent validation has not been performed.
