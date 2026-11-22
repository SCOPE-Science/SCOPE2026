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

The independent audit channel has not been performed. The current checks are computational corroboration of a separate all-dimensional analytical proof.

Execute `python verify_centered_clipping.py` with Python 3; it uses the standard library only and exact `fractions.Fraction` arithmetic. Expected outputs:

```
EXACT_ALL_ACTIVE_MASKS_AND_STEP_CUTS_PASS n=2..10
EXACT_STRICT_MASK_LOCAL_WITNESSES_PASS n=2..100
RANDOM_RATIONAL_TWO_INPUT_AND_ONE_INPUT_PASS trials=2400
CENTERED_CLIPPING_VARIATION_ALL_CHECKS_PASS
```

The checker exactly enumerates \(2^n\) masks at each step cut for \(2\le n\le10\), confirms each cut modulus \(2j(n-j)/n\), and constructs actual pairs with the designated masks (strictly away from clipping boundaries) at \(2\le n\le100\). It also checks seeded rational two-input inequalities, individual-input variation diminution, and translation equivariance. Computation beyond those cases was not performed; no finite enumeration is claimed to prove the infinite family. The rigorous upper bound and sharpness for all \(n\ge2\) are derived in `RESULT.md`.
