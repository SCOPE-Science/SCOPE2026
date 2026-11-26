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

RESULT.md lines 70–100: projection of 0 onto the convex hull of equal-norm roots gives a covering ball of squared radius 2−||c||², and averaging squared distances with any edge decomposition of c forces every other center's required squared radius to be strictly larger. Reflecting right coordinates is orthogonal; uniqueness enforces block symmetry. To check sufficiency of the Hall inequalities directly, assign x₃ to (3,1), satisfy y₃ from (1,3), distribute x₂ among the remaining V₁,V₂ capacities, then finish with U₁. Block flows lift by uniform allocation to the complete cells. If a vertex coordinate were zero, connectivity gives an adjacent positive vertex; redirecting a small positive edge weight at that vertex to the zero endpoint lowers the norm to first order. Thus positivity constraints are inactive. Centering the two Hall normals within each side gives the displayed K as their Gram matrix. They are independent by their different left-side steps; strict feasibility is witnessed by putting nearly all left and right mass in U₁,V₁. The stated cases solve the 2×2 complementarity problem, with exclusive positive supports and consistent zero-multiplier boundaries. The norm increase is λᵀKλ=λᵀδ. In 2(u_i+v_j−||c||²), this identity cancels the constant terms, leaving the two displayed allowed-cell indicator terms, with the stipulated sign for squared-radius clearance. Direct substitution gives λ=(2/23,1/23), norm correction 1/46, R²=34/23, and the three opposite-diagonal contacts for the worked example. The frozen rational checker is a finite, statically inspected consistency check, not a proof or an independent computation.

## originality

PASS

Supported claim is the explicit quantitative two-cut classification, not the equal-norm reduction, Hall inequalities, or generic KKT. The directly relevant earlier single-cut theorem does not determine the active-active case. The inspected general minimum-norm framework supplies algorithms, not the explicit formulas, contact sets or the specification of which inequalities suffice for these margins.

## value

PASS

The six-parameter formula answers the next nested-neighborhood case after a genuine one-cut result. It gives the exact metric invariant together with which edges attain it and identifies when a positive Hall deficit is inactive because of the other cut. That interaction and the three-cell contact set make the classification more than the two single-cut cases or a generic projection algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
