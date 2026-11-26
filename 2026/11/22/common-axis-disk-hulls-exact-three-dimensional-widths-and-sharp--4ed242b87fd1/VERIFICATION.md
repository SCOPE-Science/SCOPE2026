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

The original calculations are mathematically consistent; the substantive repair changes the contribution, not its coefficients. For the retained m>=3 case, support maximization and central symmetry give the range and formula. At the minimum set delta=w^2/4-1/m; for Y_0=a the simplex in the m-1 remaining independent transverse coordinates has volume [m delta-(m-1)a]^(m-1)/(m-1)!, with 0<=a<=m delta/(m-1). All transverse squares are 1/m+O_m(delta), strictly positive for small delta, so the product Dirichlet density is a^(-1/2) times a uniformly smooth factor. Integration with B(1/2,m) and delta=epsilon/sqrt(m)+epsilon^2/4 gives the repaired coefficient and relative O_m(epsilon) error. At the upper edge the single-circle neighborhoods each have a Beta((m-1)/2,1) lower tail, and overlap forces the sum of all m transverse squares below 2(1-w^2/4). The Beta(m/2,1/2) estimate controls the total overlap at the stated order. The original m=2 density follows by differentiating the CDF, and rotational symmetry gives the stated second moment using E|cos(2 Phi)|=2/pi; these are no longer contributions. The repaired comparison also derives the weak limit from the appropriate Dirichlet-maximum scaling and independent normalized transverse vector. The frozen numerical checks were inspected but not executed; the asymptotic assertions follow analytically.

## originality

PASS

The frozen originality claim is not accepted as stated: its complete two-disk law is a direct specialization of a spherical cap-intersection formula, and its growing-dimensional law follows from a Dirichlet maximum theorem and the one-coordinate limit. The corrected claim in /workspace/repairs/3/RESULT.md and SLOGAN.txt is the pair of fixed-dimensional endpoint laws with exact leading constants for m>=3. The covered comparisons are no longer claimed as contributions. No inspected result states or mechanically supplies the retained common-axis endpoint coefficients together; obtaining them requires the local slack-simplex and overlapping-circle estimates for this statistic.

## value

PASS

The corrected result compares extremal directional rarity on a natural all-dimensional convex body. Exact constants and error orders quantify an isolated lower-edge set with a singular density direction versus multiple intersecting upper-edge circles. This gives both endpoint probabilities for every m>=3 rather than treating the known two-disk CDF or the Dirichlet limit as novel or relying on a minor numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
