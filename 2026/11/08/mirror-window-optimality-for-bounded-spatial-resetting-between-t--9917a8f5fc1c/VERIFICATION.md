---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For D,L,R>0 and reset site a∈(0,L), the proposed piecewise C² value V satisfies V(0)=V(L)=0, derivative and second derivative matching at a and L-a, and D V″+min_{0≤u≤R}u(V(a)-V(x))=-1. The strict signs V(x)<V(a) outside (b,L-b) and > inside prove bang-bang selector for b=min(a,L-a), with centered a=L/2 correctly yielding zero resetting. A uniform exponential tail follows from a positive-probability no-proposal Brownian boundary hit in fixed blocks under any bounded predictable reset rate; stopped Dynkin gives E tau≥V, equality for feedback proves all-starting-point adapted-control optimality. Independently symbolically verified C² matching, HJB identities, and sign at a=.3,L=D=1,R=4; proof handles arbitrary parameter and controller, no finite lattice extrapolation.

## originality

PASS

Generic HJB resetting-control mechanisms and one-target nonresetting windows are earlier literature; the fully evaluated two-absorbing-end first-exit boundary problem, mirror window (b,L-b), finite-ceiling independence of switching locations and exact tanh value are distinct from the inspected prior statements. Potential unindexed exact two-exit treatment is retained as risk.

## value

PASS

Solves a natural constrained continuous-time stochastic-control problem exactly, producing a simple implementable optimal policy against even history-adapted strategies and closed-form rate-dependent benefit. The two absorbing endpoints change geometry, and fixed switching coordinates are a structural observation not routine one-target reuse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
