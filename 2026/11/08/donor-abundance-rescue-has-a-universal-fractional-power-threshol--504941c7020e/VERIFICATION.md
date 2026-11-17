---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For positive trajectories weighted logarithmic identity d log(u*v^p)/dt = u/(m+u) -(e-B)-(h+B)u is exact and checked symbolically. Positive equilibria are roots a<b of an explicit quadratic; Jacobian determinant sign distinguishes saddle (a,va) and attracting (b,vb), boundary (0,v0) is a sink. Dulac multiplier 1/(u^2*v^2) yields negative divergence (e-s-delta*(u+v)-u^2/(m+u)^2)/(u^2 v^2) under e<s, ruling out cycles while positivity and boundedness constrain omega-limits. The northwest stable branch moves monotonically backward in u downward and v upward and cannot terminate at a finite boundary equilibrium, giving a full graph psi for V>=va; strong cooperativity separates basin outcomes. Along branch, d log(psi(V)V^p)/dV is positive and O(V^-2), so H->finite positive C; integration of E/((s+delta)V^2)+O(V^(-2-p)) produces the explicit relative 1/V correction. Three numerical RK4 parameter examples and rational identity checks corroborate, not replace the planar proof.

## originality

PASS

Xia et al 2023 publish the same nonlinear model, equilibria, local stability and basin phase portraits; this is credited. The available source descriptions and sections inspected do not state the globally parameterized large-donor stable separatrix nor a universal fractional-power exponent and explicit next correction. Search of Resultary identified critical extinction and balanced-parameter studies of the same or related models, but none with this V->infinity rescue threshold. Thus best-of-knowledge PASS with significant publisher-full-text and unindexed phase-plane literature risks.

## value

PASS

Bistable donor-rescue threshold is a natural observable for nonlinear migration models; exact power law p=delta/(s+delta) and correction separate migration scaling from local Allee parameters, a substantive asymptotic description of the basin boundary. It is not merely checking equilibrium stability or renaming a local stable manifold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
