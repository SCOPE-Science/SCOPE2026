---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For t>=1 the refractory rule makes E_{t-1} disjoint from E_{t+1}. Every excited vertex at t has at least theta neighbors in E_{t-1} and so at most Delta-theta neighbors in E_{t+1}; counting edges E_t--E_{t+1} gives theta e_{t+1}<=(Delta-theta)e_t. Initially e1<=floor(Delta*n/(Delta+theta)), so the integer excitation count vanishes once the real geometric envelope is <1, with one final refractory-clearance step. For theta=Delta, e2=0 and total rest by time three. Layered bipartite predecessor-successor graphs with sizes |L_h|=1, |L_{h-1}|=theta, |L_j|=ceil(theta |L_{j+1}|/(Delta-theta)) and modular adjacency realize one travelling excited front per step and have maximum degree Delta; total vertices grow as (theta/(Delta-theta))^h, giving sharp logarithmic worst-time coefficient. Independently verified all modular predecessor degree bounds for four parameter pairs, including (3,2),(5,3),(7,4),(8,5).

## originality

PASS

Prior maximum-induced-edge-density theorem with rho(G)<=Delta/2<theta already implies qualitative extinction and a linear event budget, not the exact per-step geometric factor or sharp log(n) clock with layered extremizers. Doba 2018 applies only threshold-one excitation on connected graphs; its phase-winding classification does not cover theta>Delta/2. Distinct dynamical statement and best-of-knowledge original.

## value

PASS

The half-maximum-degree regime is a natural critical parameter split for excitable systems. A sharp logarithmic time complexity rather than mere eventual extinction, plus matching constructed extremizers, is a meaningful quantitative refinement relevant to deterministic network relaxation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
