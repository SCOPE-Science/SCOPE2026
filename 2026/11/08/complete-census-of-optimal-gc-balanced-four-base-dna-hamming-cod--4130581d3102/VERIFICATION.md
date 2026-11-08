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

# Verification notes

With `verify_masks.py`, `verify_graph.py`, and `optimal_codes.json` in one directory, run:

```
python3 verify_masks.py
python3 verify_graph.py
```

The first performs exhaustive choices by GC mask (40 by 40 by 4 by 4), checks pair distances, counts all sixteen optimal closed codebooks, verifies eight-plus-eight palindrome split, five symmetry orbits, 512 orientation-selected conventional optima, and exact distance spectrum. The second enumerates every maximal clique on a freshly derived 44-vertex RC-orbit compatibility graph, verifies there are 704 maximal cliques and precisely sixteen weight-12 optima, and compares all maximal code lists against the first artifact.

The ordinary mathematical upper bound is proved separately by the fixed-GC-mask argument in `RESULT.md`; the two finite programs enumerate all its equality cases. Completeness rests on their explicit enumeration loops and graph recursion, not on a sampling hypothesis. The result has no assertion for longer words or different distance models. The unobtained full text of the relevant 2012 article remains a historical-priority limitation.
