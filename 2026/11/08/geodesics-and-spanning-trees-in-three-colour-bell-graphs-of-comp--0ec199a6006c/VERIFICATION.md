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

# Verification of the structural and enumerative formulas

Run `python3 artifacts/verify.py` using the Python standard library; no external package is needed. The script independently generates every unlabelled partition of the labelled vertex set into at most three classes, keeps only partitions into independent blocks of the complete bipartite graph, and joins two partitions precisely when deleting a single vertex gives equal restrictions. It separately constructs the predicted antipodal-cube vertex-sum and compares their full edge sets.

For \((m,n)\) equal to \((3,3),(3,4),(4,4),(3,5),(4,5)\), every pair of Bell states is checked against breadth-first-search distance and complete shortest-path multiplicity, and compared with the closed formula. For graph orders at most sixteen, the tree count is independently calculated from the reduced integer Laplacian using Bareiss elimination and compared with the product formula. Standalone quotient factors \(P_3,P_4,P_5\) receive independent determinant checks; \(P_6\) receives a product and divisibility check.

Expected final marker is `VERIFY_OK`; exact replay output is not considered proof of unrestricted parameter statements. Those follow from the partition reduction, twofold quotient covering, and character-spectrum proof in `RESULT.md`.
