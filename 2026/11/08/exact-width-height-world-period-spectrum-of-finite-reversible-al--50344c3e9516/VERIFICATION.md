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

# Reproducibility checks

Run `python3 checker.py` and `python3 spectrum_check.py` with Python 3's standard library. Both were executed from the packaged source content, with success output:

```
EXHAUSTIVE_POSETS_OK 242 419
CONSTRUCTIVE_MODELS_OK 286
INDEPENDENT_PERIOD_SPECTRA_OK 32
```

The first number counts labelled nonempty posets through four points and the second all automorphisms of them (including identity). The construction count covers positive periods through 120 subject to its width loop. The independent script compares permutation order sets in products of symmetric groups on layers to the bin-packing characterization for capacities one through eight and heights one through four.

The proof for all finite orders and all positive width, height and size caps appears in RESULT.md. Finite checks, while reproducible and useful for catching boundary issues, are not infinite proofs. An independent mathematical audit has not been performed.
