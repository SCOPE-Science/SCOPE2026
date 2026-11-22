---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The graph T5=L(K5) has 10 vertices and 30 edges; its matching complex face counts (1,30,285,980,1020,144) exhaust all cardinalities zero through five. Independent reconstruction of the deterministic descending-edge discrete Morse pairing returned 1146 matched face pairs, 8 critical 2-simplices and 160 critical 3-simplices; an oriented Hasse topological sort visited all 2460 faces, establishing acyclicity. The remaining CW model has one vertex, no 1-cells and boundary B:Z^160->Z^8. Independent exact unit-pivot cancellations computed a 7x7 minor -1, 8x8 minor absolute 3 and rank7 modulo 3, forcing Smith nonzero factors 1×7 and 3×1, H2=Z/3 and H3=Z^152. Because the 2-skeleton is a wedge of eight 2-spheres and π2≅H2, integer elementary changes of the attaching maps give M(Z/3,2) wedge 152 S3, not just abstract homology. Independent enumeration of all 120 induced S5 permutations and their signed face Lefschetz traces gives character (152,0,4,-4,0,-2,-3), agreeing with multiplicity decomposition and zero trivial component.

## originality

PASS

The complete graph matching complex M(K10) studied by Jonsson has 45 graph edges, whereas M(T5) uses the 30 edges of L(K5); torsion of the larger complex does not transfer to its subcomplex. The Petersen graph is the complementary Kneser graph KG(5,2), whose edge matching complex has a different torsion-free sphere wedge. The four-cut complex of the same T5 graph has a different face criterion and a wedge of eleven S3, not the matching complex. No inspected source supplies this precise Moore-space splitting and S5 rational character. Remaining literature priority best-of-knowledge.

## value

PASS

T5 is a canonical strongly regular graph with S5 symmetry, and integral three-torsion in matching complexes is a structurally meaningful phenomenon. The classification M(Z/3,2) wedge 152 S3 proves a homotopy type stronger than Betti tables; the complete natural S5 character records representation structure. This motivated exact invariant of a natural graph is independently useful even without an n-family theorem, and it is not a generic tiny-instance rank check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
