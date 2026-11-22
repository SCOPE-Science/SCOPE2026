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

# Reproduction

Copy `verify.py` and `forcing.tsv` alongside this document; run `python3 verify.py` with Python 3.9+ (standard library only). The certificate is a deterministic sequence of 55 forced necklace representatives. Every step is checked against all remaining compatible rotations by independent regeneration from binary four-subsets of 13 coordinates. All proper overlap lengths, both directions and self-overlaps are checked. Expected output:

```
VERIFY_OK 55 unique_oriented_optimum 1 nodes 1
```

The computation proves the complete finite claim for length 13; it does not prove corresponding claims at other lengths. The paper-construction and priority comparisons remain qualified as described in REVIEW.md.
