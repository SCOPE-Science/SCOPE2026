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

# Verification details

The scripts use Python 3 standard library only. From a directory containing `check_spider.py` and `check_equivariant.py`, run:

```
python3 check_spider.py
python3 check_equivariant.py
```

The first directly enumerates matching faces, augmented simplicial boundaries and rank reduction over the field of two elements for all 765 tested spider profiles, comparing each Betti vector to the formula. The second enumerates invariant oriented simplices for all 146 checked automorphisms and compares integral signed Lefschetz traces to the predicted representations, including mixed-length equal-arm swaps. Successful recorded outputs are in `verification_output.txt`.

The computation is finite and does not exclude integral torsion beyond the tested finite chain complexes. The uniform integral statement rests instead on the written proof of the mapping-cone decomposition, path homotopy recurrence, join orientation signs and primitive augmentation sequence. No external independent audit was performed.
