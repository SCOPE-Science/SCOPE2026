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

By symmetry of the heat semigroup, the absolute defect optimized over c is the operator norm of the difference of the two observable functionals, i.e. the Euclidean least-squares residual. Its next-functional normalization is the sine of the angle between successive snapshots. At s_j−1,s_j the consecutive affine-exponent differences select mode j+1; at s_j+1,s_j+2 they select mode j. The winners are unique: the crossing times are decreasing, separated by four and are half-integers. Writing η=min_j(ν_{j+1}−ν_j)/2>0, every competing exponent at those snapshots is at least η below the winner, by telescoping. The normalized distance from a snapshot to its winner is at most √(m−1)exp(−Lη), so a common sufficiently large finite lag gives all strict inequalities, with the proposed limits by orthogonality. Reusing the old minimizer at the next burn-in gives E_L(s+1)≤e^(−Lν_1)E_L(s); distinct semigroup eigenvalues and all nonzero modal coefficients imply a strictly positive residual at every finite step. Independently compared normalized snapshots with the wedge-product formula in dimensions 2, 4 and 8 at lag 30, as a numerical supplement only.

## originality

PASS

The absolute one-delay approximation is covered in prior heat-closure work, and spectral crossover engineering is shared with an earlier Resultary record. The supported distinct claim is the multiple prescribed integer peaks of the relative optimal one-delay operator-norm defect, including the near-one peaks and near-zero neighbors despite absolute contraction. Neither overlap supplies that conclusion as stated or by the checked reductions.

## value

PASS

This separates two explicit operator measures of one-delay reliability on a standard heat semigroup. It shows that absolute contraction at every update cannot certify even eventual improvement through a prescribed long sequence of relative-quality checks in growing dimension, and quantifies the distinction by neighboring windows with opposite limiting quality. This is useful as a boundary on what a closure error bound means, not as a claim about typical sensors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
