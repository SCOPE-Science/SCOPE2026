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

At a singular point with m nonzero coordinates, the derivative equations on their squares have eigenvalues 2-lambda and 2+(m-1)lambda, giving exactly the stated exclusions. The three disjoint line lists have 4+12+12 members and their binary restrictions are squares, so the odd-characteristic bitangent count gives completeness. The sign and mixed discriminants are in k, equal up to square factors to -3 and 3-lambda; when a line has degree two no contact on it can have degree one because a smooth contact point determines the tangent line. In the coordinate-zero group the discriminant is -4lambda/(1-w); the two choices differ by a square when both radicals are rational. If w is nonrational its quadratic norm is 16lambda^2/e. For nonzero lambda the norm criterion therefore gives unresolved contacts over the quadratic line field precisely when both d and e are nonsquares; if only e is nonsquare and w is rational, the discriminant is already in k. The reduced hyperflex support has one point per line at lambda=0 or 3 only; characteristic five excludes the latter fiber. The two-nonsquare character sum gives (q-chi(-1))/4; the excluded d=-3 has 1-d=4, and d=-1 at lambda=0 must be removed exactly for q=3 modulo 8. Unique tangents give disjoint supports, so the cycle counts and zeta factors follow. I tested the entire dual projective plane over the quadratic line field for each smooth prime-field parameter at p=5,7,11,13, using binary quartic square extraction rather than the radical line list; all cycle counts agreed. An additional scan over F25 checked all rational lines and degree-one contacts there, not the nonrational line orbits over F25. Replay: python3 /workspace/branches/reproductions/ciani.py. The all-prime-power scope follows from the algebra, not these checks.

## originality

PASS

The supported distinct contribution is the uniform Frobenius classification on all reduced contact supports and particularly the criterion and census for degree-four contacts over quadratic line fields. The pencil, its geometric line groups, line descent, all three binary square restrictions, and the two special complex hyperflex examples are not new. The earlier restrictions provide the equations, but the key nonrational case requires a further quadratic-field square-class computation and an exact parameter count; no inspected earlier statement supplies that characterization. The same-day Fermat computation directly overlaps the lambda=0 case, not the full marked family.

## value

PASS

For the natural geometric collection of all theta contacts, the arithmetic data ask more than the field of its bitangent lines. The exact square-class obstruction and its prevalence characterize when the line field misses the contact field, give the actual reduced scheme zeta function, and distinguish this from a recalculation of line orbits or of a single special quartic. The motivation holds for the marked pencil, not for an unclaimed census of isomorphism classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
