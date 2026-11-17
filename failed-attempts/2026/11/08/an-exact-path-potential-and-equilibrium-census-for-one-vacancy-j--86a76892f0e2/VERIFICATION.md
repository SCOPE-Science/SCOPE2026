---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The quotient by vacancy side and red count gives a consecutive integer interval I=[max(-1,2(r-b)),min(2r,2a-1)] with L_x=2x and R_x=2x-1. Every profitable jump crosses parts and moves one edge; its fixed sign depends only on the moving color, utility fraction and endpoint counts; reverse has negative sign. Summing edge signs gives strictly +1 ordinal potential for improvements, no repeated quotient states, at most H=tmax-tmin<=2min(a,b) improving jumps. Weak local maxima characterize equilibrium, and independent vertex/color/binomial counting gives displayed labeled equilibrium sum. Independently checked consecutive-state/bound identities for all side sizes 1..5 and red populations; for K_2,3 with nonmonotone type payoffs direct enumeration gave exactly 6 equilibrium colorings, matching the formula. These checks corroborate general proof; utilities arbitrary within two type classes only.

## originality

FAIL

Earlier October 26 and November 2 published records cover the same one-vacancy biclique game. In particular Nov 2 *Exact potential and sharp vacancy boundary* proves an exact potential for arbitrary type- and part-dependent nonlinear functions on complete multipartite graphs, hence all payoff functions in the assigned theorem; Nov 2 *One vacancy forces terminating jumps* explicitly builds the same bipartite two-color path of population states and establishes bounded universal convergence. The assigned path-sign potential is the edgewise orientation of the already published exact potential. Its labeled equilibrium sum is a direct binomial weighting of local maxima, and the 1-to-3 step tightening of the earlier uniform bound is not a substantive new theorem; no independent original final claim survives.

## value

FAIL

A path potential for arbitrary utilities and an algorithmic equilibrium census are meaningful in isolation, but here the decisive path structure and an exact potential in a stronger model were already published. The formula counting labeled equilibria is direct binomial weighting of the already-known quotient sinks; the new endpoint bound improves earlier O(min part) by at most a few moves without a motivated tightness or asymptotic change. As the assigned final claim, it is a routine deduction/renaming of prior structure rather than a distinct valuable research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
