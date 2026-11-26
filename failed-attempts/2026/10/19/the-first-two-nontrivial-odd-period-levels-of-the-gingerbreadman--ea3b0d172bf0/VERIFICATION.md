---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On a closed sign branch the map is affine with determinant-one linear part. A sign itinerary is feasible exactly when all branch inequalities hold along the affine iteration and (I−A_n)z=d_n. Weak inequalities retain the switching line; Fourier–Motzkin projection is valid even with missing bounds or singular return equations. Independent replay `python3 -B /workspace/reproduce_frozen.py 3` propagates the scalar recurrence, solves each exact rational closing system, and checks singular cases by two-dimensional feasibility via the closest feasible point to the origin (origin, projection onto an active line, or intersection of independent active lines). No singular itinerary was feasible. The point counts for n=1,3,5,7,9,11 are 1,1,11,1,1,23. Direct iteration verifies the unique fixed point (1,1), the four listed orbit representatives, their least periods and absence of zero first coordinates. The computed return traces 3,1 and 5,−5 give the stated elliptic or saddle types since the determinants are one. The uploaded transcript and verifier were inspected, not executed.

## originality

FAIL

An earlier catalogued, scientifically matching whole-plane result already determines the complete claimed odd-period inventory through eleven, including all four cycles and their stabilities. Restriction to odd periods leaves no distinct surviving scientific assertion. The unknown publication priority of other sources is a separate issue.

## value

FAIL

A global short-period inventory and stability classification for this map are meaningful, but the frozen odd-only recomputation reproduces the same cycles, exclusions and traces from a wider exact inventory. The alternative smaller-dimensional implementation is corroboration, not a distinct scientific contribution in the stated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
