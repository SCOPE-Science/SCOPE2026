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

Put m=n+1 and v_i=e_i−1/m on the sum-zero space H. The frame operator of the v_i is I_H. For u_i=Tv_i with unit circumradius, tr(TᵀT)=m. The opposite facet has distance 1/(m||T⁻ᵀv_i||), since ⟨v_j,v_i⟩=−1/m for j≠i. With A=(n/m)TᵀT the resulting traces are n and 1/(nh²) for A and A⁻¹, and the normalized volume is √det A. At h=1/n, equality in the reciprocal-trace Cauchy–Schwarz inequality forces A=I. Otherwise the spectral feasible set is compact away from zero and the two gradients are independent. Stationarity for log determinant gives a quadratic in each eigenvalue. With roots x>y the Lagrangian Hessian is negative at x and positive at y. A difference of two coordinate directions for a repeated root is tangent to both constraints; the second-order necessary condition rules out repeated x at a minimum and repeated y at a maximum. The eigenvalue ratios y/x=t² and exceptional multiplicity one give h⁻²=n²+(n−1)(1/t−t)² and the printed product formulas. For actual attainment, a balanced unit sign vector q∈H has |⟨q,v_i⟩|²=1/m for every i. Thus the two deformations along its rank-one projection preserve vertex uniformity and, using their inverses, facet-distance uniformity. In every equality case equal vertex lengths force these same coordinate squares, and any balanced signs differ only by permutation, giving congruence by the polar decomposition. As h↓0, t∼√(n−1)h gives both constants and powers. An independent arithmetic check at n=5,t=1/2 gives h⁻²=34 and the stated extremal trace pairs; the supplied rational Gram checker was inspected, not executed.

## originality

PASS

The creditable claim is the global odd-dimensional three-center volume envelope with actual attainment and unique congruence classes, not the three-dimensional result, general coincidence of simplex centers, or spectral optimization presented as a new matrix inequality. The closest available statements concern different spectral objectives, specific geometric families or lower dimensions. Even prior coverage of the relaxed determinant extrema would not settle whether simultaneous equal-vertex and equal-facet diagonal conditions can be attained and uniquely enforced in the claimed regime.

## value

PASS

At fixed inradius and circumradius the volume is not determined even under all three center constraints. The sharp extremes identify how degeneration can proceed at two distinct asymptotic powers and rigidly specify the corresponding endpoint shapes. The balanced-axis argument explains the odd-dimensional regime beyond a stand-alone determinant computation; this directly answers a natural extremal geometry question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
