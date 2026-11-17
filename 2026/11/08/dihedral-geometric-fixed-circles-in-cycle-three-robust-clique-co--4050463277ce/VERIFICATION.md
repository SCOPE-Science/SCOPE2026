---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Geometric fixed points are exactly orbit-barycenters when supports are unions of vertex orbits: exact PL identification, not vertexwise fixed subcomplex. For n>=6 every face has at most four original vertices because five vertices force an independent triple; admissible 4-subsets have a two-edge perfect matching. Rotation order>=3 supports no orbit; order2 halfturn gives cycle C_{n/2}. Odd reflections have singleton plus paired orbits yielding C_{(n+1)/2}; even vertex-axis C_{n/2+1}, edge-axis C_{n/2}. n=3..5 K is a full simplex, so all element fixed sets contractible. I independently enumerated all orbit-face complexes for n=3..14 and all dihedral elements; they matched the exact f-vectors and classes. Inspected source verify_dihedral_fixed.py checks n<=35. Unlimited claim rests on orbit/matching proof, not the samples.

## originality

PASS

The same complex has known ordinary S3 homotopy and dihedral homology orientation, but neither implies PL geometric fixed circles. Explicit subgroup-element geometric circle shapes and polygon cardinalities were compared with prior work, including broader bipartite k3 result; found no coverage in material read, not a guarantee against unindexed geometry sources.

## value

PASS

The natural three-robust clique sphere on cycles has published homology characters, but geometric PL fixed sets can differ despite identical Lefschetz data. Explicit polygon fixed triangulations and axis-dependent sizes for all cyclic lengths are a meaningful and potentially reusable exact structural classification beyond low-cost orientation traces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
