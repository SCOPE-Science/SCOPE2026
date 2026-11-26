---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Positive conductances and leaf killing make A SPD. Let m_j=|S_j|. Radial invariance and the nonzero coefficient -w_j on the next shell make K_k exactly the span of shell indicators through level k-1. Independently, for 1<=k<=H, set the trial solution x equal to zero from level k onward and prescribe its difference from level j to j+1, j<k, to be (1-B_j/B_k)/(m_{j+1} w_j). The total outward flux at level j is then 1-B_j/B_k. Subtracting the incoming flux gives (Ax)_root=1-1/B_k, (Ax)_v=-1/B_k on levels 1 through k, and zero outside. Killing contributes nothing to this trial vector. Thus the uniform-ball residual is attainable, and its ball indicator is annihilated by A on levels below k, making the residual perpendicular to A K_k by symmetry. Its squared norm is 1/B_k. k=0 is the root point mass; at H+1 invertibility on the full invariant radial subspace gives exact termination, with none earlier. The d>=3 count sums a geometric progression and d=2 has two vertices per nonroot shell. Constant and root coordinate Rayleigh quotients give the stated conditioning bound as killing vanishes. The frozen verify.py is a finite exact-rational check (the package reports 10,602 assertions on 879 trees), inspected but not executed for this review; the independent flux and orthogonality argument handles the universal quantifiers.

## originality

PASS

Credit standard minimum-residual Krylov theory and prior endpoint formulas. The support, uniform amplitudes and weight independence for the full class were not established by the compared prior statements. This is a bounded priority assessment of the structured graph law, not of the underlying Krylov machinery.

## value

PASS

The point-source grounded-tree problem gives an exact structured Krylov benchmark for an infinite family: the residual is an entire vector fixed by volume growth, not just an estimate. It identifies precisely when branching changes preterminal norm rates and gives an explicit family with diverging condition number and unchanged exact residuals. It is not a finite-precision or solution-error claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
