---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For S any four-element F7 set, degree<2 polynomial evaluation gives 49 codewords. Seven constants are conflict-free against nonconstant distinct-symbol supports, so always included. Permute then delete causes two nonconstant codewords to conflict iff their four-symbol value supports share at least 3 symbols (including identical supports); complements are affine images of T=F7\S. AGL(1,7) gives progression/nonprogression 3-subset orbits sizes21 and14 with stabilizers 2 and3. Pairwise-compatible triples must have disjoint 21-bit unordered-pair masks. The finite C++ certificate independently examined all 2^21+2^14 orbit-family subsets and Python independent conflict search reproduced maximum packings of 6 (14 equality families) and 7 (2 equality families). Consequently M(S)=13 or14 and optimal labeled codebook counts 14*2^6=896 or 2*3^7=4374 respectively; exactly 21/14 evaluation sets have these types. All finite candidates are covered, not sampled.

## originality

PASS

PASS on current source record and primary-literature comparison for exact orbit-dependent F7 subcode capacity, 896/4374 equality counts and complete complement-triple packing types; affine symmetry and general permute/insdel machinery are known.

## value

PASS

An exact natural four-point first-nontrivial prime-field subcode invariant of a difficult permutation/deletion channel, with structural AP/nonAP dichotomy and complete optimal packings; mathematically more than a known general RS bound or arbitrary choice of a small subset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
