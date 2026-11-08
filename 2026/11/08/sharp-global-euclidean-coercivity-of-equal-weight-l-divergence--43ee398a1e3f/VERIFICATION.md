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
# Verification and limits

The theorem is proved for every integer \(n\ge2\) and all \(p,q\in\Delta_n^\circ\) by a range minimization, convex chord bound, zero-sum norm inequality, and an elementary hyperbolic comparison. The sharpness construction remains strictly inside the simplex for every approximant. The worst-case-growth consequence requires a nonempty compact forward-shift-invariant path space and an explicit cumulative squared-increment lower bound for all starting times.

## Executed checks
Running `python3 verify.py` on the standalone file embedded in the same package yielded exactly:

```text
VERIFY_OK exact_grid_pairs=68982 range_enumerations=39000 randomized_simplex_pairs=19800 boundary_sharpness=81 two_cycle_checks=24
```

The script separately evaluates the original L-divergence expression, the proposed quadratic lower bound, finite range-midpoint bounds, range-to-total-variation estimates, two-coordinate asymptotic sharpness, and dynamical two-cycle sums. Its deterministic pseudorandom generator makes the additional cases reproducible. The checks were executed before packaging, directly from the same standalone script that is embedded here.

## Epistemic limitations
These are finite numerical and rational-grid checks with floating-point logarithms; none independently proves the continuum inequality or historical originality. The analytic proof is the only universal justification. A potential originality risk is earlier specialized work on sharp logarithmic Jensen-gap inequalities under simplex normalization not located by the recorded searches. Independent validation has not been performed.
