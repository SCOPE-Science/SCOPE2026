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

Run `python3 check_matching_ranks.py` with Python 3 and no dependencies beyond the standard library. The executed output was:

```
ALL_CHECKS_OK positions=51883 labelled_hosts=3736 max_n=12
```

The checker enumerates each allowed prime extension over every marked subset in a canonical degree-at-most-one host, computes the game rank by direct recursion over all actual new vertices, and compares with the independently written resource formula. It checks all canonical host isomorphism types and all marked subsets through 12 vertices, and separately enumerates every labelled matching graph through 9 vertices to compare the full labelled rank census. No sampled or timed-out instances are counted as verified. These finite tests support but do not replace the all-size and countable proofs.

Scientific limits: unrestricted graph-extension ranks, uncountable hosts and independent mathematical validation are not covered. The inspected 2026 primary rank article supplies definitions, not a matching-specific proof. Historical priority remains provisional.
