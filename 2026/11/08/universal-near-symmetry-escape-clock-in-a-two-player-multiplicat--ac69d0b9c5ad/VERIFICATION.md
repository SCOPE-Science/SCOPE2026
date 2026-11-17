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

The exact log-odds update gives L(F1)−L(F2)=L(x)−L(y)+a(x−y), maintaining coordinate order. Solving the diagonal two-cycle gives t=1−2σ and a=8atanh(t)/t, strictly increasing from 8 to infinity. The transverse multiplier at either phase equals Λ=1+h, h=aσ(1−σ), while tangential multiplier 1−h has magnitude <1. In local symmetric/antisymmetric coordinates v grows by Λ times [1+O(center_error+v²)], while center error contracts plus O(v²); before fixed small exit, both perturbation-error sums are bounded geometrically, giving N=log(1/ε)/logΛ+O(1). Finite smooth preperiod from any diagonal start outside the .5 preimage set preserves a positive transverse multiplier. Differentiating h(t) proves γ decreases; σe^(a/4)→1 gives γ~ae^(−a/4). Independent iterates at gains 9,12,20 agreed with bounded-offset clock. No finite test substitutes for local-uniform proof.

## originality

PASS

Chotibut–Falniowski–Misiurewicz–Piliouras 2018 introduce the same map and prove diagonal convergence to a 2-cycle and off-diagonal convergence to pure equilibria; their transverse derivative and convergence are prior. The novel exact all-nonexceptional-start first-exit clock together with strict gain monotonicity and exponential large-gain slowdown was not stated in examined original theorem portions. A general hyperbolic escape principle is a mathematical dependency, but does not directly supply this map-specific γ(a) behavior. Priority risk remains for unindexed equivalents.

## value

PASS

The theorem quantifies how long seemingly symmetric two-player learning states remain near a transversely repelling cycle and identifies the counterintuitive exponential high-gain slowing. The strict universal coefficient across diagonal starting states is a motivated stability-timescale invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
