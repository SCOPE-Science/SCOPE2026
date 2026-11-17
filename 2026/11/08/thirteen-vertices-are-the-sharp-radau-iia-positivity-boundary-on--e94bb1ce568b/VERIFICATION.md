---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For conference graphs with N=4t+1 vertices and SRG parameters (4t+1,2t,t-1,t), the adjacency relation A^2=tI-A+tJ and Laplacian relation L^2=(4t+1)L-t(4t+1)I+tJ reduce the two-stage Radau IIA heat update to I-alpha L+beta L^2. Exact interpolation yields positive denominator D, and strictly positive adjacent/nonadjacent transitions for h>0. The only sign obstruction is its common diagonal numerator P_t(h)=t^2(4t+1)h^4-4t(t-1)(4t+1)h^3+(-8t^2+40t+6)h^2+(24t+24)h+36. For t=1,2 P_t positive; for t>=3 P_t(0)>0,P_t(2)<0,P_t(infty)>0 and two coefficient sign changes give exactly two simple positive roots. Consequently positivity loses then reenters on exactly one bounded interval; no vertex-transitivity needed. The rescaled polynomial limits give t h_-(t)->3/2 and h_+(t)->4 along existing graphs. Independent Sympy expansion rederived diagonal interpolation identity and checked P_t(2) signs for t=1..99, including t=3 P(2)=-180; the root-count and infinite asymptotics depend on the analytic proof, not those finite checks.

## originality

PASS

The two-stage Radau stability rational function and strong regular graph spectral algebra are known, but the exact all-parameter conference-graph diagonal reentry threshold and asymptotic scales are not implied by examined general RK positivity theory or prior complete-multipartite Radau families. Conference graphs are typically primitive SRGs, not covered by multipartite classifications. Novelty qualified against unindexed association-scheme diffusion papers.

## value

PASS

Positivity of a graph heat integrator is mathematically meaningful because a negative transition violates order preservation despite stability and unit row sums. Determining exactly where it first fails for every conference graph, proving a single negative band and two asymptotic scales, produces a sharp graph-family theorem beyond a tiny-instance witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
