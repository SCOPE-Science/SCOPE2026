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

For the normalized conic parametrization, the opposite chords give Pascal coefficients [−z, x(y+z−1)+z, −xyz]. Distinct vertices give distinct opposite-side intersection points, and the quadratic conic restriction has discriminant z²D with z nonzero. For distinct y,z outside {0,1}, the x-quadratic discriminant has character χ(y(y−1)z(z−1)); it is nonzero, and the linear cases y+z=1 have character sum zero and one root each. Removing x=0,z subtracts two sets of square values. The x=1 and x=y exclusions factor into the two stated products; their sums are both −2q+6+χ(−3), giving A_S−A_E=−3q²+20q−33−2χ(−3). For tangencies, the two deleted zero sets have q−4 members each; the resulting A_T is (q−4)(q−5). The nonsplit line orbit is transitive, since an affine F_q transformation can send any nonrational parameter in F_{q²} to another, carrying conjugates along. The other two orbits follow from transitivity on conic points and pairs. Dividing each normalized tally times |PGL₂| by its orbit size and by the free dihedral factor 12 gives the claimed per-line counts. In particular (6,6,48) at q=7 is the normalized tally, whereas (6,21,64) is the correct per-line tally. All three formulas are positive for permitted q≥7, and q=5 has only exterior lines hit. Direct independent censuses agreed at q=5,7,11.

## originality

PASS

The supported contribution is the complete rational fiber count by secant, tangent and exterior line type, including the quadratic-character dependence and sharp surjectivity threshold. Credit is not assigned for the already catalogued F_5 distribution or for the geometric notion of a fixed Pascal-line fiber.

## value

PASS

The rational fiber sizes of a classical map give more than an existence result: they distinguish the three line orbits, quantify the field-dependent discrepancy, and explain the first-size exception while proving all-line surjectivity in larger fields. The exact per-line count is useful for finite conic incidence calculations and is not a recomputation of the F_5 catalogue alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
