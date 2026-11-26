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

The ordinary cut complex has a face exactly when its complement contains a disconnected triple. In the dual this means that the induced complement graph has maximum degree at most one: two missing edges of a triple share a vertex, and conversely two missing edges incident to one vertex give a disconnected triple. Fresh exact code tested this matching condition for every mask, then computed the augmented boundary ranks modulo 3. Those ranks are lower bounds on rational ranks; the resulting reduced mod-3 homology is supported in just one degree for every input. Rational homology is therefore zero elsewhere, and the Euler characteristic fixes the remaining rank. Alexander duality transfers the degree by n−d−3. The frozen integral calculation uses genuine unit pivots: the Schur complement and deletion in the adjacent maps follow from the chain identity after isolating the unit pair. The fresh replay concerns rational homology, not an independent torsion test. For each dihedral element, its fixed space is the complex of orbit unions that are faces of the original complex, since fixed barycentric coordinates are constant on each vertex orbit. The reduced Euler characteristic of this fixed space equals the reduced Lefschetz trace; alternatively, an invariant simplex on j vertices and m orbits contributes (−1)^(j−1)(−1)^(j−m)=(−1)^(m−1). This bypasses the ambient orientation twist in the dual formula and independently reproduces all 264 character entries. After barycentric subdivision there are no inversions; the rational quotient chain complex is the coinvariant chain complex of the subdivision, and averaging is exact. The independent character averages give the rotation ranks 1,0,3,6,4,1,1,0 and the full quotient ranks 0,0,0,4,4,0,0,0. For n=20 the rotation traces equal 2cos(2π·2k/20)+2cos(2π·6k/20) and both reflection traces vanish, so the stated real constituents describe the rational representation after extension of scalars.

## originality

PASS

The distinct claim is the equivariant window for the ordinary three-cut complex: complete rational characters and the ranks on the geometric orbit spaces for p=5, 13<=n<=20. The nonequivariant homology table and nonshellability range are prior results, not claimed as new. Verified general character results start at n=27 for p=5, and the source for the sharp shellability threshold does not determine the characters.

## value

PASS

The eight cases form the entire naturally determined nonvoid nonshellable range for the fifth power, not an arbitrary cutoff. The character resolves behavior invisible from known Betti ranks: a nonzero rational class survives the full geometric quotient only at n=16,17, with rank four in both, and the n=20 rotation action separates the two real constituents. This is independently useful equivariant information for these ordinary cut complexes, not a recomputation of their nonequivariant table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
