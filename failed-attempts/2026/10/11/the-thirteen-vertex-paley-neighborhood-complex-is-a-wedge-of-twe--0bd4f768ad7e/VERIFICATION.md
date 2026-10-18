---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

From nonzero squares Q={1,3,4,9,10,12} modulo 13 every maximal open-neighborhood simplex is a translate v+Q. Complete independent enumeration gives f=(13,78,221,195,78,13), 598 nonempty faces; the fixed-vertex toggle order gives 286 valid pairs, acyclicity across all 2067 nonempty Hasse covers, and critical one dim0+25 dim2, hence integral ∨25 S² by Forman. A direct independent check of all 4-subsets gives α=3, and the claimed 5-color assignment is proper, so χ=5. Lovász connectivity lower bound uses conn=1, giving χ≥4; the claimed strict gap is correct.

## originality

FAIL

A separate public Resultary record titled “The neighborhood complex of the order-13 Paley graph is a wedge of 25 two-spheres” states and proves EXACTLY N(P13)≃∨25 S² for the identical Q13 graph using a different 286-pair full acyclic matching. Its entire RESULT.md has been read. The remaining χ=5 and Lovász bound4 are straightforward well-known graph coloring/standard connectivity deductions, not a surviving substantive original finding on which to repair the exact duplicated central result.

## value

PASS

The homotopy type of a named six-regular, 13-vertex strongly regular Paley graph’s Lovász neighborhood complex is a natural exact topological invariant with relevance to chromatic topology, and is inherently a motivated computation (even though O fails because this exact fact is published elsewhere). The coloring comparison is a clear secondary illustration, not a second independent contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
