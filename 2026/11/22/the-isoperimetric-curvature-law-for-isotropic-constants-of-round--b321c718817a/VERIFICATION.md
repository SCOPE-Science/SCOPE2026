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

I checked the edge moment identity using centered vertices: the mean of xxᵀ on the opposite side is S/6 for each side, while Q₀=A S/12; the first variation therefore cancels the area normalization. The strip contribution to Q₂ is A I by the divergence theorem, and the sector and moving-centroid terms give the traces in (12)–(13). An independent way to see the coefficient is to compare with the homothetic triangle obtained by translating all three support lines outward by t. Its area is A+Pt+(P²/4A)t², and its J stays 1/108. Relative to circular rounding it adds exactly (P²/(4A)-π)t² in area, confined to O(t) neighborhoods of the original vertices: a point in the excess cannot project to an edge interior because the offset support constraint would force its distance to be at most t. Each vertex has the same leverage vᵀQ₀⁻¹v=8/A, and centering corrections to the difference of second moments enter only at order t³ because the original centroid is zero. Thus removing the excess area D t² changes J/J(0) at order t² by -8D/A+4D/A=-4D/A, giving the claimed coefficient. The outer area and moments are polynomial in t near zero by strip/sector integration, so the one-sided derivatives are justified, not inferred from just a pointwise remainder. The inner support-line shift is exactly an incenter homothety for -r<t≤0. The sharp triangle perimeter inequality gives the equilateral equality case and positivity of the deficit; the right curvature and known area determine the positive perimeter.

## originality

PASS

The equilateral specialization is already covered by the exact regular-polygon formulas. The supported distinct claim is the single deficit law for all nondegenerate triangles, including scalene ones, and the sharp consequences in that larger class. Closely related same-day records do not establish the general triangle identity. No historical-priority assertion is made.

## value

PASS

Across all triangle shapes a priori shape-dependent second moments and moving centroids reduce to one classical deficit. This links an affine invariant under a Euclidean perturbation to a recoverable Euclidean perimeter and gives a sharp equilateral extremizer after scale normalization. The distinction between inner homothety and outer corner rounding is structural; the value is not in redoing the regular case or claiming global monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
