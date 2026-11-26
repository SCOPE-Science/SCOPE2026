---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and evidentiary limits

Run `python3 verify_degree_collapse.py` using Python 3 and the standard library. `verification_output.txt` records the original finite check output. The script generates deleted-edge patterns for the tested shores and counts triangle-free neighborhoods directly, separately from the degree-only expression. It checks the degree expression on four-cycle-free patterns and the first correction coefficient on four-cycle-bearing patterns. Its canonical polynomial-fibre test includes only the four-cycle-free patterns, allowing within-shore permutations and the exchange of equally sized shores. It also directly checks the two center-swapped witnesses for third-shore size one through seven.

The proof in `RESULT.md` handles arbitrary shores and gives the full small-order classification by an explicit table covering all deletion patterns, including the four-edge fibre omitted from the script's fibre test. No finite computation by itself establishes the general polynomial identity, its inverse, or publication priority.
