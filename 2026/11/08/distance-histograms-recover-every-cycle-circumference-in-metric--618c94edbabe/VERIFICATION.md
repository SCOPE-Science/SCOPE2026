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

# Executable and analytical checks

Run `python3 verify.py` with the Python standard library. The code is included in this package, not referenced through any external repository. Its independent two-point simulator directly samples individual weighted graph edges, computes endpoint distances with shortest paths, and compares empirical CDF values with the independent symbolic block formula. Rational arithmetic checks formulas exactly at numerous non-knot radii. Four geometries include one bridge, a cycle, a cycle with a bridge, and a cactus with three cycles, two of equal circumference, and two bridges.

The successful execution printed:

```
GRAPH 0 total 3 cycle_lengths {} max_abs_CDF_err_so_far 0.004119
GRAPH 1 total 5 cycle_lengths {Fraction(5, 1): 1} max_abs_CDF_err_so_far 0.004476
GRAPH 2 total 7 cycle_lengths {Fraction(5, 1): 1} max_abs_CDF_err_so_far 0.004476
GRAPH 3 total 163/10 cycle_lengths {Fraction(5, 1): 2, Fraction(3, 1): 1} max_abs_CDF_err_so_far 0.004476
CACTUS_VERIFICATION_OK exact_mass=4 exact_density_derivatives=316 jump_groups=4 independent_pairs=140000 max_abs_cdf_error=0.004476
```

The exact checks include all four graph CDFs saturating at one, exact derivative identities away from knots, and exact recovery of the one-sided cycle-jump coefficients using two rational perturbation scales whose continuous affine parts cancel. The 140,000 sampled distances yield the stated empirical CDF discrepancy. Finite tests and random samples do not prove the general theorem, which relies on the rigorous blockwise decomposition. At isolated density breakpoints, the density value itself is irrelevant; the proof and tests use one-sided limits. The complete weighted graph is not asserted recoverable from the pair histogram.
