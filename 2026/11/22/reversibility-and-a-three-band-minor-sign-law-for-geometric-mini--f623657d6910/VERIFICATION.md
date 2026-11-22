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

The exact algebraic and finite-rational checker in `checks/check.py` was executed against the present package and returned:

```
PASS: PGF identities, symmetry, marginals, signed minors and transitions
```

It verifies the two-variable pgf identity symbolically, stationary marginals and symmetry symbolically, the first two minor identities symbolically, and explicit finite transition/mass/minor identities over nonnegative indices at rational parameters. Infinite-index and all-parameter conclusions rely on the exact Gram and geometric-ratio arguments in `RESULT.md`. The checker is a reproducibility aid, not an infinite certificate. An independent audit has not been performed. Full text of relevant older minification literature was unavailable; historical priority is not independently established.
