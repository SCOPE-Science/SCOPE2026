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

# Reproducibility
Execute `python3 verify_c6.py c6_branch_certificates.json` with Python 3.9+ in the directory containing the two named artifacts. The verifier checks the complete prefix certificate using exact rational and integer arithmetic. It does not import an optimizer or rely on rounding. It also evaluates the explicit attaining integer signals independently.

Successful check totals: 15,139 terminal certificates, 1,739 feasible strict branches, 107,818 branch-cut comparisons; upper bound 19/10 with equality. These finite computations are complemented by the analytic branch-integration and coarea reductions in RESULT.md. Independent audit has not been performed.
