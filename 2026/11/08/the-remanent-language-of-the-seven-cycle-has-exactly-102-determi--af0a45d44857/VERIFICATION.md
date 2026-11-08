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

The exact computation is reproducible using only Python 3's standard library:

```sh
python3 checker.py automaton_certificate.json
```

The checked certificate enumerates all 128 seven-cycle orientations, all reachable states of their simultaneous subset product after collapsing failure configurations to one rejecting sink, both signed-word transitions, every shortest access word, and the final state partition. The checker compares a freshly generated transition table and Moore refinement to the certificate. A separate, direct oriented-graph-walk implementation verifies every word of length at most ten. The complete proof uses the exhaustive 230-state construction and stable 102-block partition; checking only length-ten words would not establish the infinite-language claim.

Expected output:

```
VERIFIED: 128 orientations; 230 reachable subset states; 102 minimal states; baselines 6, 18
```

This verification is reproducible computation, not independent external validation. No claim about arbitrary cycle sizes, external priority certification, or unseen code execution is made.
