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

# Reproduction and boundaries

Run `python verify.py` with a standard Python 3 interpreter. The verifier independently constructs the hypercube edges as bit flips and checks that the syndrome assignment has precisely the claimed counts of each color among the neighbors of every vertex. It covers 106 feasible triples across dimensions \(1\le d\le12\) and up to 16 colors. It additionally exhausts small surjective colorings for dimensions \(1\le d\le3\), checking both possible and excluded palette/tolerance pairs in 14 instances.

Expected output:

```
EXPLICIT_CONSTRUCTIONS_DIRECT_NEIGHBOR_COUNTS_OK 106
EXHAUSTIVE_SMALL_PALETTES_OK 14
VERIFY_OK
```

These checks do not establish the infinite theorem; its necessity follows from positive off-color counts and equal-size color classes, and sufficiency follows from the explicit linear map in `RESULT.md`. The theorem does not assert that every coloring is linear, nor does it certify historical priority or independent mathematical validation.
