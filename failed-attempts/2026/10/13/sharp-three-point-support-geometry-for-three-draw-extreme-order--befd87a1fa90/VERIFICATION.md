---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Positive affine normalization gives {0,t,1} with 0<t<1. The joint (L,U) counts in rank order are 1,6,12,1,6,1 for (0,0),(0,t),(0,1),(t,t),(t,1),(1,1). They give the stated raw moments and positive covariance. The extrema have positive variance because the all-zero and all-one samples occur with positive probability. An independent check yields Var(L) Var(U)-16 Cov(L,U)^2 = 4(2t-1)^2(247(t-1/2)^2+729/4)/177147. This proves the claimed positive correlation bound of 1/4, attained only at t=1/2, and corroborates the derivative proof. The midpoint condition returns to the original support under the affine map. There is no claim about changing parent masses.

## originality

FAIL

The exact midpoint optimization for three draws is already covered by the analytic certificate in the distinct companion record 4. That record restricts its headline to n>=4, but its proof establishes strict monotonicity for the entire parameter region 0<x<1/3, 0<r<3/5 under a=r*x^2 and b=x+a. The n=3 inputs satisfy those inequalities with exactly the bounding values used in that proof. Substitution gives the same strict equality condition and sharp value; no extension argument or extra case work is needed. This is demonstrable scientific redundancy in the records under review, not a claim that one same-day record had historical priority. Other close sources cover the midpoint value or address different optimization problems, not the missing geometry by themselves.

## value

FAIL

The discrete lattice-optimality question is genuine and its three-draw evaluation is a useful illustration. As a standalone narrow invariant, however, this record supplies no distinct exact fact beyond a direct substitution in the companion proof. Its own derivative computation neither strengthens the bound nor adds a separate stability or structural theorem. The result is useful as a worked example of that broader analysis, not a separate surviving finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
