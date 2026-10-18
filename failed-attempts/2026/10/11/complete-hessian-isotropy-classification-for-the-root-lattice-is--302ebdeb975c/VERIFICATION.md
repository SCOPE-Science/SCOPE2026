---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Assuming precisely the source equations quoted in the frozen RESULT.md, orthogonal diagonal/off-diagonal projections have coefficients a_d,b_d, so condition ratio κ_d=b_d/a_d. Independent exact SymPy verifies κ_d−1=(d−1)(d−4)/[d(2d−3)], κ_{d+1}−κ_d=(7d²−9d+4)/[d(d+1)(2d−3)(2d−1)]>0 for all d≥4, κ_4=1, κ_5=39/35, and κ_d→3/2. Source quoted scalar forms for A2 and E6–E8 entail the remaining isotropic cases. Valid for optimized local Hessian only, not global isoperimetry.

## originality

FAIL

The entire advertised isotropy set and all-rank Hessian condition-number profile are direct algebraic consequences of the earlier Novaga–Song all-rank Hessian coefficients and their already-proved strict-root-local-minima list, not an independent original theorem. This is decisive implication coverage, not failure arising from source access alone.

## value

FAIL

This is exclusively a ratio, equality check, telescoped first difference and limit of the already published all-rank quadratic Hessian coefficients. It introduces no new intrinsic invariant beyond taking a standard matrix condition number of an explicitly diagonalized two-eigenspace form; the classification is mechanistically implied and does not fill a substantive research gap. Exact algebra alone does not confer scientific value under the shared bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
