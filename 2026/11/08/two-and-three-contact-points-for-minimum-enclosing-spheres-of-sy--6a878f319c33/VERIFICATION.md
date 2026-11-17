---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Endpoint midpoint E and odd half-difference O are orthogonal, giving radius lower bound S. Setting x=t²/a², for even d and a²<=1 the coordinatewise bound (1−x^j)^2 <= 1−x^(2j−1) proves every curve point within ball centered E, and strictness aside from the stated contacts. For even d and a²>1, exact identity R²−||γ(t)−λE||²=Σ a^(4j) x^j(1+1/M−x^j−x^(j−1)/M) proves strict containment for 0<x<1, while λE is the strictly positive barycenter of 0 and two endpoints at equal radius, proving uniqueness/minimality. For odd d, pairing even terms with preceding or following odd terms (depending M<=1 or M>=1) bounds distance by S strictly except at |t|=a. Strict convexity excludes all other hull contacts. Fresh independent rational coordinate-norm checks (2460 distances) corroborate equations; they are not the unrestricted proof.

## originality

PASS

Best-of-knowledge original all-real-parameter enclosing-ball contact theorem; an earlier same-moment-curve source gives only Euclidean diameter envelope for integer parameter subsets, a genuinely weaker metric quantity and parameter domain. Konoike cyclic-polytope work inspected at abstract level emphasizes Ehrhart geometry, but full text unavailable and retained as priority risk.

## value

PASS

A sharp dimension-parity and real-scale contact transition for the canonical metric realization of cyclic polytopes, with a closed minimum-ball center/radius valid under arbitrarily many interior insertions. The two-vs-three support-point phenomenon is a concrete structural result useful for computational convex geometry and metric polytope comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
