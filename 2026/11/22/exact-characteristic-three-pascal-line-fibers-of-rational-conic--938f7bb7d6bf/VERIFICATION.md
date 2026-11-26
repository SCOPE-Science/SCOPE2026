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

The standard conic is rational over each finite field here and PGL₂ acts sharply triply transitively. Chords at finite u,v have coefficients [1,−u−v,uv]; the two relevant intersections in the normalized order are proportional to [−ab,0,1] and [bc,bc,b+c−1]. Their joining coefficients and the characteristic-three discriminant are as stated. For A=a(b−1) nonzero, the reciprocal change is projective bijective, giving exactly the four exclusions. Recomputing their discriminants gives two squares at c=1,a, a linear expression in b at c=∞, and a quadratic in a at c=b (except for b=−1) of nonzero discriminant (b−1)^2. At c=b the two roots are b and b/(b+1)^2 for b≠−1; the latter is admissible. At c=∞ the zero b=(a+1)^2/a is admissible for a≠0,1,−1. The corresponding omitted character and zero contributions yield the three stated normalized totals. Rational-line type is transitive: tangency and split unordered pairs follow from the conic action; nonsplit conjugate pairs are transitive because any two nonrational degree-two parameters are related by a rational affine transformation using the basis 1,α. Divide by twelve for the free dihedral action on six distinct vertices and by the appropriate number of lines; all factors are positive for q≥9. A separately written F9 direct collinearity enumeration with i²=−1 found all 12,600 hexagons and precisely the claimed per-line multiplicities on 91 rational lines.

## originality

PASS

The three exact fixed-line rational multiplicities in characteristic three are the supported distinct claim. Credit the classical Pascal map and available geometric one-fiber description, and distinguish conditional tangent/secant existence from counts for all three types.

## value

PASS

The distribution by rational-line orbit, including the exceptional nonsplit case and the sharp smallest field, is a natural arithmetic invariant of the Pascal map. It gives actual fibers rather than a mean or possible image. The small-characteristic change in the exclusion arithmetic makes this more than routine continuation of the adjacent-field formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
