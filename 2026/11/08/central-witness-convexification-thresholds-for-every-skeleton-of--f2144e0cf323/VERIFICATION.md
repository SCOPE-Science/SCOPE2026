---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS: In barycentric blocks n_i=d_i+1, a target Y of total 1+t in each factor decomposes as A+tB with A in k-skeleton iff one can choose positive supports s_i whose sum of costs s_i-1 is at most k and whose largest s_i target coordinates carry at least 1. Their minimum possible sum over target blocks is s_i(1+t)/n_i at the product centroid. Consequently Σceil(n_i/(1+t))≤k+r is sufficient for every target and necessary for the centroid; all t≥0 boundaries are included. The minimum over finitely many support allowances gives the exact rational attained threshold. An independent exact-fraction support-budget enumeration for small products (1,1),(1,2),(2,2),(1,1,1), sample t including 0,1/2,1,2 confirmed the ceiling/centroid criterion. No finite enumeration substitutes for the general capacity argument.

## originality

PASS

The product-of-simplices skeleton support-allocation/centroid witness equivalence is not supplied by the previously published simplex-skeleton equal-weight self-averaging theorem, because the Minkowski operation differs. Meyer offers a general exposed-set criterion but no inspected explicit all-product ceiling classification. Best-of-knowledge PASS with disclosed risk from Meyer’s inaccessible full text.

## value

PASS

PASS: A natural all-dimensional class of polytopes and every closed skeleton receives an exact, attained rational Schneider index, and the scaled centroid is a universal obstruction. This clean single-witness classification and factor-specific budget is a motivated structural geometric theorem, not an unmotivated low-dimensional slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
