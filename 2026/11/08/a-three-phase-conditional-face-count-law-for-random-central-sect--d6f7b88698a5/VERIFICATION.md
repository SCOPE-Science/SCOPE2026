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

PASS. For a Haar normal U and unit cube, W=sum_i|U_i| and the central section is a hexagon iff all three positive |U_i| satisfy the strict triangle inequalities (equivalently max|U_i|<W/2), else a quadrilateral outside null equality surfaces. Parameterizing the width-s small circle around (1,1,1)/sqrt3 gives spherical measure ds dphi/sqrt3. For 1<s<sqrt2 the allowed positive-octant arc length is 2pi-6 arccos q(s); for sqrt2<s<sqrt(8/3) quadrilateral arcs have length 6 arccos(q(s)/2); for larger s no such arc exists. Dividing by octant area pi/2 produces exact f4,f6 and conditional 1,3arccos(s/(2sqrt(6-2s²)))/pi,0. Limits match at both sharp boundaries; integrated f4=0.649040687816... and f6=0.350959312184..., sum1. Numerical integration and direct circle/edge-crossing checks corroborate but do not prove the spherical geometry.

## originality

PASS

PASS for the genuinely joint conditional law. Lonke's section-vertex expectation fixes only the cube's unconditional quadrilateral probability; Finch's width moments and a previously published exact cube-width density fix only the width marginal; published exact Haar hexagon probability for boxes fixes polygon-type marginal. The same Haar normal couples the two observables, and knowing both marginals cannot imply their joint allocation, especially the exact threshold pair sqrt2 and sqrt(8/3) and the strictly decreasing conditional law. No source actually read contains this joint cube formula. A differently named stereological conditional distribution remains a residual priority risk.

## value

PASS

PASS. This is a natural complete joint law of two measurements made on the same random central planar section, determining which combinatorial types are possible at each observed width, with exact sharp all-width trichotomy and nontrivial mixed-phase probability. It is not a recomputed unconditional polygon frequency or width density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
