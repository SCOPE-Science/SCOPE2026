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

# Reproduction and limitations

Run `python3 check_inertia.py` with Python 3 standard library. The file enumerates every positive composition of total size from 1 through 7. For each composition, it enumerates all within-layer permutations (every linear-extension chamber), builds the order-polytope simplex vertices and their piecewise-affine transfer images in the chain polytope, and integrates each coordinate product over the simplex using the barycentric moment formula. All quantities use `fractions.Fraction`, not floating point.

Recorded direct execution result: `ORDER_CHAIN_DIRICHLET_SIMPLEX_CHECKS_PASSED 127 1813 1981 21`. The program made 127 independent composition checks of the inertia-gap identity and 1,813 within-layer covariance-entry comparisons. The same run also made 1,981 fixed-height extremizer-profile checks through eleven coordinates and 21 exact two-level vertex-reflection checks. Those counts refer to executed tests, not to any exhaustive statement for unbounded dimension.

Independent analytical checks: the transfer's inverse and triangular unit Jacobian are explicitly proved in RESULT.md; each coordinate's order-statistic and spacing moments are independently derived from Dirichlet gaps; summation counts each triple of distinct layers once; and balancing transfers have an exact positive increment when two layer sizes differ by at least two. The proof covers all positive layer sizes without a computation cutoff.

The method assumes uniform volume measure, the canonical coordinate Euclidean metric and nonempty antichain layers. It does not establish analogous inequalities for arbitrary posets or for the full covariance matrices in the positive-semidefinite order. No independent mathematical audit has been performed.
