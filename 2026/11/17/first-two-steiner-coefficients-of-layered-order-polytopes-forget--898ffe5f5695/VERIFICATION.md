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

The order-simplex triangulation with prod a_i! simplices proves volume. Facets are exactly bottom coordinate, top coordinate, and adjacent-layer comparisons; their unit normals yield n(2+k sqrt2) surface/vol. Verified the four exhaustive ridge-face classes BB, BE, same-interface shared-endpoint EE, distinct-interface disjoint EE with normalized measure 2,2k sqrt2,k sqrt3,k(k-1). Overlapping adjacent-interface edges and disjoint same-interface comparisons force extra ties and are not ridges. Normal angles are pi/2 except same-interface sharing endpoint pi/3. In V_(n-2)=sum area(phi/2pi), the class totals yield formula for every k=r-1 and a_i>=2. Recomputed formula at r=2,3 and unequal profiles. Source SciPy convex-hull verifier independently checks 16 finite profiles (1356 ridges), not an exhaustive proof. Intrinsic volumes use standard Steiner convention kappa_2=pi.

## originality

PASS

Originality best-of-knowledge: Stanley triangulation/facet theory and Ahmad-Fourier-Joswig combinatorial ranked poset f-vectors are earlier; they do not determine weighted Euclidean ridge measures. Related Resultary chain-polytope Steiner theorem is for distinct (noncongruent when r>=3) object and has different constants. Related rankwise chain-order interpolation apparently covers the first boundary area but does not yield the second intrinsic volume formula, so that portion of claim survives. Full mathematical priority unknown.

## value

PASS

The size-independence of two metric normalized Steiner coefficients is surprising given distinct individual layer sizes and facet numbers; the second coefficient requires a complete natural ridge classification and weighted curvature cancellation. It is a potentially reusable exact intrinsic volume for canonical order polytopes, not merely a textbook volume computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
