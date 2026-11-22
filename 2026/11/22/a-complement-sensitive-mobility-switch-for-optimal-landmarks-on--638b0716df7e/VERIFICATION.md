---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The claim is a structural theorem for the 16-vertex, 5-regular Clebsch graph and its 10-regular complement. Its primary correctness evidence is the complete proof in `RESULT.md`: the generator-sum representation, distinct-signature incidence bound, intersecting-two-subsets star/triangle dichotomy, explicit unresolved triangle witnesses, and exact common-neighbor argument for the star bases. The 16-component exchange decomposition and both slide graphs follow from neighborhood intersection and independence; no experimental extrapolation occurs.

Two independent scripts were executed from their exact included source paths with Python 3. `verify_binary.py` uses the five-generator Cayley construction and checks strong regularity, all smaller resolving sizes, all 1,820 four-subsets, 80 metric bases, 120 independent four-sets, 160 jumps, 0 slides on the original graph and 160 slides on the complement. `verify_incidence.py` independently constructs an isomorphic graph from a center, five singletons and ten pair-vertices, then independently enumerates and verifies 80 bases, 16 neighborhood families and the two distinct slide graphs.

Observed result from each: `verification=PASS`. Both scripts require only the Python standard library. They are finite consistency checks, not external independent mathematical audits. Exact graph, adjacency condition, landmark size, move rules, and complement convention are defined in the result and code. A related 2019 publisher full text was not accessible; research priority remains qualified.
