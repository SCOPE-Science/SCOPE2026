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

## Actual verification

`python check.py` completed successfully from the extracted candidate package. It verified the exact symbolic reference-element matrix and row sums, a sharp boundary-conditioning witness, 300 deterministic nonsingular affine shapes under nonzero drift, and 16 assembled Dirichlet-grid cases; plus arbitrary signed Péclet and positive diffusion edgewise perturbations; total count: 2,233 check conditions. The analytical proof establishes the quantified statement, not the finite sweep.

The main assumptions are an affine, nondegenerate parallelogram, bilinear/Wachspress basis, the complete six-edge IBEAM local discretization, positive edgewise diffusion, arbitrary real edgewise Péclet labels, and a three-by-three-or-larger uniform cell array with outer Dirichlet vertices. The classification is of the \(M\)-matrix property, not of all possible inverse-positive matrices. Publication-priority risk remains for unindexed equivalent classical quadrilateral-mesh conditions. Independent audit has not been performed.
