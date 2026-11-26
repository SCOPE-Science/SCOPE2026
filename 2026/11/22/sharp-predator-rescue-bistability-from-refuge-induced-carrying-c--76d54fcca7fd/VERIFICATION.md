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

At a positive equilibrium the predator equation gives (h-mu*delta)X=mu(1+q), q=beta*Y. Thus h<=mu*delta precludes positive equilibria; otherwise X=T(1+q) and the prey equation on this nullcline reduces to alpha F(q)/(1+q), with F=1-rho+(1-eta)q-rho*q^2. The constant term, vertex and discriminant yield the stated counts for rho<1, rho=1 and rho>1, including exclusion of zero roots and the positive fold only at positive eta. At a positive root, the Jacobian determinant has the sign of -F'(q): H_X>0 for the predator per-capita term and H_q=-T H_X. For the trace, set phi=rho(1+q^2)/(1+q). At a positive equilibrium, 1-phi>0 and the prey diagonal term is alpha[-phi+(1-phi)delta*X/(1+delta*X+q)]. In the wedge and on its positive fold phi>=rho*2(sqrt(2)-1)>1/2, so this diagonal is strictly negative uniformly over delta*X/(1+delta*X+q) in (0,1); the predator diagonal is also negative. The lower root is a saddle, the upper a sink. The predator-free invasion eigenvalue is negative iff rho>1 when T exists, and its other eigenvalue is -alpha. At the positive repeated root the nullcline elimination is regular because H_X>0; restricted to its tangent, the quadratic and a-parameter derivatives are nonzero (F''=-2rho and dF/da=-q*deta/da), and the other eigenvalue is strictly negative. This gives a nondegenerate saddle-node, on the wedge boundary rather than inside it. The origin is an additional boundary equilibrium, not one of the three specified states; the census classifies positive equilibria.

## originality

PASS

There is substantial demonstrable same-model coverage: a distinct same-day record proves the identical census and local types on the normalized subfamily delta*K=1. No historical order is inferred. Credit is limited to the full positive-parameter result, notably that the sharp stability wedge and positive saddle-node classification persist for arbitrarily varying the independent saturation group delta*K. Pure rescaling to unit prey capacity and unit refuge scale leaves this group in the off-nullcline vector field and trace. The positive-root geometry alone is shared and is not credited as a new mechanism.

## value

PASS

The homogeneous classification for the originating model is useful beyond a fixed normalization: it determines that changing saturation relative to physical prey capacity cannot switch the positive attractor to an unstable branch anywhere in the sharp wedge at fixed rho and eta. This stability robustness across an independent model group, together with the fold and the negative invasion rate, is the useful extension, not another instance of the already known normalized bistability phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
