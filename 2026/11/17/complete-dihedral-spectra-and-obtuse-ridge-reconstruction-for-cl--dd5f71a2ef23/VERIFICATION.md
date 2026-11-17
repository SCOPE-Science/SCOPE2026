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

# Reproducibility and verification

## Analytical checks

The construction is fixed in the standard \(N\)-coordinate Euclidean zero-sum hyperplane. Every facet normal is derived from the explicit barycentric-coordinate formula. Three independent orthogonal projection families are calculated and summed, giving the exact Gram entries for the hub, a leaf diagonal, same-blade leaf pairs, and different-blade pairs. The cosine has an explicit negative sign for the supplementary interior angle. Strict inequalities are proved for all integer parameters \(s,m\ge2\); all ridge classes and the sharp \(m=1\) boundary are handled.

## Standalone finite replay

Run `python3 check_clique_windmill_angles.py` (Python standard library only). The checker builds each original Laplacian from graph edges, computes \(L^+\) independently by exact rational Gauss–Jordan inversion of \(L+J/N\), and verifies every entry of \((L^+)^2\) against the predicted piecewise formula. It checks \(2\le s\le6\), \(1\le m\le5\): 25 parameter pairs spanning 2,625 unordered facet pairs, maximum order 31. It also verifies strict positive-sign and ordering inequalities for the multi-blade cases.

Observed replay:

```text
CLIQUE_WINDMILL_ANGLE_PASS exact_parameter_pairs=25 all_ridges=2625 max_order=31
```

## Limits

Finite matrix experiments do not prove the general theorem; the all-parameter proof is the symbolic spectral calculation in RESULT.md. No formal proof certificate, independent mathematical audit, or global bibliographic uniqueness certification is asserted. The arbitrary unimodular lattice representation may change all Euclidean angles.
