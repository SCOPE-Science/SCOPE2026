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

# Reproducibility and verification

Execute `python3 verify.py` with Python 3.10 or later and no external dependencies. Expected final line:

```
POSSET_DIFFERENCE_BODY_PASS posets= 407 n_profiles= {1: 1, 2: 2, 3: 7, 4: 40, 5: 357} integer_points= 36947 total_contact_occurrences= 3158
```

The checker generates all transitively closed partial orders compatible with a natural labeling on up to five elements. Every finite poset of at most five elements has such a labeling, so all isomorphism classes occur among these test inputs. The code compares the full sets of ternary signed-chain integer points with all antichain-indicator differences. It separately checks the second-width maximum and the equality/contact sets. Integer arithmetic is exact. The symbolic proof in `RESULT.md`, not these finite checks, establishes the theorem for all sizes and all real polytope points. No independent audit has been performed.
