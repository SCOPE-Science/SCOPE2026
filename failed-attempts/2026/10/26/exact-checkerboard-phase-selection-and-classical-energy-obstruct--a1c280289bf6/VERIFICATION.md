---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Regular bipartiteness gives Ls=2rs, so on u=xs diffusion sends y=x^2 to exp(-2 delta t)y and reaction sends y to exp(2t)y/[1+(exp(2t)-1)y]. Composition gives numerator exp(2 alpha h)y and denominator 1+beta y, with beta=(exp(2h)-1)exp(-delta h) for DRD and (exp(h)-1)[1+exp((1-2 delta)h)] for RDR. The only positive fixed point is (exp(2 alpha h)-1)/beta; reciprocation gives an affine contraction of slope exp(-2 alpha h), and the amplitude sign is preserved. Factoring the exponentials gives the two stated sinh formulas. Strict increase of sinh(z)/z for z>0 gives the DRD bias and the RDR trichotomy, including exact preservation at delta=1/2. The graph energy restricted to the line is N[(y-alpha)^2+1-alpha^2]/4, so the classical energy strictly increases starting at the nonzero physical equilibrium exactly when the physical state is not fixed by the step. This argument covers each h>0, and attraction is confined to the invariant line. RDR at delta=1/2 is the explicit step-independent exception to the general step-size dependence.

## originality

FAIL

There is direct present-day catalogue coverage by the stronger all-integer-p statement in Sharp order-dependent stationary-pattern bias for Strang splitting on bipartite reaction–diffusion graphs. Its p=1 case on the identical graph class gives both laws, the entire bias trichotomy and attraction. The frozen energy counterexample is not in that statement, but follows directly from its exact fixed-point classification and evaluation of the standard energy at u=xs, where the physical fixed point is the unique minimum in y. This is equivalent or immediately implied coverage, not a finding of pre-freeze priority: the matching catalogue record is dated 2026-11-02, later than this frozen record, and the comparison does not establish which work was derived independently or first. The earlier inspected primary papers' modified-energy results do not themselves establish the frozen claim.

## value

PASS

The exact split equilibria matter for long-time computations. In particular, starting at a genuine nonconstant equilibrium gives a sharp counterexample to unqualified classical-energy dissipation at every positive step, without contradicting decay of a modified energy. The exceptional RDR parameter distinguishes the two common Strang orientations with no asymptotic or floating-point qualification. This structural example is useful even though its mathematical content is covered by the catalogue comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
