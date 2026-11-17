---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: The restricted quadratic form in a central plane has eccentricity squared equal to its eigenvalue gap divided by the larger restricted eigenvalue. There are exactly four oriented circular-section normals at (±sqrt((β-α)/(γ-α)),0,±sqrt((γ-β)/(γ-α))); linearizing the gap in two tangent coordinates yields radial slope 2sqrt((β-α)(γ-β))/β. Four disks of radius (β/[2sqrt((β-α)(γ-β))])ε² give Cε⁴. Min–max gives M=1-α/γ; explicit perfect-square identity yields the sharp bound and involution β→αγβ/((α+γ)β-αγ). Exact rational check of (1,2,4) vs (1,4/3,4) gives M=3/4,C=1/2; spheroid formulas follow from uniform directional cosine. Fixed triaxial shape only; no uniform gap-merger claim.

## originality

PASS

PASS, best knowledge: Classical circular planes, full cross-section aspect-ratio histograms, and spheroidal distributions are acknowledged; inspected material did not supply the exact quartic fixed-triaxial near-circular probability, coefficient or full two-statistic inverse nonuniqueness. This is distinct from a random affine offset section. Residual risk from older stereology literature, including not fully accessible Hayes/Landrø technical details.

## value

PASS

PASS: Recovering three-dimensional shape from random two-dimensional sections is a natural inverse-stereology problem. A sharp quartic rare-event coefficient and its exact two-to-one ambiguity with maximal eccentricity show precise information loss; this matters for statistical identifiability and distinguishes triaxial from rotationally symmetric cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
