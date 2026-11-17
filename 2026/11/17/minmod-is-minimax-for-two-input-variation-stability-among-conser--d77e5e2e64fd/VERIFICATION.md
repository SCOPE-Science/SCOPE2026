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

# Verification record

The final theorem was checked in three separate ways: (i) symbolic polynomial identities \(\max A=4/27\), \(\min B=-4/27\), \(\int|A'|=\int|B'|=8/27\), and nonnegative central kernels at all four extreme selector states; (ii) explicit finite-support secant witnesses achieving \(43/27\) for every tested positive rational decrement; and (iii) 6,000 random rational two-input samples whose continuous variation was computed by integrating quadratic derivatives between their real roots.

The independently runnable `check_minimax.py` is included and uses only the Python standard library. On replay it printed:

```text
EXACT_BASIS_EXTREMA_AND_CENTRAL_BERNSTEIN_PASS 43/27
FOUR_SHARP_SINGLE_JUMP_WITNESSES_PASS 43/27
RANDOM_TWO_INPUT_BV_STRESS_PASS 6000 max_sample_ratio 1.296296296
UNIVERSAL_LOWER_BOUND_SYMBOLIC_INEQUALITIES_PASS
ALL_MINMOD_HERMITE_MINIMAX_CHECKS_PASS
```

The mesh tests and random experiments are finite. The all-selector lower bound and arbitrary-length upper bound are established analytically in `RESULT.md`. The checker uses floating-point quadratic roots for random tests and exact rational arithmetic for the decisive algebraic identities and witnesses. It is not an external or independent mathematical certification. Any historical-priority conclusions remain qualified by the inspections in `REVIEW.md`.
