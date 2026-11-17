---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The simplicial faces are precisely subsets of 20 open 9-neighborhoods in J(6,3), with 8,621 augmented faces. Independently regenerated faces, 4,238 toggled pairs, critical cells (one 0, one 2, 142 3), and all 142 signed integer Morse degrees: 95 zero, 30 +2, 17 -2, so gcd 2. Source verifier explicitly constructs and topologically sorts all 41,940 nonempty Hasse arrows. Its graph acyclicity and unit incidence recursion are mathematically appropriate. The 2-skeleton is S2, so 142 attaching maps are integral degrees, reducing by unimodular changes to degree 2 plus 141 zero attachments. Thus the claimed Moore wedge follows, not just field Betti numbers.

## originality

PASS

Best-of-knowledge no earlier covering exact open-neighborhood Johnson Moore homotopy identified; the closest Johnson theories have different simplex tests.

## value

PASS

This is a natural first 20-vertex middle-level Johnson graph, and its common-neighbor complex unexpectedly realizes 2-primary integral torsion in degree two despite a high-dimensional pure triangulation. The precise Moore summand and 141-sphere count are not implied by known clique/closed-neighborhood calculations and are a useful benchmark for topology of graph Hom/neighborhood complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
