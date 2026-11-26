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

The affine conversion x_e=(1-χ_e)/2 gives equality of the real degree filtrations. In the fan at 0, the diagonal (0,2j) separates the two triangles in the quadrilateral with cyclic vertices (0,2j-1,2j,2j+1); the r=floor((n-2)/2) such quadrilaterals have disjoint interiors. Simultaneous independent flips therefore give 2^r distinct valid triangulations, with each indicator depending on at most one flip bit. A monomial of degree <r omits a bit, so its alternating sum cancels by pairing that bit. The uniform parity measures differ on the event that all replacement diagonals occur, since exactly one bit pattern qualifies. For finite sharpness I independently generated size-(n−3) compatible subsets by the alternating-endpoint crossing test and retained all size-≤r compatible subsets as features; no use of the frozen recursion or flip traversal. Exact row elimination modulo 3 gave (rows,features,rank) for n=4,…,10 equal to (2,3,2), (5,6,5), (14,31,14), (42,71,42), (132,441,132), (429,1078,429), (1430,7351,1430). Replay: python3 -I independent_polygon_rank.py from the review workspace root; equivalently recursively take each next higher-ordered diagonal from those compatible with all previously taken, set the row entries for the subsets of that triangulation, and eliminate over F_3. The row counts agree with Catalan enumeration, and full rank over F_3 certifies a nonzero integral minor, hence full real row rank. This does not assert that intermediate modular ranks equal the real ones. Full rank gives unique measures. More generally a nonzero real left-kernel vector sums to zero since the empty monomial is present; normalizing its positive and negative parts gives two equal-data measures. The explicit parity vector specifically certifies degrees <r, not possible larger deficient degrees for n>10. No general equality for n≥11 is needed or established.

## originality

PASS

The result concerns the saturation degree of the finite Boolean evaluation ring of triangulations in the labelled diagonal coordinates. Structural associahedron results, compatible-face counts, full Walsh transforms in the same coordinates, and filtered ranks in a different Catalan encoding do not cover the actual degree cutoff. The lower bound uses a specific independent-flip family, and the finite cutoffs are genuine exact ranks rather than face counts.

## value

PASS

The minimum joint observation degree is a natural invariant for exact recovery of arbitrary mixtures on a standard combinatorial family. The independent-flip construction supplies explicit indistinguishable probability laws for a degree growing linearly with n; the exhaustive calculation settles the matching threshold through the nontrivial 1430-state case. It is not an enumeration of triangulations, a single-state identification algorithm, or a noise-conditioning claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
