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

# Reproducibility and verification

Run `python3 check.py` with a standard Python 3 interpreter and no dependencies. The checker uses exact rational weights for all possible binary draw histories for schedules through five steps. It cross-checks the closed second moment recursion, compares all admissible fixed-budget schedules with both sorted extrema, verifies the exact two-adjacent-step swap difference even with arbitrary common prefixes/suffixes, and verifies that the future pure-Pólya risk formula is invariant under one further P step. The same code checks two explicit instances of strict reversal under opposite reinforcement. On packaging it printed `12517 exact-rational assertions passed`.

Proof versus computation: the adjacent-swap formula and Pólya beta continuation in RESULT.md establish the complete theorem for arbitrary \(n\). Exhaustive finite-history checks do not prove any infinite-horizon limit or general quantifier. Publication or historical uniqueness is not independently certified.
