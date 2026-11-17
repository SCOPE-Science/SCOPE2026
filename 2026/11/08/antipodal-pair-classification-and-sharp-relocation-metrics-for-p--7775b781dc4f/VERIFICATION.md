---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the specified cyclic 12-vertex icosahedral graph an antipodal pair (u,bar u) has disjoint closed neighborhoods partitioning V. Sets {u,bar u,v,w} with v adjacent u and w adjacent bar u are paired dominated and matched. No 2-set dominates. Complete test of all 30 initial edges and 21 disjoint second edges proves every feasible matched 4-set contains an antipodal pair, so 6*25 minus 15 duplicate two-pair states =135, subclasses 60/60/15. Independently enumerated all C(12,4)=495 four-subsets and reconstructed reconfiguration graph on 135 valid states. Slide 360 edges, all ecc six; jump 720 edges, all ecc four. Exact finite graph proof, no general graph-family claim.

## originality

PASS

Haynes–Slater (1998) is founding definition only; complete full Teshima 2022 dissertation Chapter 2 constructs hosts realizing arbitrary paired-domination reconfiguration graphs but does not classify the unmodified Platonic icosahedron. Related Resultary triangular graphs and Kneser graphs are nonisomorphic hosts with distinct optimum-state spaces, so their formulas do not imply 135 configurations or 360/720 moves here. No equivalent icosahedron pairing census found in searched record database.

## value

PASS

Paired domination naturally requires a matched backup pair of guards and is meaningful on a canonical symmetric graph. Antipodal neighborhood partition yields a structural full optimizer classification; exact local versus unrestricted relocation diameters 6 vs 4 quantify a concrete mobility penalty, a natural finite exact benchmark not an arbitrary enumerated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
