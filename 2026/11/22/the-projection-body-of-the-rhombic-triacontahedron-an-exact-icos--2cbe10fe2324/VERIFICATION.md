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

The area formula for planar zonotopes gives support ∑|u·(v_i×v_j)|, hence segments [-c,c]; the factor 8 in the volume is required. Independent exact replay: work in integer pairs (A,B)=A+Bφ with φ²=φ+1, form each determinant as a scalar triple product, and compare (2A+B)+B√5 to zero by signs and squared magnitudes. The 20 source minors have 10 each of 2φ and 2+2φ. The 455 image minors have absolute values 0,4φ²,4φ³,4φ⁴,8φ³ with multiplicities 70,100,180,100,5. Sum these and multiply the second sum by 8 to obtain the claimed volumes and ratio. Checking the 105 image generator pairs gives 31 unoriented normal lines with 15/10/6 perpendicular direction sets of sizes 2/3/5 and exactly the stated pairwise absolute cosines. Equal-length distinct generators at these planar angles give regular 4-, 6- and 10-gons. Independently the 30 signed image generators are the six axial vectors of length 2φ and all sign choices of cyclic permutations of (φ²,φ,1); divided by 2φ these are the unit H3 roots, yielding the uniform truncated icosidodecahedron. Doubling opposite facet counts gives 30/20/12 faces and then 180 edges and 120 vertices by double incidence and Euler. The original axes are opposite vertex-pairs of a regular icosahedron; no three are coplanar, and the generator pairs give congruent golden rhombi. The exact metric statements use the displayed normalization; affine covariance preserves the quotient but not face regularity under general affine changes.

## originality

PASS

The surviving contribution claimed in the record is the concrete unpolarized projection-body correspondence and the exhaustive real metric triple spectrum in that normalization. The zonotope operator formula, the solid's face data and edge-normalized solid volumes are classical. The ratio is a short evaluation once the correspondence and scale are identified, not an independent advance on the bound. A particularly close earlier certificate computes the exact arithmetic norm census of the same projective H3 arrangement and its incidence counts; it does not determine the normalized real absolute determinant frequencies from its stated data.

## value

PASS

The canonical icosahedral six-generator zonohedron is a natural test of the sharp projection-volume bound, and the map to the uniform H3 zonotope ties that affine quotient to a concrete metric generator model. The complete real determinant spectrum resolves volumes of the constituent rank-three generator parallelepipeds and their frequencies, information a total volume or an incidence/field-norm table cannot supply. That fixed-root-data benchmark is useful independently of a new general inequality. Recomputing only the two standard solid volumes or facet counts would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
