---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent proof check of RESULT.md lines 31–67: telescoping the independent avoidance probabilities gives x/N and x(y−1)/(N(N−1)) for x<y. Subtracting the marginal product gives the stated off-diagonal entries; the diagonal check gives Σ=N D/(N−1)−H/[N(N−1)], with H the inverse of the Dirichlet path difference matrix A. On the interior grid, B=A diag(x(N−x)) is self-adjoint in the weighted inner product; its action on the degree-d quotient of the polynomial flag is (d+1)(d+2), including the one-site grid. Inversion and conjugation give the claimed simple spectrum; the Rayleigh quotient gives both extremal weights. The finite normalized kernel and diagonal terms converge by Riemann sums. In the continuous problem −[t(1−t)p]'' preserves the polynomial flag with the same leading coefficient and is symmetric by integration by parts on t(1−t)p; weighted polynomial density gives completeness. The lower bound is attained by constants and the upper bound is sharp by high-degree modes. The supplied verifier was inspected, not rerun; its recorded 2617 assertions cover finite exact checks only.

## originality

FAIL

No earlier verbatim tree-spectrum statement was established. Nevertheless the claimed invariant is mechanically determined by the published leaf cross-moment and classical Hahn spectrum: the covariance entries are the Dirichlet inverse plus a multiple of the diagonal weight, and the weighted Dirichlet difference operator is exactly the Hahn operator plus 2I. The variance bounds are then Rayleigh quotients and the continuum claims direct Riemann-sum and Jacobi consequences. The result is correct, but the frozen claim does not establish a distinct result beyond these direct implications.

## value

FAIL

Variance by birth-label mode is a natural diagnostic, and the exact comparison with independent indicators is interpretable. But the reported gain is an elementary Green-matrix identification followed by application of the already tabulated Hahn law to known entries, with the bounds and continuum limit immediate from that identification. It does not meet the standard for a useful, previously undetermined exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
