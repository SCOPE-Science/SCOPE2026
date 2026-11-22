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

# Verification of the directed-edge Euclidean volume claim

The standalone `verify.py` runs using only the Python standard library. Run `python verify.py`. The expected final line is:

```
UNICYCLIC_DIRECTED_ROOT_METRIC_PASS orientations=1144 graphs=10 special_energy=[10,26] balanced_means=4,6,8,10 leaf_extrema_t=1..15
```

The verifier constructs the actual oriented incidence vectors of ten unicyclic graphs and evaluates exact Gram determinants using fraction-free integer elimination. It tests every orientation (1,144 cases total): when the cycle is unbalanced, it checks the squared factorial-scaled full-dimensional simplex volume against \(n\delta^2\); when balanced, for every cycle-edge deletion it checks the squared factorial-scaled simplex volume against \(n\sum_v h_v^2-(\sum_vh_v)^2\). Its checks do not assume the asserted determinants.

The same program tests the exact four-cycle pendant-height identity and both sharp finite-orientation extrema for all integer leaf counts from one through fifteen. It separately tests exact integer moment identities for balanced pure cycles as an additional stress check. Low-dimensional Euclidean convex hull volumes were also computed numerically independently for both dimension cases, and matched the derived expressions to floating point precision.

These tests are not infinite certificates. The general graph claim follows from the spanning-tree Gram determinant, affine-circuit triangulation, and Euclidean height calculation in `RESULT.md`, and the sharp family statement from discrete optimization and a lattice-basis sign-flip map. Neither formal proof certification nor independent scientific audit has been performed.
