---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Affine transform to fractional hypersimplex Q_{n,q}, q=(n-|t|)/2, lists all vertices as permutations of k ones plus a fractional r. Strict convexity forces endpoint vertices. Rearrangement and equality cases separate disjoint supports from odd central fractional overlap, yielding squared diameter 8(k+r²) outside odd plateau and 8k inside it, with counted unordered endpoint pairs. Independently enumerated exact rational vertex pairs for n=3..8 across selected integral and fractional q including central limits; all matched exact diameters and factorial pair counts. Actual frozen verify.py examined.

## originality

PASS

The all-real-offset Euclidean diameter and enumeration of every diametral vertex pair are explicitly classified, including odd central plateau and jump loci. Searched combinatorial cube-slice reconstruction, minimum-width and hypersimplex facial thickness do not logically imply this maximum-distance metric pair count. Direct vertex-pair enumeration through n=8 supports the proof. Historical priority is best-of-knowledge and remains provisional.

## value

PASS

The natural metric diameter graph of cube slices has a complete nontrivial classification over continuous real offsets, with an odd-dimensional plateau and discrete jumps in the multiplicity of extremizing pairs. These fine Euclidean properties are not determined by ordinary face-lattice graphs or minimum width; useful in metric convex geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
