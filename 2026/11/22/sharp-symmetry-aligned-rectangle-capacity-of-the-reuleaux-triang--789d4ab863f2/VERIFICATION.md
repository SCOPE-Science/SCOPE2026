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

The corrected RESULT.md proves the same exact aligned-area formula without assuming the frozen proof's false vertical extent [-h/2,h]. For a rectangle of horizontal half-side u and horizontal center s, its largest absolute abscissa is U=u+|s|. All vertical coordinates must lie in the intersection of the two exact disk intervals, whose lower endpoint is h-Q(U) because Q-P increases to 3h/2, and whose upper endpoint is -h/2+P(U). These bounds are sufficient as well as necessary. The true vertical extent is [h-1,h]. Area is bounded by 2u f(U) <= 2U f(U), with equality only at s=0 and full available height. Strict concavity gives the unique interior root; a rational bracket establishes noncentrality and unequal sides. The frozen u,v,c decimals were wrong at the stated precision; the repair gives the reproduced values without changing the exact result or the stated area. The bounded 80-digit Decimal replay used 120 bisection steps and found area 0.4197167574230241 and the four predicted contacts, with the other eight squared-distance slacks positive. No unrestricted-orientation claim is proved.

## originality

PASS

Bounded evidence supports the exact aligned capacity and optimizer as a distinct result. The closest different indexed contact result is for a circular segment, not a three-disk intersection; polygonal algorithms and the classical least-area theorem do not provide this constrained optimizer. No claim of global priority or unrestricted optimality is warranted.

## value

PASS

The symmetry class is a canonical restriction in a classical constant-width body. Its exact rectangular capacity, contact pattern and unique off-centroid nonsquare optimizer give a sharp feasible-area benchmark and separate this problem from a centered or square ansatz. This value does not depend on claiming arbitrary-orientation optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
