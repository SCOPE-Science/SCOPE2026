---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

All six facet distances, including the vertical half-height, are fixed at one; 0 <= c < 1 parametrizes that family up to congruence. The first pedal is the polar with exactly eight supporting planes indexed by the sign vectors; the second feet are their dual sign vectors divided by squared norm. In the orthogonal horizontal sum/difference axes the resulting four columns have radii A,B and half-heights h+,h−. A supporting functional of the projected diamond, slightly tilted vertically, exposes each endpoint. In any convex representation the total weight at the two Y-corners is at least |Y|/B, and this lower bound can be attained throughout the diamond; placing all mass on the upper endpoints therefore yields the claimed roof for h+ >= h−. This proves the four lateral quadrilaterals and four roof triangles for c>0 (two merged flat roofs at c=0). Section integration gives V=4AB(2h++h−)/3. Differentiation gives the stated quintic and positive prefactor; F′(c) <= 99(c−1)<0 before the excluded endpoint. Opposite endpoint signs and the rational bracket establish the unique interior global maximum; the cube gives 8/27, and V tends to zero as c approaches 1. An exact determinant test at c=3/5 gave 190/729 without floating hull triangulation, and the derivative replay reproduced c*=0.175097381279917 and V*=0.302143544127582.

## originality

PASS

Credit inversion of vertices, qualitative non-parallelepiped rigidity, and the cube endpoint to existing results. The explicit noncubical facet and volume profiles and the unique skew optimizer are supported as distinct, to the best of the inspected evidence.

## value

PASS

A single natural shape parameter ranges from the symmetric cube to near-degeneracy while all facet distances are fixed. The calculation gives a sharp counterexample to cube extremality on this family, a complete facet transition, and a unique maximizing geometry. The value is the structural comparison and exact optimizer, not the size of the percentage gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
