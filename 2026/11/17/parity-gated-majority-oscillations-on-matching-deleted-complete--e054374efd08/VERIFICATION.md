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

For every missing-edge pair (a,b), its common neighborhood contains S-a-b ones among N-2 vertices; a universal vertex x sees S-x ones among N-1. The exact tie rules give consensus off critical levels and an involution on central balanced states when u is even. For even u, the middle layer has binom(2r+u,r+u/2) periodic states and either 2^r extra fixed states only when u=0 or no balanced fixed states when u>=2; fixed and 2-orbit formulas follow. For odd u, only S=h or h+1 can avoid immediate consensus; every pair becomes 00/11 and universal bits agree after one update. Counting the possible alternating pair profiles yields u=1, odd h with h=r+(u-1)/2, and the parity/size extinction conditions for u>=3; after at most three updates any nonperiodic configuration enters a uniform consensus. An independent literal-neighborhood binary state enumeration r=1..4,u=0..4 (up to 12 vertices) matched fixed counts and primitive 2-cycle formulas; the exact weighted pair-profile verifier source independently establishes finite instances.

## originality

PASS

Earlier published cocktail-party plus one-universal-vertex result already determines u=0 and u=1 exact cycle populations; these special cases are explicitly credited. The new full unbounded u>=2 parity-and-availability criterion, even-u balanced-layer family, and extinction/reappearance for odd u>=3 were not found as corollaries of accessible broader complete-multipartite majority results. Best-of-knowledge PASS with clear prior art and residual risk.

## value

PASS

The mixed-size multipartite graph K_{2^r,1^u} is a natural, sharply parameterized family bridging cocktail-party graphs and complete graphs. An exact all-r,u oscillation phase diagram proves that increasing universal-vertex count can eliminate and later restore periodic disagreement depending on parity; closed cycle formulas and uniform three-step bounds are independently useful natural invariants, beyond the known u=0/u=1 examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
