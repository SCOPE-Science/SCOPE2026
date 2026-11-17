---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Every ternary cubic is uniquely normalized in (5^10-1)/4=2,441,406 scalar classes; exhaustive rational tangency masks over all 31 PG(2,5) points show no nonsingular-at-rational-points form exceeds 29 covered points. This supersample includes all geometrically smooth forms. The two displayed smooth representative cubics have 8 and 10 rational points, each with 29-point tangent union; independent direct F5 point/gradient evaluation reproduced both omitted-point pairs. Exact PGL3(F5) orbit enumeration of 93,000 forms per representative exhausts the 186,000 extremizers; geometric smoothness is certified by the full-chart unit Gröbner ideals. Distinct point counts give distinct Frobenius traces -2 and -4 and hence zeta numerators 1+2T+5T² and 1+4T+5T². Reconstructed source checker loops and orbit method were inspected, but the complete 2.44-million-form C++ orbit execution was not rerun in this audit; independent checks corroborate representatives, not full exhaustion.

## originality

FAIL

FAIL: A complete earlier October 25 result establishes the identical 29/31 bound for all cubics, not merely smooth ones; exactly the same two PGL3(F5) classes, orbit size 93000 each, stabilizers 4 and rational point counts 8/10. Its point-count information also immediately fixes the two submitted Weil polynomials. The new representatives are just projectively equivalent choices, and a different finite implementation does not create novelty.

## value

FAIL

FAIL: Although tangent coverage is a natural finite-geometry extremum, the exact extremum and full equality classification are previously established, and the stated elliptic zeta numerators follow from the earlier displayed rational point counts. No distinct new mathematical invariant, theorem or useful refinement survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
