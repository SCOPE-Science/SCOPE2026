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

# Verification of the sharp ordered-variation comparison

The complete proof in `RESULT.md` establishes the theorem for every integer \(n\ge2\). The standalone `checker.py` is an independent finite-instance corroboration using rational arithmetic, not an exhaustive proof over the continuous family of all stochastic matrices.

Run `python3 checker.py` in this directory. The completed execution returned:

```
EXACT_SHARP_ALL_DIMENSIONS_N2_TO32_AND_THREE_SMOOTHINGS_PASS 93
EXACT_LOWER_EQUALITY_POSITIVE_KERNELS_PASS 62
EXACT_MONOTONE_RANDOM_KERNEL_BOUND_CHECKS_PASS 1320
ALL_ORDERED_MARKOV_COEFFICIENT_CHECKS_PASS
```

The checker computes exact ordered tails and row-pair total variation. It checks \(n=2,\ldots,32\) for all sharp examples and 1320 exact-rational mixtures of increasing deterministic maps. The proof of the universal comparison is the combinatorial vertex argument, not these samples. This verification does not cover arbitrary partially ordered state spaces, non-monotone matrices, or independent scientific priority.
