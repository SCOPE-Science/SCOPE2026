---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The analytic proof uses a cone-measure radial factorization for convex free sums, a Dirichlet moment identity, and induction through graph disjoint unions and joins. The induced four-vertex path is integrated separately to establish the exact failure outside the hereditary class.

The accompanying `checker.py` was run directly from the same directory. It enumerates stable-set indicator vertices independently of the cotree calculation, triangulates each polytope, uses integer Bareiss determinants to get exact simplex volumes, and integrates first and second moments as rational numbers. It checked all labeled cographs of orders two through five and thirty additional seeded six-vertex cographs: 564 graph configurations, 9,590 full-dimensional simplices, 2,766 edge pairs, 1,220 positive nonedge pairs, and 1,522 zero-covariance nonedge pairs. The independent simplex route also checked 1,120 cubic moments for the three- and four-vertex cographs. A symbolic polynomial integral independently confirms the nonedge covariance of the induced four-vertex path as \(-11/3750\).

Expected successful check marker:

`COGRAPH_COTREE_MOMENTS_CHECKS_PASSED 564 9590 2766 1220 1522 CUBIC 1120 P4_NONEDGE_COV=-11/3750`

Execute `python checker.py` with NumPy, SciPy and SymPy installed. These finite tests are corroborating evidence, not a proof of the all-order theorem or an assessment of historical novelty. An independent mathematical audit has not been performed.
