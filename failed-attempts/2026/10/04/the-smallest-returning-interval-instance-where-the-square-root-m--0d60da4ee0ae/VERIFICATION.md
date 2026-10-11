---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For 0<r<1 the Gram determinant is positive. Reflection decomposition gives the exact positive square root with S12=r/D>0 and S11-S22=(s/2)(1-(1+s)/D)>0 because D squared minus (1+s) squared equals 2r squared. Rotating the first two SRM vectors therefore has positive derivative (2/3)S12(S11-S22), proving a strict measurement improvement. Chen and Ma cover i=1, and equal-prior discrimination between at most two pure states has optimal SRM, establishing the stated parameter minimality.

## originality

FAIL

The strict SRM suboptimality is mathematically correct, but it is directly covered by a published necessary-and-sufficient SRM criterion. Dalla Pozza and Pierobon prove for an irreducible Gram block that the SRM is optimal if and only if the diagonal entries of its positive square root are equal. Chen and Ma supply the exact returning-interval Gram matrix. The audited computation itself proves S11 differs from S22 for every nontrivial overlap, so the strict failure is an immediate specialization of that prior theorem. The first-parameter boundary combines this with Chen and Ma's i=1 result and the standard binary case; it does not escape the implication-level coverage.

## value

FAIL

The boundary is natural, but once the exact three-state Gram matrix is written down, the central conclusion is a routine specialization of the published necessary-and-sufficient equal-diagonal square-root criterion. Under the common value bar this does not supply an independently substantive mathematical advance beyond applying known general theory to the smallest parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
