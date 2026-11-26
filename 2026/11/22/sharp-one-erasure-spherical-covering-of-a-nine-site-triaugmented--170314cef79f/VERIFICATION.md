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

This is one deletion, with two types of deleted site, in the intact triaugmented-prism chamber 1/2<r<1. All surviving vertices remain extreme, by the radial supporting functionals. For each erased hull the ten triangles and one quadrilateral support it strictly on the origin side, with equality exactly at the listed vertices. Euler's inequality f≤2v−5 for a hull with a quadrilateral makes the v=8 lists exhaustive. The central covering cosine is the origin-centered inradius, not the radius of a freely centered insphere. The new equatorial-deletion quadrilateral is the plane with first coordinate r/2. For prism deletion, if W denotes projection onto that prism site's horizontal direction, the quadrilateral is W+(1+r)z/(2h)=1/2, whose plane distance squared is A=(1−r)/(5−3r). The remaining squared distances compare as in the tables, giving min(1−r²,r²/4) and A, respectively. The sign of A−r²/4 is the sign of 2−3r, with A<1−r²; the competing cosine branches each have strict monotonicity on their own side and meet at 1/3. This proves the unique minimax parameter 2/3. As a separate within-family check, the prism plus its three pyramids has volume √3 h(2r+r²/2), whose derivative vanishes only at √3−1 in the chamber, so the contrast with the volume parameter holds directly. The cited global volume theorem was not independently checked. The independent exact SymPy replay /workspace/branches/8452ec81-00e1-4b3f-b62a-001edbfb54a3/facet_check.py checked every supporting sign, origin orientation, quadrilateral coplanarity and squared-distance identity over the open interval by algebraic factorization, as well as the controlling comparisons. The uploaded script was inspected, not executed.

## originality

PASS

The supported distinct result is the exact orbit-resolved one-erasure cosine and the minimax switch inside this fixed family. The available same-family results concern intact-body volume, inball or ellipsoid quantities. The critical erased facets are not even supporting planes of the intact configuration, and available other erasure formulas are for different codes. This is not a claim to have identified a global robust spherical code or established historical priority.

## value

PASS

The family is geometrically motivated by the nine-vertex volume problem, but failure of a site asks a different, natural robustness question. The exact radius quantifies the degradation, identifies which site type is critical and locates a sharp design parameter distinct from the volume optimizer. The emerging quadrilateral supports explain the comparison and make this a reproducible benchmark for erasure-robust covering, without extrapolating to arbitrary configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
