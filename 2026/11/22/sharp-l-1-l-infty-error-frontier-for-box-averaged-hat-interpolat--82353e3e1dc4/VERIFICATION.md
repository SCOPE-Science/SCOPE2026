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

# Reproducibility

Run `python3 verify.py` using Python 3 and no external dependencies. The script builds the exact rational nodal box averages and continuous piecewise-affine reconstruction of one or more jumps, integrates each linear absolute-error segment exactly, and measures the maximum error from the two traces of every jump and the knot values. It checks all positive rational box widths with reduced or unreduced denominator at most 32 inside the stipulated range and 36,534 half-cell jump cases. It also checks sharp witnesses at every tested width, the \(3/2\) threshold and the \(49/96\) sharp uniform coefficient. A reproducible sequence of 2,500 randomly generated finite signed-jump functions checks both inequalities and the reconstructed-signal variation bound.

Expected terminal summary:

```
EXACT_PHASE_AND_WITNESS_CHECKS_PASS 36534
UNIQUE_L1_PRESERVING_LINFINITY_OPTIMUM_PASS alpha=3/2 c1=1/2 cinf=49/96
EXACT_SIGNED_MULTI_JUMP_AND_TV_DIMINISHING_CHECKS_PASS 2500
ALL_BV_BOX_AVERAGING_CHECKS_PASS
```

The proof in `RESULT.md`, not these finite tests, covers every real BV input, every positive mesh spacing and the full real bandwidth continuum. The computations are exact rational arithmetic for a bounded test set; no exhaustive claim is made over arbitrary BV functions.
