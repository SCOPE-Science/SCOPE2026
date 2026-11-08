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

# Verification instructions and boundaries

Use `python3 verify_shapley.py`. The script requires only Python's standard-library exact rational arithmetic, factorial and binomial functions. It constructs every two-party population split up to 14 voters, all coalition compositions, the type-collapsed Shapley expression, and an independent labelled-subset Shapley expression. It then verifies efficiency, all core inequalities, uniqueness of the first bad split and blocking type, and the exact payoff fractions and deficit.

Successful output reports 49 party-size profiles and 1512 coalition-type comparisons, no failing profiles through 13 voters, and only (6,8) at fourteen with blocking composition (6,1) and gap 83/858. The test's proof domain is finite: two parties, 2 seats, harmonic PAV and at least two approved candidates per party. No external or independent audit has been performed.
