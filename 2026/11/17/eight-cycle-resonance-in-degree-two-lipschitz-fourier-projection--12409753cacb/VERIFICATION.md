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
# Reproducible verification
Run `python3 verify.py` from the same directory as this document, with Python 3 and its standard library. No external packages are required.

The exact arithmetic checker uses rational interval enclosures of \(\pi\) from Machin's identity, rational cosine Taylor enclosures with certified remainder, and exact rational comparisons. The fifteen cases \(5\le n\le20\) with \(n\ne8\) pass the stronger ceiling \(B_n<163/100\). The remaining infinite range \(n\ge21\) follows analytically from the periodic-derivative variation bound and the verified rational comparison \(250/157+(44/(3\cdot21^2))(22/7)<17/10\).

On the recorded replay the checker reported:

```
CERTIFIED_FINITE_N5_TO_N20_EXCEPT_N8_PASS 15 largest_upper (13, 1.6270737478770116)
ANALYTIC_ALL_N_GE_21_RATIONAL_BOUND_PASS 1.6968810373203977
INDEPENDENT_SAMPLED_MEDIAN_N5_TO_N100_PASS
EXPLICIT_EIGHT_CYCLE_ZERO_SUM_NORMING_GRADIENT_PASS
ALL_FIVE_CHARACTER_LIPSCHITZ_PROJECTION_CHECKS_PASS
```

The numerical sampled-median comparisons are diagnostics, not proof of a universal inequality. The quotient-duality reduction, uniqueness of the invariant projector, continuous median identity, and infinite-range Fourier-series bound are proved in `RESULT.md`. The certificate covers only its listed finite dimensions. This verification is not an independent mathematical audit.
