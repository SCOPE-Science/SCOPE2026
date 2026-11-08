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

# Reproducible checks

Run `python verify_torus_law.py` with Python 3 and NumPy. It verifies an exact rational reflection/basis identity, constructs numerical Voronoi polygons of seventeen flat torus lattices, checks forty-six facet-distance threshold groups against the analytic square-root coefficients, and independently compares ten radial CDF estimates against 75,000 directly sampled quotient point pairs per comparison lattice.

Observed execution:

```
VERIFY_OK exact_reflection_isometry=1 polygon_cases=17 facet_threshold_groups=46 max_signature_relative_error=7.0705357e-05 independent_pair_cdf_checks=10 max_cdf_error=0.00225397
The checks use orientation interval unions; all-lattice validity requires the analytical proof.
```

These finite tolerance-based checks support the independent implementations of the relevant geometric formulas; they do not prove the all-lattice reconstruction theorem. The theorem's proof is given in `RESULT.md` using exact angular interval geometry and planar Voronoi classification. Dependencies: NumPy, Python 3 standard library. No other files are needed.
