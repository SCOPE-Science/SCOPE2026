---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The actual Pappus graph has 27 edges and 2597 nonempty independent faces (f-vector 18,126,438,801,756,348,90,18,2). The source gives a full 1293-pair acyclic Morse matching to one vertex and ten degree-four cells, and exhaustive 216-automorphism enumeration. Independent graph-automorphism and signed simplicial Lefschetz calculations reproduce the complete trace distribution {-2:21,-1:72,0:54,1:32,2:36,10:1}, zero character mean, and norm squared 2. Hence rational degree-four homology has two distinct irreducibles; the source and earlier detailed proof identify their dimensions 4 and 6. This is exhaustive for the specified finite graph, not a claim for all cubic Levi graphs.

## originality

FAIL

The 18 October 2026 full-Pappus symmetry result computes the same G=Aut(P), |G|=216, complete rational H4 character, exactly trace multiset -2:21,-1:72,0:54,1:32,2:36,10:1, two absolutely irreducible modules of degrees 4 and 6, and no invariants. Its normal C3 decomposition is stronger. The new 13-class labeling and examples are re-expression, not additional character information.

## value

FAIL

The full 216-element character and two-irreducible decomposition have already been computed with stronger canonical module identification. A second enumeration and different class indexing are reproducible but do not resolve an unknown invariant or meaningful gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
