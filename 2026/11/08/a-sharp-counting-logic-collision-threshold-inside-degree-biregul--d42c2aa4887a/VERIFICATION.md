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

The degree constraints partition the graph into degree-3 centers and degree-2 stubs, the latter inducing a perfect matching. Each stub pair joins two distinct centers by a three-edge path or closes a triangle at one center. A cycle/parallel pair in the center skeleton would induce a nonclique biconnected block, so it is a tree with degrees 1 or 3. Its i internal degree-3 vertices and i+2 leaves create 2i+2 centers plus 6i+6 stubs: graph order 8i+8. Deleting skeleton leaves bijects the isomorphism types with subcubic unlabeled trees on i vertices. Degree partition is equitable, with neighbor-count quotient [[0,3],[1,1]], hence joint 1-WL stable histogram, and therefore C² equivalence, depends only on i. First nonisomorphic subcubic trees occur at i=4 (P4 and K1,3), order 40; explicit distinct families persist for every i>=4. Independent networkx unlabeled-tree enumeration gave 1,1,1,1,2,2,4,6,11 for i=0..8.

## originality

PASS

General color-refinement/C² equivalence is known, as is the appearance of smaller collisions among unrestricted chordal, block and 2-tree families. The submitted statement explicitly concerns this exact uncolored degree-incidence-defined block-graph subclass; none of the inspected published results classifies its skeleton by all subcubic trees, proves 8i+8 census, or implies the sharp relative first collision at 40. No claim of global first collision is accepted. Distinct relative-vs-absolute logical quantifiers were checked. Potential unindexed tree-gadget encodings remain a bounded historical risk.

## value

PASS

A complete infinite structural parametrization of a natural exactly degree-biregular block-graph class, together with an exact logical-equivalence spectrum and sharp first relative collision, is a motivated classification rather than an arbitrary tiny counterexample. A researcher studying stability of C²/color refinement on chordal/block families can use the exact 40-vertex boundary and infinite indistinguishability construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
