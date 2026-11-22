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

# Verification

Execute `python3 check.py` in the directory containing this document. The script enumerates all finite edge-pattern quotients for each of the five groups, every split \(k=n+r\) with \(k\leq5\), and directly counts their equivalence classes. It separately enumerates translation subgroups for \(k\leq7\). Expected complete output is preserved in `checks.txt`.

The direct finite enumeration makes no assumptions about the closed-form rank functions; those are compared after explicit orbit construction. It cannot certify infinitely many parameter values, the absence of earlier equivalent publications, or independent validation. The human-readable proof establishes the general cases using finite field linear algebra and \(\omega\)-categoricity.
