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

With all edges positive the support lies within an exact-four partition; no internal cycle can be shattered since negating one edge leaves a positive path between its endpoints. At ≥3m−1 edges, m−1 spanning four-vertex trees can be kept positive while an edge in the remaining block is negated. The trees force all the other blocks, so those endpoints are still together. For the lower bound take m−2 three-edge stars and two two-edge stars in disjoint nominated fours. Positive cores have vacancies s_i and e_i free unqueried leaves (e_i=1 for the last two groups, 0 otherwise). A negative token forbids just its own core. Any vacancy set meeting multiple cores sees all tokens; a one-core set gives exactly 2s_i≤∑s_j+e_i. Failure in a full star forces s_i=3, both deficient capacities 1 and all other full capacities 0; put the offending center with one deficient core, one offending leaf with the other, and the remaining two leaves with the two free tokens. Failure in a deficient star forces s_i=3, its partner at 1 and all full capacities 0; put the offending center with the partner core and its two negative leaves with the two free tokens. All blocks and negative separations check in both cases. For m=2 only the latter exception can arise; m=1 is a singleton class of VC dimension zero.

## originality

PASS

The distinct contribution is the all-m exact-four law and constructive packing for m≥3, not the previously covered m=2 boundary or the trivial singleton case, both excluded from priority credit. The closest size-cap, two-block, uniform-triple and fixed-count results do not imply the new regime.

## value

PASS

This is a motivated exact capacity-constrained VC invariant, not an isolated finite example. The upper deficit from the size-cap class measures a real saturation obstruction, and the explicit optimal support and two exceptional packings are useful witnesses for subsequent constrained shattering and general block-size analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
