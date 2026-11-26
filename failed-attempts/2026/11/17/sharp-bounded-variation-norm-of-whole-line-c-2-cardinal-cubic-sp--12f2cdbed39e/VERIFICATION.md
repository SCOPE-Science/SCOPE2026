---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The C² matching condition yields the tridiagonal curvature equation. Its summable Green function follows by solving the characteristic equation and verifying the zero row; bounded polynomial pieces imply uniformly bounded nodal second derivatives, and the homogeneous equation has no nonzero bounded bi-infinite solution. The cubic pieces with the computed curvatures give existence and uniqueness. Summing translated unit steps against the ℓ¹ increments then reduces the exact quotient norm to the step. The central piece has positive derivative and variation one; reflection and geometric curvature ratios give two equal tails. The first right polynomial has equal endpoint ordinates and one interior turning point (its derivative has opposing endpoint signs), so its variation is twice the excursion, and successive tail cells scale by 2−sqrt(3) in absolute value. Independently rebuilt that polynomial and summed its overshoot geometrically to obtain exactly (2+sqrt(3)+2 sqrt(2−sqrt(3)))/3; replay /workspace/independent_exact_checks.py, cubic_cardinal(). The supplied finite natural-boundary stress tests were inspected only as optional corroboration, not used as whole-line evidence.

## originality

FAIL

The distinct indexed record 914665cad692 expressly states the same sharp discrete-to-continuous BV norm for the bi-infinite C² cubic cardinal interpolant, the same radical, and single-step attainment, including the same excess-variation mechanism. This establishes statement-level duplicate coverage, not historical priority: the match has a later catalog date and its full provenance was not resolved. The finite natural-spline comparison is not the basis of this verdict.

## value

FAIL

A sharp whole-line stability factor could be useful in a BV interpolation analysis, but the claimed invariant and witness are already stated for this very operator in the checked corpus. The geometric-tail explanation is also present there at statement level. No distinct stability theorem, parameter range, or other surviving useful finding is established by this record as stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
