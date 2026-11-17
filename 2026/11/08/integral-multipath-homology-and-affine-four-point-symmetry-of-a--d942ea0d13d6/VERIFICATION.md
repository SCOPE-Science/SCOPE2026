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

Two independent combinatorial validity predicates in the package cover all 2^12=4,096 arc masks and agree. An independent implementation reproduced 278 nonempty faces, f=(12,54,104,84,24), and mod-two reduced Betti ranks (1,4,4) in degrees (2,3,4). The package verify.py was read: integer signed boundary columns satisfy d²=0 and Schur-complement cancellations use only unit ±1 pivots (counts 11,43,60,20 in degrees 1..4), leaving free zero-differential groups Z,Z4,Z4; this excludes hidden torsion. Every one of 24 vertex symmetries induces an oriented simplicial permutation. The checker calculates their chain-boundary-image traces over p=1009 and recovers the rational homology character; dimensions at most 4 uniquely fix integer traces from residues. Character is (1,q,epsilon*q) for q the action on F2^3/<111>. Its averages yield fixed dimensions (1,1,0). No infinite family or integral lattice representation is claimed.

## originality

PASS

Specific exhaustive Resultary searches for cyclic tripartite blow-ups, affine four-coset representations, 12-arc multipath complexes, and homology ranks (1,4,4) found no earlier covering record; the only exact match indexed was this assigned 2026-11-08 finding. The checked general multipath frameworks concern different directed paths, polygons and acyclic comparison theorems. Originality is best-of-knowledge, not a consequence of an empty search.

## value

PASS

A natural minimal cyclic layered digraph demonstrates how excluding directed cycles produces higher integral homology and a nontrivial full finite-group representation, separating the degree-limited join S2 from the actual complex. These exact invariant and symmetry facts answer a motivated structural question beyond a routine textbook substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
